# Import dependencies
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import pandas as pd

# Create class for items
class Item:
    def __init__(self):
        self.name = ""
        self.damage = 0
        self.tears = 0
        self.range = 0
    
    # function to check if item with this name already exist
    def searchByName(self, name):
        if self.name == name:
            return True

# Create class for characters
class Character:
    def __init__(self):
        self.name = ""
        self.damage = 0
        self.tears = 0
        self.range = 0

# Create temporary array for items
array = []

# Function to get items stats
def getStats(rows, typeStat):
    for row in rows:
        # Get all names and description of items
        name = row.find_elements(By.TAG_NAME, 'td')[0].text
        desc = row.find_elements(By.TAG_NAME, 'td')[4].text.lower()
        
        """ 
            Check "+" to get only description with statistics (example : "+1 damage")
            Items without statisic values does not interest us.
        """
        if "+" in desc:
            # Split all words in description to get only what we want
            descArr = desc.split(' ')
            
            for i in range(len(descArr)):
                """
                    We need to get only number before statistic 
                    i < len(descArr) - 1 -> to avoid index out of range
                    "+" in descArr[i]  -> to check values with "+"
                    descArr[i+1] == typeStat or descArr[i+1] == typeStat + ',' -> to check value before a statistic name
                """
                if i < len(descArr) - 1 and "+" in descArr[i] and (descArr[i+1] == typeStat or descArr[i+1] == typeStat + ','):
                    # New instance of item with name, damage, tears, range
                    item = Item()
                    item.name = name
                    if(typeStat == "damage"):
                        item.damage = desc.split(' ')[i]
                        array.append(item)
                    elif(typeStat == "tears"):
                        isExist = False
                        # If item already exist juste add the statistic
                        for existItem in array:
                            if(existItem.searchByName(name) == True):
                                existItem.tears = desc.split(' ')[i]
                                isExist = True
                        if isExist == False:
                            item.tears = desc.split(' ')[i]
                            array.append(item)
                    elif(typeStat == "range"):
                        isExist = False
                        for existItem in array:
                            if(existItem.searchByName(name) == True):
                                existItem.range = desc.split(' ')[i]
                                isExist = True
                        if isExist == False:
                            item.range = desc.split(' ')[i]
                            array.append(item)
                    break

def getPage(url, element, typeStat):
    # Init driver
    driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX)

    # Get item page
    driver.get(url)

    # Wait for load page
    time.sleep(2)

    #Accept cookies
    driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/div[2]').click()
    time.sleep(1)

    #Get all items
    rows = driver.find_elements(By.XPATH, element)
    getStats(rows, typeStat)
    # Close driver
    driver.close()

# Call the function to get page and wait before getting another page to simulate a real behaviour
getPage("https://bindingofisaacrebirth.fandom.com/wiki/Damage", '//*[@id="mw-content-text"]/div/table[4]/tbody/tr', "damage")

getPage("https://bindingofisaacrebirth.fandom.com/wiki/Tears",  '//*[@id="mw-content-text"]/div/table[5]/tbody/tr', "tears")

getPage("https://bindingofisaacrebirth.fandom.com/wiki/Range",  '//*[@id="mw-content-text"]/div/table[4]/tbody/tr', "range")

# Save items and characters into csv file
def saveCsv(arraytmp, name):
    array = []
    for item in arraytmp:
        array.append({"name": item.name, "damage": item.damage, "tears": item.tears, "range": item.range})
    df = pd.DataFrame(array)
    df.style
    df.to_csv(name, index=False)  
    print(df.head())

saveCsv(array,'datas/items.csv')

# Temporary array for character
tmpArrayCharacters = []

def getPageCharacter():
    # Init driver
    driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX)

    # Get character page
    driver.get("https://bindingofisaacrebirth.fandom.com/fr/wiki/Personnages")

    # Wait for load page
    time.sleep(2)

    #Accept cookies
    driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div[2]/div[2]').click()
    time.sleep(1)

    #Get all characters
    names = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/div[3]/div/table/tbody/tr[2]/td')
    damages = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/div[3]/div/table/tbody/tr[5]/td')
    tears = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/div[3]/div/table/tbody/tr[6]/td')
    ranges = driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div/div[3]/div/table/tbody/tr[8]/td')
    
    for i in range(len(names)):
        if(i < len(names) - 1):
            # New character instance for all
            newCharacter = Character()
            newCharacter.name = names[i + 1].text
            newCharacter.damage = damages[i].text.split(' (')[0]
            newCharacter.tears = tears[i].text
            newCharacter.range = ranges[i].text
            
            tmpArrayCharacters.append(newCharacter)

    # Close driver
    driver.close()

# Call function to get characters page
getPageCharacter()

saveCsv(tmpArrayCharacters,'datas/characters.csv')
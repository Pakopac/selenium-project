# Isaac scrapping stats

## Overview

This project is based on the game the binding of isaac.\
The goal of this project is to simulate stats with a character and some stuffs.
<br><br>
We scrap this site using Selenium to get statistics\
https://bindingofisaacrebirth.fandom.com/wiki/Binding_of_Isaac:_Rebirth_Wiki 
<br><br>
You can check all details and explains by reading the notebook :thumbsup:\
 https://github.com/Pakopac/selenium-project/blob/master/project.ipynb

## script.&#8203;py
This is the script for scrapping \
First we get items by stat with theses pages: \
https://bindingofisaacrebirth.fandom.com/wiki/Damage (for damage stat) \
https://bindingofisaacrebirth.fandom.com/wiki/Tears (for tears stat) \
https://bindingofisaacrebirth.fandom.com/wiki/Range (for range stat) \
And get from table
![Capture d’écran du 2021-12-16 12-23-48](https://user-images.githubusercontent.com/33722914/146364717-76d617d5-93d1-4ca7-8d50-16e7d55c0812.png)

Then we get character stats from this page: \
https://bindingofisaacrebirth.fandom.com/fr/wiki/Personnages \
run: \
```
cd project
python script.py
```

## request.&#8203;py
Get stats for a character and items. \
run command 
```
cd project
python request.py 7 1 5 9
```
First argument is id of character and others are ids of items \
The result:
```
--- Samson ---
Damage: 7.0
Tears: -0.05
Range: 19.0
```
## Docker
Docker does not work yet !!
```
cd project
docker build -t selenium-project-0.1 .
docker run -v data-selenium selenium-project-0.1
```
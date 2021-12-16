#Get Python image
FROM python:latest

# Set work directory
WORKDIR /project

# Copy script into docker
COPY . /project

# Create directory for csv files
RUN mkdir /datas

# install requirements
RUN pip install -r requirements.txt

# execute script
CMD [ "python", "script.py"]
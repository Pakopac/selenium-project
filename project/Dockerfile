#Get Python image
FROM python:3.7

RUN mkdir /project \
    && apt-get update \
    && apt-get install -y \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    xdg-utils \
    libgdk-pixbuf2.0-0

WORKDIR /project

COPY requirements.txt /project/
COPY drivers /project/drivers

RUN chmod a+x drivers
RUN pip install --upgrade pip \
    && pip install -r requirements.txt --upgrade \
    && dpkg -i drivers/google-chrome-stable_current_amd64.deb \
    && chmod a+x drivers/chromedriver

COPY . .
ENV DISPLAY=:20

RUN Xvfb :20 -screen 0 1024x768x24 -nolisten tcp &

# execute script
CMD [ "python", "script.py"]
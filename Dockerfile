FROM python:3.7

RUN apt-get update \
	&& apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

#download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install


# install chromedriver
RUN apt-get install -yqq unzip  \
	&& wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip  \
	&& unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


#install python dependencies
COPY requirements.txt requirements.txt 
RUN pip install -r ./requirements.txt 

#some envs for gunicorn, I assume
#ENV APP_HOME /app 
#ENV PORT 5000

# set display port to avoid crash
ENV DISPLAY=:99

COPY app.py app.py
CMD ["python", "./app.py"]

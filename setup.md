su -s /bin/bash www-data

// to www-data

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install unzip

sudo apt-get install libpango1.0-0
sudo apt-get -f install
wget -c "https://www.slimjet.com/chrome/download-chrome.php?file=lnx%2Fchrome64_54.0.2840.71.deb"
sudo dpkg -i download-chrome.php?file=lnx%2Fchrome64_54.0.2840.71.deb
sudo rm download-chrome.php?file=lnx%2Fchrome64_54.0.2840.71.deb
sudo apt-get install -y -f

curl "http://chromedriver.storage.googleapis.com/LATEST_RELEASE"

sudo mkdir /var/chromedriver
cd /var/chromedriver
wget "http://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip"

unzip chromedriver_linux64.zip


sudo apt-get -y install python3-pip python3-dev build-essential libssl-dev libffi-dev xvfb



pip3 install --upgrade pip

#Installing Virtualenv will allow us to create a virtual environment and install any Python packages in it without affecting our system’s Python. Go here learn more about Virtualenv:

sudo pip3 install virtualenv

#Set up a virtual environment with the following command. It will create the folder /var/venv/:

virtualenv /var/venv

#Activate the virtual environment with:
source /var/venv/bin/activate

#Let’s get Selenium and PyVirtualDisplay. In your venv, run:
pip3 install selenium==3.0.0
pip3 install pyvirtualdisplay==0.2.1



######


Step 2 – Install Google Chrome
Now install Latest Google chrome package on your system using the below list commands. Google chrome headless feature opens multipe doors for the automation.

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
Step 3 – Install ChromeDriver
You are also required to setup ChromeDriver on your system. ChromeDriver is a standalone server which implements WebDriver’s wire protocol for Chromium. The WebDriver is an open source tool for automated testing of web apps across multiple browsers.
###
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
####
You can find the latest ChromeDriver on its official download page. Now execute below commands to configure ChromeDriver on your system.

sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
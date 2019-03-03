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
pip install selenium==3.0.0
pip install pyvirtualdisplay==0.2.1
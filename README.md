# flask-leds

A Flask server to control an LED strip from the Raspberry Pi using an [Adafruit PCA9685](https://www.adafruit.com/product/815).

## Setting up the Raspberry Pi

Start from a Raspbian Lite installation

### Install system software:

        sudo apt-get install vim samba samba-common-bin python3-pip libffi-dev
	
### Install Adafruit PWM driver

        sudo apt-get install git build-essential python-dev
        cd ~
        git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
        cd Adafruit_Python_PCA9685
        sudo python setup.py install
    
### Install and configure `virtualenv` and `virtualenvwrapper`

        sudo pip3 install virtualenv
        sudo pip3 install virtualenvwrapper
        
        mkdir ~/projects
        
Add these lines to .profile:

        export WORKON_HOME=$HOME/.virtualenvs
        export PROJECT_HOME=$HOME/projects
        export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
        source /usr/local/bin/virtualenvwrapper.sh

Reload .profile with `source .profile`        

## Set up Flask project

        mkproject <projectname>
        pip install Flask ipython sqlalchemy flask-sqlalchemy flask-migrate Flask-Login py-bcrypt flask-bcrypt Flask-Restless Adafruit_PCA9685 flask_script


## Set up virtualenvwrapper hooks for the leds project

Copy the contents of the `virtualenvwrapper` directory to ~/.virtualenvs/leds/bin

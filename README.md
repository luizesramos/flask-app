# flask-app

Flask app exercisiong different features of the Flask framework.

# Recommended Software

Install brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install python3 (implicitly installs pip3)
brew install python3

# Create the application project and virtual environment

Create it manually or with PyCharmCE, then browse to the project directory and create a virtual environment.

mkdir -P flask-app/venv
cd flask-app
python3 -m venv venv

Activate the virtual environment
source .venv/bin/activate

Install flask in the virtual enviroment
pip install flask

Deactivate the virtual environment
deactivate
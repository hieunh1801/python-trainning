# Create project API step by step

__PIP__
| Command line                   | Description                                            |
|:-------------------------------|:-------------------------------------------------------|
| pip freeze > requirement.txt   | extract library to file requirement.txt                |
| pip install -r requirement.txt | download and install library from file requirement.txt |
| pip list                       | show all library in current enviroment                 |
| pip uninstall SomePackage      |                                                        |

__VIRTUALENV__
| Command line             | Description                               |
|:-------------------------|:------------------------------------------|
| pip install virtualenv   | download and install virtualenv           |
| virtualenv --version     | test                                      |
| virtualenv venv_name     | create virtual environment name venv_name |
| source venv_flask_sqlite/Scripts/activate | to be using this virtual environment      |

__RUN APP__
| Command line               | Description |
|:---------------------------|:------------|
| set FLASK_APP=server.py |             |
| flask run                  | run app     |
set FLASK_APP=server.py && flask run
## Step 1: Configuration


### 1.1 Prerequisite instal
- Python 3.0: check __python --version__
- Pip: check __pip --version__
- virtualenv


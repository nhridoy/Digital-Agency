# Digital Agency
 
# Follow these Steps Carefully
## Install Git
[Download From Here](https://git-scm.com/downloads)

## Install Python (3.9.8 Recommended)
[Download From Here](https://www.python.org/downloads/release/python-398/)

## Commands to run
### Clone
```commandline
git clone https://github.com/nhridoy/Digital-Agency.git
```

### Create Virtual Environment
```commandline
py -m venv venv
```
### Activate Virtual Environment (for cmd)
```commandline
cd venv/Scripts/activate
```
### Install requirements
```commandline
pip install -r requirements.txt
```
### MakeMigrations and Migrate
```commandline
py manage.py makemigrations
```
```commandline
py manage.py migrate
```
### Create SuperUser
```commandline
py manage.py createsuperuser
```

_N.B: Currently Using sqlite database for development purpose._

**_N.B: Never work on master branch. Create your own branch to work on._**
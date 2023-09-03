# FlaskLearning
Learning Flask from CodeWithHarry

python --version
pip install virtualenv
virtualenv flaskenv

run in powershell admin to run all scripts
Set-ExecutionPolicy unrestricted

To activate environment (If working on visual studio)
 .\flaskenv\Scripts\activate.ps1

pip install Flask

create a minimal Flask App
create 2 folders > static | templates

ORM facility
pip install flask-sqlalchemy

Method 1:
python
$ from app import db
$ db.create_all()

Method 2:
flask shell
$ db.create_all()

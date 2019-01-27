## Backend

**Setup**

Dependencies:

    Python 2.7.13+

**Create a Python virtual environment, install package dependencies**

./python virtualenv syspets

./source syspets/bin/activate

./pip install -U -r syspets/requeriments/base.txt


### Database PostgreSQL

**Create a user and database on PostgreSQL (run psql):**

CREATE ROLE pets_admin WITH LOGIN PASSWORD 'password';<br/>
CREATE DATABASE pets;<br/>
ALTER DATABASE pets OWNER TO pets_admin<br/>
GRANT ALL PRIVILEGES ON DATABASE pets TO pets_admin;<br/>


### Initialize the database, create an admin user:

./python manage.py createsuperuser--

./python manage.py makemigrations --settings=syspets.settings.locale<br/>
./python manage.py makemigrations users --settings=syspets.settings.locale<br/>
./python manage.py makemigrations registration --settings=syspets.settings.locale<br/>
./python manage.py makemigrations adnews --settings=syspets.settings.locale  
./python manage.py migrate --settings=syspets.settings.locale  


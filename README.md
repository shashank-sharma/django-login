# Django Login

Django login is a project used to show log in feature with Django authentication. It takes username at first and password and then it will let you log in.

Demo: [Heroku Site](http://django-login.herokuapp.com)

### Technical Details:

1. Python 3.6
2. Django 1.11
3. PostgreSQL
4. Materialize CSS Framework

### Installation

Installation part is pretty easy:

Step 1: Clone the given repository in your local machine

`git clone https://github.com/shashank-sharma/django-login/`

Step 2: Now change directory and then you can create virtual environment by using:

`python3.6 -m venv myvenv`

Note: You might need to instsall virtualenv by apt-get install virtualenv

Step 3: After creating virtual environment do activate it by:

`source myvenv bin/activate`

For Windows it will be like: `myvenv\Scripts\activate`

Step 4: Install dependencies by using:

`pip install -r requirements.txt`

Step 5: Now migrate django project:

`python3.6 manage.py makemigrations`

`python3.6 manage.py migrate`

Step 6: Change few fields:

GMAIL_USER, GMAIL_KEY in mysite/settings.py so that your mailing system works fine.

Step 7: Run your project by doing:

`python3.6 manage.py runserver`

### Additional information

There is automatic deploy to heroku site with this github repository so there are no extra hidden codes used except few environment variables like password.


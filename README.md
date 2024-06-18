# LittleLemon
I want you to test. An example could look like the following:

# User Settings
create user http://127.0.0.1:8000/auth/users/

check tokens http://127.0.0.1:8000/auth/token/login

# API Check
you need login or set token

http://127.0.0.1:8000/restaurant/menu/

you donot need login

http://127.0.0.1:8000/restaurant/menu/1

you need login or set token

http://127.0.0.1:8000/restaurant/booking/tables/

http://127.0.0.1:8000/restaurant/booking/tables/1/

I used this user, but you use your local mysql, so you need create users.

username: admin
email: example@email.com
pass: 123@!pass

# Run server
pipenv install
python manage.py makemigrations && python manage.py migrate && python manage.py runserver

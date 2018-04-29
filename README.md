# blog-mockup-python

## What it is
This is a mock blog application built with Python/Django and React. I decided to set up an API built with Django REST Framework hooked up to a PostreSQL server as the backend and React + Next.js for the frontend. 

## Requirements
- ensure that you have the latest versions of Python and Node.js installed.
- install PostgreSQL server on your machine and use pgAdmin or an interactive terminal to create a DB called 'SmallBlog'. 
- Create a user called 'blog_service_account' with the password '!P@ssw0rd'. 
    -Make sure the user has permissions to create tables.
- start the Python virtual environment
    - execute the 'activate' script located in `blog-mockup-python\backend\env\Scripts`
- Migrate model changes to 'SmallBlog' db
    - migrations should be included so just go to `blog-mockup-python\backend\api` directory and execute `python manage.py migrate` in order to create all necessary tables

## How to start it up
1. make sure PostgreSQL is running
2. make sure Python virtual env is running
3. execute `python manage.py runserver` in `blog-mockup-python\backend` directory
4. go to `blog-mockup-python\frontend` directory and execute `npm run dev` to start the development node server for the front end

# Countdown App
Hi, I`m a student learning backend web developement and this is my first python django portfolio-project.
## About
This is a simple app that allows you to create countdowns to watch how your favorite events are coming. You can create a countdown for any time in future, specify description, text that will be visible when countdown finishes and share the link with friends. Also, authenticated users can bookmark countdowns and press buttons with emoji to show their reaction.
## Work example
![](https://i.imgur.com/HFOdCLY.gif)

## Try it out
Clone the repository:
```bash
git clone https://github.com/kokokojo2/CountDown
cd CountDown
```
Make and activate virtual environment:
```bash
python -m venv countdown_env
countdown_env\Scripts\activate
```
Install needed requirements:
```bash
pip install -r requirements.txt
```
Create sqlite3 database:
```bash
python manage.py makemigrations
python manage.py migrate
```
Run developement server:
```bash
python manage.py runserver
```
After following these steps, open [this](http://127.0.0.1:8000/) url in your browser to check out the work of application.

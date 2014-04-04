#tilbot

![Screenshot](http://i.imgur.com/bilVFxp.png)

A small flask application that collects and displays "TIL" comments from Reddit, written in Python 3. 

I wrote this to learn about `praw` and databases, especially `sqlalchemy`.

##Installation
- Clone this git repo
- Create and activate a virtualenv
- Install the requirements:

        pip install -r requirements.txt

- Run the following command to setup the database:

	    python manage.py db upgrade

- Run the scraper and the flask app:

		python manage.py scrape
		python manage.py runserver

Note that the scraper will request credentials for a Reddit account. As soon as the scraper finds a TIL post, you can refresh the flask site and the post will be visible there.

You can also run the following command to get an interactive shell with `app`, `db` and the `Comment` and `Author` models available:

    python manage.py shell


---
Licensed under GPL v3

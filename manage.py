from flask_script import Manager, Server, Shell, Command
from flask_migrate import MigrateCommand

from tilbot import app, db
from tilbot.models import Comment, Author
import til_scraper

manager = Manager(app)


def _make_context():
    return {"app": app, "db": db, "Comment": Comment, "Author": Author}


class Scrape(Command):
    """Run scraper"""

    def run(self):
        til_scraper.main()

manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("scrape", Scrape())

if __name__ == "__main__":
    manager.run()

import datetime
import praw

from collections import deque
from time import sleep

from tilbot import db
from tilbot.models import Comment, Author


def comment_exists(comment_id):
    """Return True if comment_id is in the database"""
    exists = Comment.query.filter(Comment.id == comment_id).first()

    return bool(exists)


def get_author(author_id, name):
    """Return an Author from the database or a new one if the author_id isn't found"""
    author = Author.query.filter(Author.id == author_id).first()

    if not author:
        author = Author(id=author_id, name=name)

    return author


def save_comment(r_comment):
    """Add a comment to the database"""
    author = get_author(r_comment.author.id, r_comment.author.name)

    time = datetime.datetime.fromtimestamp(r_comment.created_utc)
    comment = Comment(id=r_comment.id, body=r_comment.body, permalink=r_comment.permalink,
                      subreddit=r_comment.subreddit.display_name, timestamp=time, author=author)

    db.session.add(comment)
    db.session.commit()


def valid_til(comment_body):
    """Return True if the comment seems to be a valid TIL"""
    if not comment_body.startswith("TIL"):
        return False

    # Remove "TIL..."
    if len(comment_body) < 8:
        return False

    return True


def main():
    """Main program loop"""
    try:
        user_agent = "TIL getter by /u/dmzda"
        r = praw.Reddit(user_agent=user_agent)
        r.login()

        done = deque(maxlen=1000)

        while True:
            all_comments = r.get_comments("all", limit=None)
            for comment in all_comments:
                if comment.id not in done and valid_til(comment.body):
                    if comment_exists(comment.id):
                        print(comment.id, "already exists")
                    else:
                        save_comment(comment)
                        print(comment.id, comment.body)
                done.append(comment.id)
            sleep(32)

    except Exception as err:
        print(err)
        sleep(300)
        main()


if __name__ == "__main__":
    main()

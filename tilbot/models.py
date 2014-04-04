from tilbot import db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.String, primary_key=True)
    body = db.Column(db.String)
    permalink = db.Column(db.String)
    subreddit = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    author_id = db.Column(db.String, db.ForeignKey("authors.id"))

    author = db.relationship("Author", backref=db.backref("comments"))

    def __repr__(self):
        return "<Comment(id={}, body={}, subreddit={}, timestamp={}, author_id={})>".format(
            self.id, self.body[:20] + "...", self.subreddit, self.timestamp, self.author_id)


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "<Author(id={}, name={})>".format(self.id, self.name)

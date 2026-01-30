class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(200),nullable=False,unique=True)
    password_hash=db.Column(db.String(200),nullable=False)
    
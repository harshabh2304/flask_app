class Cafe(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(300),nullable=False)
    location=db.Column(db.String(300),nullable=False)
    power_socket=db.Column(db.Boolean,nullable=False)
    rating=db.Column(db.Integer)
    opening_time=db.Column(db.String(100),nullable=False)
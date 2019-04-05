from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    program = db.Column(db.String(64), index=True)
    batch = db.Column(db.String(32), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Teacher(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Semester(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    semester_no = db.Column(db.Integer, index=True, unique=True)
    subjects = db.relationship('Subject', backref='semester_name', lazy='dynamic')

class Subject(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    subjectname = db.Column(db.String(64), index=True)
    teachername = db.Column(db.String(64), index=True)
    day = db.Column(db.String(32), index=True)
    room = db.Column(db.String(32), index=True)
    timing = db.Column(db.String(64), index=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('semester.id')) 

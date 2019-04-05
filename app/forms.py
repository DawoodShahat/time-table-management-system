from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

# Add User usecase
class AddStudentForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    program = StringField('Program', validators=[DataRequired()])
    batch = StringField('Batch', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Password', validators=[DataRequired()])
    password_hash_confirm = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password_hash')])
    addstudent = SubmitField('Add Student')

class AddTeacherForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password_hash = PasswordField('Password', validators=[DataRequired()])
    password_hash_confirm = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password_hash')])
    addteacher = SubmitField('Add Teacher')

# Remove User usecase
class RemoveStudentForm(FlaskForm):
    searchname = StringField('Search', validators=[DataRequired()])
    remove = SubmitField('Remove Student')

class RemoveTeacherForm(FlaskForm):
    searchname = StringField('Search', validators=[DataRequired()])
    remove = SubmitField('Remove Teacher')

# Search User usecase
class SearchStudentForm(FlaskForm):
    searchname = StringField('Search', validators=[DataRequired()])
    search = SubmitField('Search Student')

class SearchTeacherForm(FlaskForm):
    searchname = StringField('Search', validators=[DataRequired()])
    search = SubmitField('Search Teacher')

# Create Time Table usecase
class CreateTimeTableForm(FlaskForm):
    select_semester = SelectField('Select Semester')
    pick_subject = StringField('Subject Name')
    teacher_name = StringField('Teacher Name')
    day = SelectField('Day')
    room_no = StringField('Room No')
    timing = SelectField('Timing')
    add_subject_to = SubmitField('Add Subject to Time Table')

# View Time Table usecase
class ViewTimeTableForm(FlaskForm):
    select_semester = SelectField('Select Semester')

# Create Program usecase
class CreateSemesterForm(FlaskForm):
    semester_no = StringField('Semester No')
    batch = StringField('Batch')
    program = StringField('Program Name')
    create_semester = SubmitField('Create Semester')



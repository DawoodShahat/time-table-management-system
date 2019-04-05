from app import app, db
from flask import render_template, redirect, request, url_for, flash, jsonify
from app.forms import LoginForm, AddStudentForm, AddTeacherForm, RemoveStudentForm, RemoveTeacherForm, SearchStudentForm, SearchTeacherForm, CreateTimeTableForm, ViewTimeTableForm, CreateSemesterForm

from app.models import Student, Teacher, Semester, Subject
from sqlalchemy import asc

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template('base.html', form=form)

@app.route('/admin/')
@app.route('/admin')
def admin():
    return render_template('admin.html', title='Administrator')

@app.route('/admin/adduser', methods=['GET', 'POST'])
def adduser():
    return render_template('adduser.html', title='Add User')

@app.route('/admin/adduser/student', methods=['GET', 'POST'])
def addstudent():

    form = AddStudentForm()
    if form.validate_on_submit():
        user = Student(username=form.username.data, program=form.program.data, batch=form.batch.data, email=form.email.data) 
        user.set_password(form.password_hash.data) 
        db.session.add(user)
        db.session.commit()
        flash('Student is added Successfully')
        return redirect(url_for('addstudent'))
    return render_template('addstudent.html', form=form)

@app.route('/admin/adduser/teacher', methods=['GET', 'POST'])
def addteacher():

    form = AddTeacherForm()
    if form.validate_on_submit():
        user = Teacher(username=form.username.data, email=form.email.data) 
        user.set_password(form.password_hash.data)
        db.session.add(user)
        db.session.commit()
        flash('Teacher is added Successfully')
        return redirect(url_for('addteacher'))
    return render_template('addteacher.html', form=form)


@app.route('/admin/removeuser')
def removeuser():
    return render_template('removeuser.html',title='Remove User', usecase='removeuser')

@app.route('/admin/removeuser/student', methods=['GET', 'POST'])
def removestudent():

    form = RemoveStudentForm()
    if form.validate_on_submit():    
        user = Student.query.filter_by(username=form.searchname.data).first()
        if search_user(form, Student):
            db.session.delete(user)
            db.session.commit()
            flash("{} is found and successfully removed!".format(form.searchname.data))
        else:
            flash("{} is not found!".format(form.searchname.data))

    return render_template('removestudent.html', form=form)

@app.route('/admin/removeuser/teacher', methods=['GET', 'POST'])
def removeteacher():

    form = RemoveTeacherForm()
    if form.validate_on_submit():    
        user = Teacher.query.filter_by(username=form.searchname.data).first()
        if search_user(form, Teacher):
            db.session.delete(user)
            db.session.commit()
            flash("{} is found and successfully removed!".format(form.searchname.data))
        else:
            flash("{} is not found!".format(form.searchname.data))
    return render_template('removeteacher.html', form=form)


# Search User usecase
@app.route('/admin/searchuser')
def searchuser():
    return render_template('searchuser.html', title='Search User', usecase='searchuser')

# search method used in multiple routes
def search_user(form, table):

    if form.validate_on_submit():
        user = table.query.filter_by(username=form.searchname.data).first()
        if user is not None:
            return True
        else:
            return False


@app.route('/admin/searchuser/student', methods=['GET', 'POST'])
def searchstudent():
    
    form = SearchStudentForm()
    if form.validate_on_submit():    
        if search_user(form, Student):
            flash("{} is found!".format(form.searchname.data))
        else:
            flash(" is not found!".format(form.searchname.data))

    return render_template('searchstudent.html', form=form)

@app.route('/admin/searchuser/teacher', methods=['GET', 'POST'])
def searchteacher():

    form = SearchTeacherForm()
    if form.validate_on_submit():    
        if search_user(form, Teacher):
            flash("{} is found!".format(form.searchname.data))
        else:
            flash(" is not found!".format(form.searchname.data))
    return render_template('searchteacher.html', form=form)

# Modify User Credentials
@app.route('/admin/modifyuser')
def modifyuser():
    return render_template('modifyuser.html', title='Modify User', usecase='modifyuser')

flag = True
@app.route('/admin/modifyuser/student', methods=['POST', 'GET'])
def modifystudent():
    global flag    
    flag = True
    form = SearchStudentForm()
    if form.validate_on_submit():    
        if search_user(form, Student):
            flash("{} is found!".format(form.searchname.data))
            return redirect(url_for('modifystudentdata', username=form.searchname.data))
        else:
            flash("{} is not found!".format(form.searchname.data))

    return render_template('modifystudent.html', form=form)

@app.route('/admin/modifyuser/student/modifystudentdata/<username>', methods=['GET', 'POST'])
def modifystudentdata(username):
    global flag
    form = AddStudentForm()
    user_std = Student.query.filter_by(username=username).first()
    if flag:    
        form.username.data = user_std.username
        form.program.data = user_std.program
        form.batch.data = user_std.batch
        form.email.data = user_std.email
        flag = False

    if form.validate_on_submit():
        user_std.username = form.username.data
        user_std.program = form.program.data
        user_std.batch = form.batch.data
        user_std.email = form.email.data
        db.session.commit()
        flag = True
        flash("data has been successfully modified")
        return redirect(url_for('modifystudent'))
    return render_template('modifystudentdata.html', form=form)

@app.route('/admin/modifyuser/teacher', methods=['GET', 'POST'])
def modifyteacher():
    global flag
    flag = True
    form = SearchTeacherForm()
    if form.validate_on_submit():    
        if search_user(form, Teacher):
            flash("{} is found!".format(form.searchname.data))
            return redirect(url_for('modifyteacherdata', username=form.searchname.data))
        else:
            flash("{} is not found!".format(form.searchname.data))
    return render_template('modifyteacher.html', form=form)

@app.route('/admin/modifyuser/student/modifyteacherdata/<username>', methods=['GET', 'POST'])
def modifyteacherdata(username):
    global flag
    form = AddTeacherForm()
    user_std = Teacher.query.filter_by(username=username).first()
    if flag:    
        form.username.data = user_std.username
        form.email.data = user_std.email
        flag = False

    if form.validate_on_submit():
        user_std.username = form.username.data
        user_std.email = form.email.data
        db.session.commit()
        flag = True
        flash("data has been successfully modified")
        return redirect(url_for('modifyteacher'))
    return render_template('modifyteacherdata.html', form=form)


# Create Time Table
@app.route('/admin/createtimetable', methods=['GET', 'POST'])
def createtimetable():
   
    form = CreateTimeTableForm()
    form.select_semester.choices = [('None', 'Select'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), 
            ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')]
    form.day.choices = [('None', 'Select'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')]
    form.timing.choices = [('None', 'Select'), ('class-1', '8:30am-10:00am'), ('class-2', '10:15am-11:45am'), ('class-3', '12:00pm-1:30pm'), ('class-4', '2:00pm-3:30pm')]

    return render_template('createtimetable.html', form=form, title='Create Time Table')

# called when a post request is send for the updation of table
@app.route('/updatetable', methods=['GET', 'POST'])
def updatetable():

    semester_obj = Semester.query.filter_by(semester_no=request.form['semester']).first() 
    if semester_obj:
        subject = Subject(subjectname=request.form['subject'], teachername=request.form['teacher'], day=request.form['day'],
                room=request.form['room'], timing=request.form['timing'], semester_name=semester_obj)
        db.session.add(subject)
        db.session.commit()
    else:
        semester_obj = Semester(semester_no=request.form['semester']) 
        subject = Subject(subjectname=request.form['subject'], teachername=request.form['teacher'], day=request.form['day'],
                room=request.form['room'], timing=request.form['timing'], semester_name=semester_obj)
        db.session.add(subject)
        db.session.commit()
    return ""


# View Time Table
@app.route('/admin/viewtimetable')
def viewtimetable():
    
    form = ViewTimeTableForm()

    semesters = Semester.query.order_by(Semester.semester_no.asc()).all()
    choices = [(semester.semester_no, semester.semester_no) for semester in semesters]
    form.select_semester.choices = [('None', 'Select')] + choices 

    return render_template('viewtimetable.html', form=form, title='View Time Table')

@app.route('/updateview', methods=['GET', 'POST'])
def updateview():

    semester = Semester.query.filter_by(semester_no=request.form['value']).first()
    data = []
    for subject in semester.subjects.all():
        data.append({"semester": "None", "subject": subject.subjectname, "teacher": subject.teachername, "day": subject.day, "room": subject.room, "timing": subject.timing}) 

    return jsonify(data)

@app.route('/admin/gettabledata', methods=['GET', 'POST'])
def gettabledata():
    return render_template('tabledata.html', form="")

# CreateProgram 
@app.route('/admin/createsemester')
def createsemester():
    form = CreateSemesterForm()     
    return render_template('createsemester.html', form=form)


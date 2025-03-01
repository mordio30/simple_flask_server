from flask import Flask

app = Flask(__name__)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

@app.route('/old_students/', methods=['GET'])
def old_students():
    old_students = []
    for student in students:
        if student['age'] >= 21:
            old_students.append(student)
    return old_students

@app.route('/advance_students/', methods=['GET'])
def advance_students():
    advance_students = []
    for student in students:
        if student['age'] <= 20 and student['grade'] == 'A':
            advance_students.append(student)
    return advance_students

@app.route('/student_names/', methods=['GET'])
def student_names():
    student_names = []
    for student in students:
        student_names.append({'first_name': student['first_name'], 'last_name': student['last_name']})
    return student_names

@app.route('/student_ages/', methods=['GET'])
def student_ages():
    student_ages = []
    for student in students:
        student_ages.append({'student_name': student['first_name'] +' '+ student['last_name'], 'Age': student['age']})
    return student_ages

@app.route('/students/', methods=['GET'])
def all_students():
    return students

app.run(debug=True, port = 8000)
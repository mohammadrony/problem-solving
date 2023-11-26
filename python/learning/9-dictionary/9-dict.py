student =	{
  "name": "Rony",
  "class": 7,
  "roll": 19
}
print(type(student)) 
print(len(student))
print(student)

student['serial'] = student.pop('roll')
print(student)
print(student.pop('serial'))
print(student)
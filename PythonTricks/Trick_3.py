#Checking for Truth conditions: (all & any)

score = 100
counter = 10
flag = True

student_list = [score > 90,
                counter < 5,
                flag == True
                ]

if all(student_list):                               #Checks if all the conditions are true....doing an 'AND' operation
    print("The student passed the exam!!!")
else:
    print("The student has failed the exam!!!")


if any(student_list):                               #Checks if any one condition is true....doing an 'OR' operation
    print("The student passed the exam!!!")
else:
    print("The student has failed the exam!!!")
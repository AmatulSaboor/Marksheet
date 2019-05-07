#taking input
fName = input(print("Enter your first name : "))
lName = input(print("Enter your last name : "))
Class = input(print("Enter your class and section : "))
Phy_marks = float(input(print("Enter the marks of Physics : ")))
Maths_marks = float(input(print("Enter the marks of Mathematics : ")))
Isl_marks = float(input(print("Enter the marks of Islamiat : ")))
Eng_marks = float(input(print("Enter the marks of English : ")))
Urdu_marks = float(input(print("Enter the marks of Urdu : ")))

#calculations
total_Marks = Phy_marks + Maths_marks + Urdu_marks + Isl_marks + Eng_marks
percentage = round((total_Marks/425)*100,2)

#grading
if percentage >= 80 :
    grade = 'A+'
elif percentage >= 70 :
    grade = 'A'
elif percentage >= 60 :
    grade = 'B'
elif percentage >= 50 :
    grade = 'C'
elif percentage >= 40 :
    grade = 'D'
elif percentage >= 33 :
    grade = 'E'
elif percentage <33 :
    grade = 'F'
else : 
    print("Hello")

#printing the marksheet
print("\n\n     ~~MARKSHEET~~\n")
print("Name  : ", fName,lName)
print("Class : ", Class)
print("\n   ~~Marks Of Individual Subjects~~\n")
print("Physics " + " | " + str(Phy_marks) + " out of 100")
print("Maths   " + " | " + str(Maths_marks) + " out of 100")
print("Islamiat" + " | " + str(Isl_marks) + " out of 75")
print("Urdu    " + " | " + str(Urdu_marks) + " out of 75")
print("English " + " | " + str(Eng_marks) + " out of 75")
print("\n   ~~Summary~~\n")
print("Total Marks = ", str(total_Marks))
print("Percentage  = ", str(percentage), "%")
print("Grade       = ", grade)

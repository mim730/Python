import datetime
myNow = datetime.datetime.now()
print(myNow)
myNum = 10
myText ="Hello"
print(myNum, myText)
x= 3
print(x)

x = 10
y = '10'
z = 10.5
sum1 = x+x
sum2 = y + y
print(type(x), type(y), type(z))

student_grades1 = [9.1, 8.8, 7.3]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.3}
E = list(range(1, 10))
print(E)
mySum1 = sum(student_grades1)
mySum = sum(student_grades.values())
length = len(student_grades)
mean = mySum/length
print(mean)
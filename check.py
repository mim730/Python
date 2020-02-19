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
monday_temp = (1,2,3)
print(monday_temp)


def mean1(value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

user_input = input("Enter value: ")
print(mean1(student_grades))



name = input("Enter your name: ")
surname = input("Enter your surname: ")
message = "Hello %s %s" % (name, surname)
message1 = f"Hello {name} {surname}"
print(message)
print(message1)


# For Loop over Dictionary
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1])) #for key, value and format(key, value)


phone_numbers1 = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers1.items():
    print("{}: {}".format(key, value))
    #print("%s: %s" % (key, value))



def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_in = input("Say Sometthing: ")
    if user_in=="\end":
        break
    else:
        results.append(sentence_maker(user_in))

print(" ".join(results))
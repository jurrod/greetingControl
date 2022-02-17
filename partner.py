
print("Hello all college students, prepare to answer some short questions")
name = input("Please enter your name ");
age = int(input("Now enter your age "));
school = input("One last step, enter the university that you currently attend ");

if (age == 18): 
    print("hi", name, "I hope your freshman year at", school, "is going splendidly!");

elif (age == 19):
    print("hi", name, "I hope your sophomore year at",  school, "is going splendidly!");

elif (age == 20):
    print("hi", name, "I hope your junior year at", school, "is going splendidly!");

else:
    print("hi", name, "Congrats!! Finish this year up at", school, "and you will be a college grad!");

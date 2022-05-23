print("Hello, World!")
str = 'Hello, Python!'
print(str)
print(str.lower())
print(str.upper())
print(str.title())

Name = input("What is your name?")
Goal = input("What is your goal?")
Time = input("When will you start working in a QA position?")
print(f"Hi user. Your name is {Name}. Your goal is {Goal}. "
      f"You will start working in a QA position {Time}.")

a = input("a:")
b = input("b:")
c = input("c:")
if a > b:
    print("so sad message")
elif b > a:
    if b > c:
        print("absolutely happy message")
    else:
        print("not so sad message")
elif a == b:
    print("something about equality")


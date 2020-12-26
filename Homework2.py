#Homework2
while True:
    first_name = input("First name: ")
    last_name = input("Last name : ")
    age = int(input("Age : "))
    birth = int(input("Date of birth(just year): "))
    person = [first_name.capitalize(),last_name.capitalize(),age,birth]
    if age !=(2020-birth):
        print("Please, enter correct value (age and year)!!!")
    else:
        for i in person:
            print(i)
        if age>=18:
            print("You can go out to the street")
        elif 0<=age<18:
            print("You can't go out because it's too dangerous")
        else:
            print("You entered an invalid age!!!")
        break

#Project 1
for i in range(0,3):
    name = input("Name   : ")
    surname = input("Surname: ")
    if name=="elif" and surname=="altınbulak":
        print(f"******Welcome,{name.capitalize()} {surname.capitalize()}******")
        while True:
            def average1(exam1,exam2,exam3):
                return (exam1*0.3)+(exam2*0.5)+(exam3*0.2)
            def average2(exam4,exam5,exam6,exam7):
                return (exam4*0.15)+(exam5*0.15)+(exam6*0.5)+(exam7*0.2) 
            def average3(exam8,exam9,exam10,exam11,exam12):
                return (exam8*0.1)+(exam9*0.1)+(exam10*0.1)+(exam11*0.5)+(exam12*0.2)
            def grade(average):
                if 90<=average<=100:
                    return "AA"
                elif 70<=average<90:
                    return "BB"
                elif 50<=average<70:
                    return "CC"
                elif 30<=average<50:
                    return "DD"
                elif 0<=average<30:
                    return "FF"
                else:
                    return "You entered an invalid grade!!!"
            c = int(input("Please, how many exams do you have from this course? (min=3),(max=5) : "))
            if c==3:
                exam1 = int(input("Midterm :"))
                exam2 = int(input("Final   :"))
                exam3 = int(input("Project :"))
                l3=[exam1,exam2,exam3]
                grade1={'Midterm':(exam1),
                'Final':(exam2),
                'Project':(exam3)}
                result1 = int(average1(exam1,exam2,exam3))
                print("-"*21)
                print("*******NOTES*******")
                print(f"{grade1}")
                print(f"Average : {result1}")
                print(f"Grade   : {grade(result1)}")
                print("-"*21)
                break
            elif c==4:
                exam4 = int(input("Midterm1 :"))
                exam5 = int(input("Midterm2 :"))
                exam6 = int(input("Final    :"))
                exam7 = int(input("Project  :"))
                l4=[exam4,exam5,exam6,exam7]
                grade2={'Midterm1':(exam4),
                        'Midterm2':(exam5),
                        'Final':(exam6),
                        'Project':(exam7)}
                result2 = int(average2(exam4,exam5,exam6,exam7))
                print("-"*21)
                print("*******NOTES*******")
                print(f"{grade2}")
                print(f"Average : {result2}")
                print(f"Grade   : {grade(result2)}")
                print("-"*21)
                break
            elif c==5:
                exam8 = int(input("Midterm1  :"))
                exam9 = int(input("Midterm2  :"))
                exam10 = int(input("Midterm3  :"))
                exam11 = int(input("Final     :"))
                exam12 = int(input("Project   :"))
                l5=[exam8,exam9,exam10,exam11,exam12]
                grade3={'Midterm1':(exam8),
                        'Midterm2':(exam9),
                        'Midterm3':(exam10),
                        'Final'   :(exam11),
                        'Project' :(exam12)}
                result3 = int(average3(exam8,exam9,exam10,exam11,exam12))
                print("-"*21)
                print("*******NOTES*******")
                print(f"{grade3}")
                print(f"Average : {result3}")
                print(f"Grade   : {grade(result3)}")
                print("-"*21)
                break
            elif c<3:
                print("You failed in class")
                break
            else:
                print("Please enter min=3 max=5 exams!!")
        break
    elif i ==2:
        print("Please try again later...")

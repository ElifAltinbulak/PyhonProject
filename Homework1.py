#Homework1
value1 = input("Value(String) : ")
value2 = int(input("Value(Int1): "))
value3 = float(input("Value(Float): "))
value4 = int(float(input("Value(Int or Float) :")))
value5 = float(int(input("Value(Int>>Float):")))
print(f"""
Value(String):{value1}, Type:{type(value1)}
Value(Int1)   :{value2}, Type:{type(value2)}
Value(Float) :{value3}, Type:{type(value3)}
Value(Int or Float):{value4}, Type:{type(value4)}
Value(Int>>Float):{value5}, Type:{type(value5)}""")

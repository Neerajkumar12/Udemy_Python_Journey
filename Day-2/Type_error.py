# TypeError , Checking and Conversion

# print(len(12345))   # it is given the typeError

#So we need to change in string
print(len("123456"))

#check the datatype of any data

#using type() funtion
print(type("hello"))
print(type(1223))
print(type(2.4))
print(type(True))

#Type Conversion or type Casting in Python
s="123"+"456"
print(type(s))
print(s)

i = int("123")+int(456)
print(type(i))
print(i)

# if you provide abc and change into number then it will get value error

#we can convert into these datatypes:
int()
float()
bool()
str()

print("Number of letters in your name: "+ str(len(input("enter your name"))))
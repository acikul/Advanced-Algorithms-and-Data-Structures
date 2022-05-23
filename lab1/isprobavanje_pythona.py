import random

x = "mislav"
p = 5

if random.randint(1, 10) > 2:
    print(type(x))
    print("p je tipa: " + type(p).__name__)
else:
    print("hello world!!!!!!!")

print("#########################")

fruits = ["apple", "banana", "cherry"]
b, y, z = fruits
# print(b)
# print(y)
# print(z)


print("#########################")


def myfunc():
    print(int(3.8))
    print("len je ", len("petar"))
    return "t" in "petar"


myfunc()
print(myfunc())


b = "Hello, World!"
print(b[-4:-1])
print(b.upper())
print(b.replace("H", "j").capitalize())
print(bool(b))


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["biba"]
print(thislist)

thislist.insert(2, "kika")
print(thislist)

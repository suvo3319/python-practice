print("Hello, World!")
# a = 5
# b = 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)

# a = 5
# b = 2

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# a = 20
# a+=2
# print(a)
# a+=2
# print(a)
# a-=2
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)
# a+=5
# a%=2
# print(a)
# a+=5
# a**=2
# print(a)

# print(True and False)
# print(True or False)
# print(not True)

# a = int(input("Enter First number: "))
# b = int(input("Enter Second number: "))
# print("The sum of",a,"and",b,"is",a+b)

# a = float(input("Enter side of a area:"))
# print("the area of the square is:",a**2)

# a = float(input("Enter First number: "))
# b = float(input("Enter Second number: "))
# print("The average f the two number is:",(a+b)/2)

# a = float(input("Enter First number: "))
# b = float(input("Enter Second number: "))
# print("Is a greater than b ",a>b)

# str1 = "hello"
# str2 = "World"
# str3 = str1 + " " + str2
# print(str3)
# print(len(str3))
# print(str3[0])
# print(str3[-1])
# print(str3[0:5])
# print(str3[:5])
# print(str3[6:])
# print(str3.endswith("ld"))
# print(str3.endswith("o"))
# print(str3.capitalize())
# print(str3)
# print(str2.replace("o","a"))
# print(str3.find("o"))
# print(str3.count("o"))

# str1 = input("Enter your String: ")
# print(str1)
# print(len(str1))
# print(str1.find("$"))

# grade = int(input("Enter your number: "))

# if(grade >= 90):
#     print("A")
# elif(grade >= 80):
#     print("B")
# elif(grade >= 75):
#     print("C")
# else:
#     print("D")

# num = int(input("Enter the number to check if it is odd or even: "))

# if(num % 2 == 0):
#     print("even")
# else:
#     print("odd")

# first = int(input("Enter your first number: "))
# second = int(input("Enter your second number: "))
# third = int(input("Enter your third number: "))

# if(first>third):
#     if(first>second):
#         print("first")
#     elif(second>third):
#         print("second")
# else:
#     print("third")

# num = int(input("Enter number to check: "))

# if(num%7 == 0):
#     print("divisable")
# else:
#     print("Not divisable")

# li = [1,2,3,4,5]
# print(len(li))
# print(li[1:])
# li.append(3.5)
# print(li)
# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)
# li.insert(2,"Ram")
# print(li)
# print(len(li))
# li.remove("Ram")
# print(li)
# li.pop(4)
# print(li)

# tup1 = (1)
# print(type(tup1))
# tup2 = (1,)
# print(type(tup2))
# tup = (12,11,17,11)
# print(tup[1:])
# print(tup.index(11))
# print(tup.count(11))

# list = []
# list.append(input("Enter your first name"))
# list.append(input("Enter your last name"))
# print(list)

# list = [1,"abc",3,"abc",1]
# list1 = list.copy()
# list1.reverse()
# if(list == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# set1 = {"a","b","c"}
# set2 = {"b","d","a","b"}

# set3 = set1 | set2
# set4 = set1 & set2
# set5 = set1 - set2
# set6 = set2 - set1
# print(set1)
# print(set2)
# print(set3)
# print(set4)
# print(set5)
# print(set6)
# print(f"is 'a' present in set1 ? {'e' in set1} ")

# dict1 = dict(key1="value1",key2="value2",key3=5)
# # print(dict1)
# dict2 = {}
# dict2["key1"] = "value1"
# dict2["key2"] = "value2"
# dict2["key3"] = 3
# print(dict2)

# print(f"value1 in dict {'value1' in dict2.values()}")

# dict3 = dict1 | dict2
# print(dict3)

# key4 = dict2.get("key4","no key")
# print(key4)

#ternary operator
# package_price = int(input("Enter the package amount:"))

# delivary_fee = 0 if package_price > 300 else 30

# print(f"The total charge for the package is: {package_price + delivary_fee}")

# seat_type = input("Enter your preffered seat type (general/seater/sleeper/ac):").lower()

# match seat_type:
#     case "general":
#         print("You will not have any personal seat")
#     case "seater":
#         print("You will get to seat down")
#     case "sleeper":
#         print("You will get a whole seat to sleep with food")
#     case "ac":
#         print("You will get ac coach with proper blanket & food")
#     case _:
#         print("User preference isn't availaible")

# Observation: The loop will run whichver list is small that many time only..

# orders = ["person 1","person 2","person 3","person 4"]
# bill_paid = [100,150,120]

# # for x in range(1,5):
# #     print(f"Your order number is {x}")

# # for names in orders:
# #     print(f"{names} orders food")

# # for idx,names in enumerate(orders,start=1):
# #     print(f"{names} is order no {idx}")

# # for name,index in zip(orders,bill_paid):
# #     print(f"{name} paid total ${index}")

# temparature = int(input("Enter the temperature of the water:"))

# while(temparature < 100):
#     print(f"temperature is {temparature} degree And water is yet to boiled")
#     temparature+=15
# print("Water is boiled..")

# # for-else loop

# staff = [("person 1",16),("person 2",13),("person 3",15)]

# for name,age in staff:
#     if(age>=18):
#         print(f"{name} is eligible to work")
#         break
# else:
#     print("No one is eligible to work")

# flavours = ["orange","mango","out of stock","lemon","discontinued","jeera"]

# for flavour in flavours:
#     if(flavour == "out of stock"):
#         continue
#     if(flavour == "discontinued"):
#         break
#     print(f"the flavour is {flavour}")
# print("end of the loop")

# walrus...

# flavours = ["orange","mango","lemon","jeera"]

# # user_input = input("Enter your desired flavour:").lower()

# # for flavour in flavours:
# #     if(flavour == user_input):
# #         print(f"{flavour} is available in our store")
# #         break
# # else:
# #     print(f"{user_input} flavour isn't availaible")

# #     #instead of doing this we can do : 



# if (user_input := input("Enter your desired flavour:").lower()) in flavours:
#     print(f"{user_input} is available in our store")
# else:
#     print(f"{user_input} flavour isn't availaible")

# dictionary ises

customers = [
    {"name":"Abhi","total":200,"cupon":"B20_40"},
    {"name":"Raj","total":230,"cupon":"F25"},
    {"name":"John","total":450,"cupon":"P50"},
]

discounts = {
    "P10":(0.1,0),
    "F25":(0,25),
    "P50":(0.5,0),
    "B20_40":(0.2,40)
}

for customer in customers:
    percent,fix = discounts.get(customer["cupon"],(0,0))
    discount = customer["total"] * percent + fix
    print(f"{customer["name"]} paid total {customer["total"]} rupees and get {discount} rupees discount on next order.")
    
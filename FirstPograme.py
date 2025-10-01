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

set1 = {"a","b","c"}
set2 = {"b","d","a","b"}

set3 = set1 | set2
set4 = set1 & set2
set5 = set1 - set2
set6 = set2 - set1
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(set6)
print("is 'a' present in set1 ?", {'e' in set1})


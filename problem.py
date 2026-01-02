#1 = To check that if a number is a positive or negative
# num=int(input("Enter the number:"))
# if num >0:
#     print("This is positive number")
# else:
#     print("this is a negative number")

#2 =Even or odd
# num=int(input("Enter the number:"))
# if num%2==0:
#     print("this is even number")
# else:
#     print("this is odd number")

#3= sum of N natural numbers
# num=int(input("Enter the number:"))
# sum=0
# for i in range(1,num+1):
#     sum=sum+i

# print(f"total={sum}")

#4 = sum of numbers in a given range
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# sum=0
# for i in range(num1,num2+1):
#     sum=sum+i

# print(f"total={sum}")

#5 = Greatest of two numbers
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# if num1 >num2:
#     print(f"{num1} is greater than {num2}")
# else:
#     print(f"{num2} is greater than {num1}")

#6 = greatest of three numbers
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))

# if num1> num2 and num1>num3:
#     print(f"{num1}is greater than{num2},{num3}")
# elif num2 >num1 and num2> num3:
#     print(f"{num2}is greater than{num1},{num3}")
# else:
#     print(f"{num3}is greater than{num1},{num2}")

#7 = leap or not
# year=int(input("Enter the Year:"))
# if(year%4==0 and year%100!=0):
#     print(f"{year} is a leap year")
# else:
#     print("it is not a leap year")

#8=prime number
# num=int(input("Enter the number:"))
# prime=True
# if num<2:
#      prime=True
# else:
#      for i in range(2,num):
#           if num%i==0:
#                prime=False
#                break
# if prime==True:
#      print("prime number")
# else:
#      print("not a prime number")


#9= prime numbers in a range
# num1=int(input("Enter the number:"))
# num2=int(input("Enter the number:"))
# display=[]
# for i in range(num1,num2):
#      num=i
#      prime=True
#      if num<2:
#           prime=True
#           display.append(num)
#      else:
#           for i in range(2,num):
#                if num%i==0:
#                     prime=False
#                     break
#      if prime==True:
#           display.append(num)
# print(display)

#10= sum of digits
# num=int(input("Enter the numbers:"))
# total=0
# while num>0:
#     digit=num%10
#     total+=digit
#     num//=10

# print(total)

#11=reverse a number
# num=int(input("Enter the numbers:"))
# rev=0
# while num>0:
#     digit=num%10
#     rev = rev * 10 + digit
#     num//=10

# print(rev)


#12=palindrome
# number=int(input("Enter the number:"))
# num=number
# rev=0
# while num>0:
#     last_digit=num%10
#     rev=rev*10+last_digit
#     num=num//10

# if number==rev:
#     print("It is a palidrome")
# else:
#     print("It is not a palindrome")

#13= Armstrong number
# number=int(input("Enter the number:"))
# num=number
# calculate the length of number without using len()or str()
# length = 0
# temp = num
# while temp > 0:
#     temp //= 10
#     length += 1
# finfing the armstrong
# armstrong=0
# while num>0:
#     last_digit=num%10
#     armstrong+=last_digit**length
#     num=num//10

# if armstrong==number:
#     print("it is armstrong number")
# else:
#     print("it is not a armstrong number")


#14=Armstrong numbers for a range
# num1=int(input("Enter the number:"))
# num2=int(input("Enter the number:"))
# display=[]
# for i in range(num1,num2):
#     looped_digit=i
#     num=looped_digit

#     #length
#     temp=num
#     length=0
#     while temp>0:
#         temp=temp//10
#         length+=1

#     #armstrong
#     armstrong=0
#     while num>0:
#         last_digit=num%10
#         armstrong+=last_digit**length
#         num=num//10

#     if armstrong==looped_digit:
#         display+=[looped_digit]

# print(display)

#15=fibonacci series upto the nth term
# num=int(input("enter the number:")) 

# f0,f1=0,1
# fibonacci =[]

# if num ==1:
#     fibonacci=[f0]
# elif num>=2:
#     fibonacci =[f0,f1]
#     for i in range(2,num):
#         f2=f0+f1
#         fibonacci+=[f2]
#         f0,f1=f1,f2

# print(fibonacci)

#16:find the nth term in fibonacci series
# num=int(input("enter the number:")) 

# f0,f1=0,1
# fibonacci =[]

# if num<1:
#     print(0)
# elif num==1:
#     print(f0)
# elif num>=2:
#     fibonacci =[f0,f1]
#     for i in range(2,num):
#         f2=f0+f1
#         fibonacci+=[f2]
#         f0,f1=f1,f2

#     print(fibonacci[-1])


#17:factorial of numbers
# num=int(input("Enter the number:"))
# fact=1
# for i in range(1,num+1):
#         fact*=i

# print(fact)

#18=power of a number
# num=int(input("Enter the number:"))

# last_digit=num%10
# num//=10
# num=num**last_digit

# print(num)

#19=factor of number
# num=int(input("Enter the number:"))

# for i in range(1,num+1):
#     for j in range(1,num+1):
#         if i*j==num:
#             print(i ,end=",")
#             break

                










    

    
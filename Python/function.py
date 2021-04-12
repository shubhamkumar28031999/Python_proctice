#fuctions practice
#def last_char(name):
 #   return name[-2]

#print(last_char("ABhishek"))
#def odd_even(num):
 #   if num%2==0:
  #      return "even"
   # else:
    #    return "odd"
#print(odd_even(10))    
#def odd_even(num):
#    if num%2==0:
#        return  "even"
 #   return "odd"  
#print(odd_even(11))  
#def is_even(num):
#    if num%2==0:
#      return True
#    return False 

#def is_even(num):
#    return num%2==0

#print(is_even(10))      
#def greater(num1,num2):
#    if num1>num2:
#        return num1
#    else:
#        return num2
#num1 = int(input("Enter the first number  "))
#num2 =  int(input("Enter the second number "))
#bigger  = greater(num1,num2)
#print(f"{bigger} is greater")
##def greater(a,b,c):
 #   if a>b and a>c:
  #      return a
   # elif b>a and b>c:
   #     return b
   # elif c>a and c>b:
    #    return c
   #3# return "ALL numbers are equal"    
#num1 = int(input('enter 1st number '))
#num2 = int(input('enter 2 nd nuber '))
#num3 = int(input('enetr third number '))
#bigger = greater(num1,num2,num3)
#print(f"{bigger}")
#def animal_crackers(text):
#    wordlist = text.split()
#    print(wordlist)

#    return wordlist[0][0] == wordlist[0][1]
#wordlist = input("enter words : ")
#print(animal_crackers(wordlist))

#def makes_twenty(n1,n2):
#    if n1+n2==20 or n1==20 or n2==20:
#        return True
#    else:
#        return False
#print(makes_twenty(20,20))

#def old_macdonald(name):
#    name = 'macdonald'
#    result =  name[0][3].upper()
    #
#vprint(old_macdonald(r


def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)


print(new_greatest(10,20,30)

#greater(a,b)  a or b 
#greater(a,b,c) ----> greatest
import random
import string
import secrets

length = int(input("Enter the length of password: "))

print("What is the complexity of the password you want: \n1. Upper and Lower case Only\n2. Upper, Lower case with digits \n3. Upper, Lower case with digits and punction marks \n")

choose = int(input("Your Choice: "))

charac1 = string.ascii_letters
charac2 = string.ascii_letters + string.digits
charac3 = string.ascii_letters + string.punctuation + string.digits


if choose == 1:
    password = "".join(secrets.choice(charac1)
                   
                   for x in range(length))

if choose == 2:
    password = "".join(secrets.choice(charac2)
                   
                   for x in range(length))


if choose == 3:
    password = "".join(secrets.choice(charac3)
                   
                   for x in range(length))



print("Your password is: ",password)

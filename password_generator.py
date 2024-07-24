import random
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'\
         ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums = ['0','1','2','3','4','5','6','7','8','9']
special_chars = ['!','@','#','$','%','^','&','*','(',')','~','/','<','>','?']
password_list=[]
alpha_len=int(input("Enter how many alphabets you want in the password\n"))
nums_len=int(input("Enter how many numbers you want in he password\n"))
special_Chars_len=int(input("Enter how many special characters you want in he password\n"))
for i in range(1,alpha_len+1):
    char=random.choice(alpha)
    password_list+=char
for i in range(1,nums_len+1):
    char=random.choice(nums)
    password_list+=char
for i in range(1,special_Chars_len+1):
    char=random.choice(special_chars)
    password_list+=char
password = random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(password)


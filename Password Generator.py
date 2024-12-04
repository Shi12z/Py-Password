import random
nbrs=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','^','%','*','-']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

PASSWORD=''
print('Welcome to Py Password Generator! ')
a=int(input('enter number of numbers you need'))
b=int(input('enter number of symbol you need'))
c=int(input('enter number of letters you need'))

for i in range(0,a):
    p=random.choice(nbrs)
    PASSWORD=PASSWORD+p

for j in range(0,b):
    p=random.choice(sym)
    PASSWORD+=p
    
for k in range(0,c):
    p=random.choice (letters)
    PASSWORD+=p
    
print(PASSWORD,'IS THE PERSONALIZED PASSWORD FOR YOU!')    
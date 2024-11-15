import random
n=random.randint(1,10)
a=-1
guess=1
while(a!=n):
    a=int(input("enter any number:"))
    if(a>n):
        print("lower number please" )
        guess+=1
    elif(a<n):
        print("higher number please")
        guess+=1
print(f"you have guessed the number {n} correctly in {guess} attempts")
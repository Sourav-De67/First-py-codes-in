import random
num=random.randint(1,11)
tries=0
while True:
    guess=int(input('Please guess your number :'))
    if num==guess:
        tries+=1
        print(f"You are write.You guess the in {tries} tries")
        break
    elif num<guess:
        print("A little lower ")
        tries+=1
    elif num>guess:
        print("A little higher")
        tries+=1
    else:
        tries+=1
        print("You are wrong")
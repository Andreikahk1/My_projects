import random
magic_num = random.randint(0, 9)
exit = False
while not exit:
    user_num = int(input("Try to guess the secret number: "))
    if user_num != magic_num:
        print("Ha ha! You're stuck in my loop!")
    else:
        print(magic_num,"Well done, muggle! You are free now")
        exit = True

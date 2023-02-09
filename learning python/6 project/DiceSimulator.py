import random
make_random_throw = True
while make_random_throw:
    makeIt = input('Do you want to start?: \nyes or no: ')
    if makeIt == 'yes': print(f"You got: \n\t\n| {random.randint(1,6)} |\n")
    else: break
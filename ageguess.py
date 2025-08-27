import random
def main():
    name = input("Hello! My program will try and guess your Age!\nWhat is your name?: ")
    age = random.randrange(18,31)
    response = input(f'Is your age {age}?[y/n]: ')
    while response != 'y':
        print('Rats...')
        age = random.randrange(15,31)
        response  = input(f'Is your age {age}?[y/n]: ')
    print(f'Your name is {name} and you are {response} years old!')
    return None

main()
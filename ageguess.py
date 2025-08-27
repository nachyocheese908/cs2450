import random
def main():
    name = input('Hello! My program will guess your age!\nWhat is your name?: ')
    ages = list(range(16,31))
    age = random.choice(ages)
    response = None
    while response != 'y':
        if len(ages) == 1:
            print(f'Your age must be {ages[0]}!\nYour name is {name} and you are {age} years old!')
            return None    
        response  = input(f'Is your age {age}?[y/n]: ')
        ages.remove(age)
        print('Rats...')
        age = random.choice(ages)
    print(f'Your name is {name} and you are {age} years old!')
    return None

main()
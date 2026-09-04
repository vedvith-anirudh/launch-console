print('Welcome to the Launch Console!')
name = input('What is your name?: ')
print(f'Hello, {name}!')
running = True
while running:
    print('1) About me')
    print('2) My goals')
    print('3) My hobbies')
    print('4) Exit')
    choice = input('Pick option 1-4: ')
    if choice == "1":
        print("I am a student who is currently in the 9th grade, and I am currently in the Elite 101 program in Code2College.")
    elif choice == "2":
        print('One of my goals is to get into MIT for my undergrad and for graduate school. For this year, on the other hand, my goal is to get an internship with the Code2College program.')
    elif choice == "3":
        print('My hobbies include: reading books, watching tv, playing videogames, and doing robotics/coding as I find all of these things very interesting. I also enjoy playing basketball.')
    elif choice == "4":
        print(f'Goodbye, {name}!')
        running = False
    else:
        print(f'That was not a listed option, {name}. Please input a valid choice.')
            
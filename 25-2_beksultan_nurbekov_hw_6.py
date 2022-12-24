import re


def colors():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        color = file.read()
        ls = re.findall(r'#.{6}', color)

        # for i in ls:
        #         print(f'{i}')
        print(f'objects in the list: {len(ls)}')

    with open('colors.txt', 'w') as file:
        file.write(f'objects in the list: {len(ls)}\n{ls}')

def emails():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        email = file.read()
        ls = re.findall(r'[a-z0-9]*@[a-z0-9]*.[a-z]+', email)

        # for i in ls:
        #         print(f'{i}')
        print(f'objects in the list: {len(ls)}')

    with open('emails.txt', 'w') as file:
        file.write(f'objects in the list: {len(ls)}\n{ls}')

def names_surnemes():
    with open('MOCK_DATA.txt', 'r', encoding='utf-8') as file:
        name_surname = file.read()
        ls = re.findall(r"[A-Z][a-z-' A-Z]+\.?\s[A-Za-z-']+\.?\s", name_surname)

        # for i in ls:
        #     print(f'{i}')
        print(f'objects in the list: {len(ls)}\n{ls}')

    with open('names.txt', 'w') as file:
        file.write(f'objects in the list: {len(ls)}\n{ls}')


def file_names():

    with open("MOCK_DATA.txt", 'r') as file:
        file_name = file.read()
        ls = re.findall(r'[A-Z][a-zA-Z]*\.[a-z0-9]+', file_name)

        # for i in ls:
        #         print(f'{i}')
        print(f'objects in the list: {len(ls)}')

    with open('files.txt', 'w') as file:
        file.write(f'objects in the list: {len(ls)}\n{ls}')

while True:
    try:
        action = int(input('enter 1 - Count first and last names\nenter 2 - Count all emails\nenter 3 - Read file names'
                           '\nenter 4 - Count colors\nenter 5 - Exit\n'))
        if action == 1:
            names_surnemes()
        elif action == 2:
            emails()
        elif action == 3:
            file_names()
        elif action == 4:
            colors()
        elif action == 5:
            break

    except:
        continue

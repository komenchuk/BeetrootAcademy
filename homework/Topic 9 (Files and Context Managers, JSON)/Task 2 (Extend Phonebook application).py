"""Extend Phonebook application
Functionality of Phonebook application:
The first argument to the application should be the name of the phonebook.
Application should load JSON data, if it is present in the folder with application, else raise an error.
After the user exits, all data should be saved to loaded JSON."""

import os
import json

# Enter a file name and check it
while True:
    name_file = input('Enter the name of the phone book: ')
    try:
        if name_file == '':
            name_file = 'phonebook.txt'
        elif name_file[-8:] != '.txt':
            name_file += '.txt'
        with open(name_file) as File:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'File started {name_file}!')
            break
    except IOError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'File {name_file} not found!')

# Create a dictionary if the file exists
with open(name_file) as File:
    try:
        phonebook = json.load(File)
    except ValueError:
        print('Create a new list!')
        phonebook = []

values = {
    'first_name': 'First name',
    'last_name': 'Last name',
    'tel_number': 'Telephone number',
    'region': 'Region',
    'city': 'City'
}


# Add contacts
def add_item(phonebook):
    first_name = input('Enter your name: ')
    first_name = first_name.strip().title()

    last_name = input('Enter your surname: ')
    last_name = last_name.strip().title()

    while True:
        tel_number = input('Enter your telephone number: ')
        if not tel_number.strip().isnumeric():
            print('Error! The entered number must contain only numbers!')
            continue
        elif len(tel_number.strip()) > 10:
            print('Error! Enter a 10-digit number, starting at 0!')
            continue
        tel_number = tel_number.strip()
        break

    region = input('Enter your region: ')
    region = region.strip().title()

    city = input('Enter your city: ')
    city = city.strip().title()

    # Add entries to phonebook
    phonebook.append({
        'first_name': first_name,
        'last_name': last_name,
        'tel_number': tel_number,
        'region': region,
        'city': city
    })

    with open(name_file, 'w') as File:
        json.dump(phonebook, File)
    print(f'Subscriber successfully added!')


# Search contacts
def search_value(value, phonebook=phonebook):
    text_value = values[value]
    found_ind = []
    print(f'Search by value "{text_value}".')
    print(f'Enter {text_value}: ')
    search_input = input().strip()
    search_results = []
    if value == 'city':
        for i in range(len(phonebook)):
            if (
                    phonebook[i]['city'].lower() == search_input.lower()
                    or phonebook[i]['region'].lower() == search_input.lower()
            ):
                search_results.append(phonebook[i])
                found_ind.append(i)
    else:
        for i in range(len(phonebook)):
            if phonebook[i][value].lower() == search_input.lower():
                search_results.append(phonebook[i])
                found_ind.append(i)
    sr = search_results
    si = search_input
    print(f'Your search returned records {len(sr)} that include {si}.')
    print_item(search_results)
    return found_ind


# Search UI
def search(phonebook):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Search by name "f"
    Search by surname "l"
    Search by telephone number "n"
    Search by region "r"
    Search by city "c"
    Back to menu "e"
    """)
    while True:
        user_input = input(': ')
        if user_input == 'f':
            search_value('first_name')
        elif user_input == 'l':
            search_value('last_name')
        elif user_input == 'n':
            search_value('tel_number')
        elif user_input == 'r':
            search_value('region')
        elif user_input == 'c':
            search_value('city')
        elif user_input == 'e':
            finish()


def print_item(elem):
    for v in values.values():
        print(f'\x1b[1m{v:<15}\x1b[0m', end='')
    print()
    if isinstance(elem, dict):
        for v1 in elem.values():
            print(f'{v1:<15}', end='')
    elif isinstance(elem, list):
        for i in elem:
            for v1 in i.values():
                print(f'{v1:<15}', end='')
            print()


# Finish menu
def finish():
    y_n = 'n'
    while y_n == 'n':
        print('Turn to the menu?')
        s = 'y/n'
        y_n = input(f'\x1b[5;31;40m{s}:\x1b[0m')
        if y_n.strip().lower() == 'y':
            user_menu()
        else:
            y_n = 'n'


# Delete contact
def delete_by_tel_number(phonebook):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Search that record by phone number.')
    found = search_value('tel_number', phonebook=phonebook)
    print('Can you see the record?')
    y_n = input('y/n:')
    if y_n.strip().lower() == 'y':
        ind = found[0]
        first_name = phonebook[ind]['first_name']
        last_name = phonebook[ind]['last_name']
        print(f'The note on the person is seen from the book.')
        phonebook.remove(phonebook[ind])
        with open(name_file, 'w') as f:
            json.dump(phonebook, f)
    finish()


# Update contact
def update_by_tel_number(phonebook):
    ind = search_value('tel_number')
    item_update = phonebook[ind[0]]
    for key, value in item_update.items():
        print(f'Significance "{values[key]}, or press "Enter"')
        s = value
        readline.set_startup_hook(lambda: readline.insert_text(s))
        s = (input(': '))
        item_update[key] = s
    s = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Edited entry:')
    print_item(item_update)
    phonebook[ind[0]] = item_update
    with open(name_file, 'w') as f:
        json.dump(phonebook, f)
    finish()


# UI menu
def user_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Add Record - Press "a"
    Search - Press "s"
    Delete - "r"
    Edit Entry - Press "c"
    Shut Down - Click "q"
    """)
    while True:
        user_input = input(': ')
        if user_input == 'a':
            add_item(phonebook)
        elif user_input == 's':
            search(phonebook)
        elif user_input == 'r':
            delete_by_tel_number(phonebook)
        elif user_input == 'c':
            update_by_tel_number(phonebook)
        elif user_input == 'q':
            quit()


user_menu()

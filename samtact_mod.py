
# Phonebook project
import os
from collections import namedtuple


contacts = []

Contact =namedtuple('Contact', ('name', 'phone_number', 'birth_year', 'city', 'email'))



def load():
    if os.path.isfile('samtact.csv'):
        with open('samtact.csv', 'r') as sam_file:
            for line in sam_file:
                n, p, b, c, e= line[:-1].split(',')
                contact = Contact(n, p, b, c, e)
                contacts.append(contact)
        if len(contacts) > 0:
            contacts.pop(0)


def add_contact():
    global option_list
    option_list = input('\n' '\N{fleur-de-lis}' ' Welcome to Samtact!\n\N{memo} Samtact will help you to simply organize and reach your contact info.\nPlease choose one of the following options:\n'+'-' * 44 +
                   ' \n1. Add a new contact \N{bust in silhouette} \N{mobile phone} \n2. See the list of all contacts \N{memo} \n3. Search\N{left-pointing magnifying glass}\n0. Exit \N{cross mark}\n\n''\N{fleur-de-lis} Enter the option you seek: ')
    
    print('-' * 44)

    while option_list != '0':
        if option_list == '1':
            full_name = input(
                '\N{bust in silhouette} Please enter the contact fullname,to add to the contact list:\n')
            phone_number = input(
                '\n\N{mobile phone} Please enter the contact phone number, to add to the contact list:\n')
            birth_year = input(
                '\n\N{calendar} Please enter the contact birth year, to add to the contact list:\n')
            city = input(
                '\n\N{cityscape} Please enter the contact city of birth, to add to the contact list:\n')
            email = input(
                '\n\N{envelope} Please enter the contact city of birth, to add to the contact list:\n')            
            contact = Contact(full_name, phone_number, birth_year, city, email)
            contacts.append(contact)
        elif option_list == '2':
            print('\n\N{memo} Contact list:\n', contacts)
        elif option_list == '3':
            name = input(
                '\n\N{left-pointing magnifying glass} Enter a contact fullname to search for the phone number:\n\N{bust in silhouette}  ')
            print('\n\N{mobile phone}', name, 'phone number: ')

            for contact in contacts:
                if contact[0] == name:
                    print(contact[1])
                    break
            else:
                print(name, ', does not exist in the contact list!')
        option_list = input('\n' '\N{fleur-de-lis}' ' Please choose one of the following options:\n'+'-' * 44 +
                        '\n1. Add a new contact \N{bust in silhouette} \N{mobile phone} \n2. See the list of all contacts \N{memo} \n3. Search\N{left-pointing magnifying glass}\n0. Exit \N{cross mark}\n\n''\N{fleur-de-lis} Enter the option you seek: ')
print('saving...')



def save():
    with open('samtact.csv', 'w') as sam_file:
        sam_file.write('Name,Phone Number, Birth year, City, Email\n')
        for contact in contacts:
            sam_file.write(f'{contact.name},{contact.phone_number}, {contact.birth_year}, {contact.city}, {contact.email}\n')




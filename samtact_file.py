
# Phonebook project
import os
contacts = []

if os.path.isfile('samtact.csv'):
    with open('samtact.csv', 'r') as samFile:
        for line in samFile:
            line = line[:-1]
            contact = line.split(',')
            contacts.append(contact)
contacts.pop(0)


optionList = input('\n' '\N{fleur-de-lis}' ' Welcome to Samtact!\n\N{memo} Samtact will help you to simply organize and reach your contact info.\nPlease choose one of the following options:\n'+'-' * 44 +
                   ' \n1. Add a new contact \N{bust in silhouette} \N{mobile phone} \n2. See the list of all contacts \N{memo} \n3. Search\N{left-pointing magnifying glass}\n0. Exit \N{cross mark}\n\n''\N{fleur-de-lis} Enter the option you seek: ')
print('-' * 44)
while optionList != '0':
    if optionList == '1':
        fullName = input(
            '\N{bust in silhouette} Please enter the contact fullname to add to the contact list:\n')
        phoneNumber = input(
            '\n\N{mobile phone} Please enter the contact phone number to add to the contact list:\n')
        contact = [fullName, phoneNumber]
        contacts.append(contact)
    elif optionList == '2':
        print('\n\N{memo} Contact list:\n', contacts)
    elif optionList == '3':
        name = input(
            '\n\N{left-pointing magnifying glass} Enter a contact fullname to search for the phone number:\n\N{bust in silhouette}  ')
        print('\n\N{mobile phone}', name, 'phone number: ')

        for contact in contacts:
            if contact[0] == name:
                print(contact[1])
                break
            else:
                print(name, ', does not exist in the contact list!')
    optionList = input('\n' '\N{fleur-de-lis}' ' Please choose one of the following options:\n'+'-' * 44 +
                       '\n1. Add a new contact \N{bust in silhouette} \N{mobile phone} \n2. See the list of all contacts \N{memo} \n3. Search\N{left-pointing magnifying glass}\n0. Exit \N{cross mark}\n\n''\N{fleur-de-lis} Enter the option you seek: ')
print('saving...')

samFile = open('samtact.csv', 'w')
samFile.write('Name,Phone,city, Birth year \n')
for contact in contacts:
    samFile.write(contact[0] + ',' + contact[1] + '\n')

samFile.close()

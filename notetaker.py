#!/usr/bin/python
from sys import exit

def printList():
    f = open('todo.txt', 'r')
    print f.read()

def appendToList():
    f = open('todo.txt','a')
    f.write(raw_input("Add a to-do item: ") + "\n")

def deleteItem():
    f = open('todo.txt','r')
    lines = f.readlines()
    f.close()

    f = open('todo.txt','w')
    
    item = raw_input("Write the line you wish to delete: ")

    for line in lines:
        if line!= item  + "\n":
            f.write(line)
    f.close()

def main():
    
    choice_valid = True
    while True:

        print '''
            ____Menu____
            1. View List
            2. Add Item
            3. Delete Item
            4. Exit"
        '''

        if not choice_valid:
            
            print 'Invalid choice.'
            choice_valid = True

        option = raw_input("Type the number of your option: ")
        
        if option == "1":
            printList()
        elif option == "2":
            appendToList()
        elif option == "3":
            deleteItem()
        elif option == '4':
            return 
        else:
            choice_valid = False

if __name__ == '__main__':
    main()


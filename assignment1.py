#Inaya Rajwani - 501037903
#Problem: When making a grocery list, people can be unsure of what they want and sometimes get carried adding and removing items and might forget what is there.
#Solution: This program enables the user to make a list, look for an item and decide if they want it or not.

#This function tells the user to make a list and add items to the list after reviewing it, if they wish:
def grocery():
    user = input('Make a list of everything you want to add to your grocery list'
                 ' (include a space between each item and connect items that have two words'
                 ' (such as beef hotdog) with a dash (like this: beef-hotdog): ')
    list = ''
    list += user #creation of list
    print('Here is your current list: ' + user)
    more_grocery = input('You want to add more items now? Type either yes or no: ')
    if more_grocery.lower() == 'yes':  #adding items
        add = input('Add the items you want: ')
        list = list + ' ' + add
        print('Here is your list:', list)
    else:
        print('Here is your list: ', list) #if they opted out of adding items, prints original list
    return list

#This function allows the user to remove items they don't want
def less_grocery(list):
    less = input('Would you like to review your list to remove any items? Type either yes or no: ')
    if less.lower() == 'yes': #If the user wants to review their list, this program enables them to look through it and see what to remove
        print('Here is your current grocery list: ',list)
        choose = input('Would you like to remove any items? Type either yes or no: ')
        if choose == 'yes': #If they choose to remove something, the for loop within this if statement, takes in their input(stored in variable yes)
                            #and goes through the list to look for that item
            yes = input('If you would like to remove any item(s), which one(s)?(remember to add space between each item) ')
            list = list.replace(yes, "") #Once the item is found, it is removed from the list
            print('This is your list now: ' + str(list)) #The new list is printed

        elif choose == 'no': #If they choose not to remove anything, this program gives them one more check to ensure that they don't want to remove anything
            no_option = input('If you don\'t want to remove any items, type 1: ') #If they do decide that they really don't want to remove anything, they type 1 and the list is printed
            if no_option:
                print('You chose not to remove anything. Here is your list:', list)
            else: #If they do indeed decide they want to remove something, this program allows them to choose the item
                check1 = input('If you are not happy with this list and you would like to remove any item(s), which one(s)?')
                if check1 == '': #If they accidentally didn't type 1 or they change their mind once again, the list is printed
                    print(list)
                else:
                    list = list.replace(check1, "") #If they did input an item, the program goes through the list they created and removes said item
                    list_items = list.split()
                    print('This is your list now: ',)
                    for item in list_items:
                        print(item) #the list is printed
    else: #if they decide they don't want to remove anything from the start and they are happy with their list, the list is printed
        print('Here is your list: ', list)
    return list

#This program allows the user to look for something specific in their list
def find_grocery():
    list = grocery()
    search = input('Is there a specific item you\'re looking for? Type \'yes\' or \'no\': ') #Here is where the user is given the option to search specifically
    if search.lower() == 'yes':
        look = input('What are you looking for? ') #The user inputs the item they want
        if (look in list) == True:
            there = (input('It is already in your list. Would you like to keep it? Type yes or no: ')) #This alerts the user that they already have the item and they can choose if they want it keep it or remove it
            if there.lower() == 'yes':
                print('This is your list: ', list)
            else:
              less_grocery(list) #This takes the user through the program of removing an item

        else:
            not_there = input('It is not yet in your list. Would you like to add it? Type yes or no: ') #If the item the user is looking for is not already on the list, this enables the user to add it
            if not_there.lower() == 'yes':
                list += look
                print('This is your list: ', list)
            else:
                print('This is your list: ', list)
    else:
        print('Here is your list: ', list)
print(find_grocery())





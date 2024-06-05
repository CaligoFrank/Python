# A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc.
# Write a program that first takes in word pairs that consist of a name and a phone number (both strings), separated by a comma. 
#That list is followed by a name, and your program should output the phone number associated with that name. Assume the search name is always in the list.

# Ex: If the input is:

# Joe,123-5432 Linda,983-4123 Frank,867-5309
# Frank
# the output is:

# 867-5309


user_input = input()

#now split it as the seperator is a space 

pairs = user_input.split(' ')

phone_book = {}

for pair in pairs:
    name, number = pair.split(',')
    phone_book[name] = number

name_to_find = input()

print(phone_book[name_to_find])





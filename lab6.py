# Write a program that gets a list of integers from input, and outputs negative integers in descending order (highest to lowest).

# Ex: If the input is:

# 10 -7 4 -39 -6 12 -2
# the output is:

# -2 -6 -7 -39 
# For coding simplicity, follow every output value by a space. Do not end with newline.


user_input = input()

#Split the input

string_nums = user_input.split()

#now do list comprehension to convert every item to an int

lst_nums = [int(nums) for nums in string_nums]
neg_nums_unordered = []
#This for loop checks every item and puts any negative nums into a neg arr

for num in lst_nums:
    if num < 0:
        neg_nums_unordered.append(num)


#now sort the list of neg nums

srted_neg_nums = sorted(neg_nums_unordered,reverse=True)

#Convert the list to a string and output it
result_string = ' '.join([str(num) for num in srted_neg_nums])
print(result_string)
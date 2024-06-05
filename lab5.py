# Given a sorted list of integers, output "Middle item: " followed by the middle integer. Assume the number of integers is always odd.

# Ex: If the input is:

# 2 3 4 8 11
# the output is:

# Middle item: 4



user_input = input()

#Now we need to convert the string input to an array
arr_string_nums = user_input.split()


    
#Now do list comprehension to convert every element to an integer two ways to do this

#arr_nums = [int(nums) for nums in arr_string_nums]

#OR

arr_nums = []
for num in arr_string_nums:
    arr_nums.append(int(num))


#Now make a variable to hold the middle index make sure to floor divide as it can only be an int

middle_index = len(arr_nums) // 2

if len(arr_nums) <= 9:
    print(f"Middle item: {arr_nums[middle_index]}")
else:
    print("Too many inputs")





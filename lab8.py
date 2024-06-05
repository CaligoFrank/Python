# Write a program that finds word differences between two sentences. The input begins with the first sentence and the following input line is the second sentence.
# Assume that the two sentences have the same number of words.

# The program displays word pairs that differ between the two sentences. One pair is displayed per line.

# Ex: If the input is:

# Smaller cars get better gas mileage
# Tiny cars get great fuel economy
# then the output is:

# Smaller Tiny
# better great
# gas fuel
# mileage economy
# Hint: Store each input line into a list of strings.


phrase1 = input()
phrase2 = input()

#convert the phrases into lists of strings
phrase1_list = phrase1.split()
phrase2_list = phrase2.split()



different_words1 = [word for word in phrase1_list if word not in phrase2_list]
different_wrods2 = [word for word in phrase2_list if word not in phrase1_list]

for i in range(len(different_words1)):
    print(f"{different_words1[i]} {different_wrods2[i]}")



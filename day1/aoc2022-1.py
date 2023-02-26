#Opens AOC Day 1 data file, and stores it into a list named data
my_file = open('./day1/aoc2022-1data.txt', "r") 
data = my_file.readlines()
my_file.close()

#Initializes two empty lists to store out final products
temp_list = []
final_list = []

#Loops through out data lists, appending values into the temp_list
#If the data list contains a '\n', we sum the temp_list and then appends that to the final_list
#Repeats this until the whole data list is empty
for d in data: 
    if d == '\n':
        final_list.append(sum(temp_list))
        temp_list = []
    else:
        temp_list.append(int(d))
print(max(final_list)) #uses the max function to find the biggest value possible in the final_list

#Starts up an empty variable named big_three, to help find the sum of the top 3 numbers in the final_list
#Loops through the final_list, adding the biggest value to big_three and then removing it from the final_list
big_three = 0
for i in range(3):
    big_three += max(final_list)
    final_list.remove(max(final_list))
print (big_three)
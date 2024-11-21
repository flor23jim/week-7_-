

################################################List comprehension###############################################
#list comprehension= A concise way to create listis in python 

#compact and easier to read than traditional loops
#[expression for value in iterable if condition]

# doubles=[]
# for x in range(1,11):
#     doubles.append(x*2) # this will cause that all the number that are in the list get doubled/ times 2 
# print(doubles)

# doubles=[x*2 for x in range(1,11)] # this would make everything we did above much simplier- put the action first than what is getting to get affected
# print(doubles)

# triples=[y*3 for y in range (1,11)]
# squares=[z*z for z in range(1,11)]
# print(squares)

# fruits=['apples','oranges','banana','coconut']
# fruits=[fruit.upper() for fruit in fruits]
# print(fruits)
#another way could be::
# fruits=[fruit.upper() for fruit in ['apples','oranges','banana','coconut']]
# print(fruits)

# fruits=['apples','oranges','banana','coconut']
# fruit_chars=[fruit[0] for fruit in fruits] # the [0] makes the output be the first letter of each word in the list 
# print(fruit_chars)

# numbers=[1,-2,3,-4,5,-6]
# postive_nums=[ num for num in numbers if num>=0] # thid would print all of th enumbers hat are postive in the list
# print(postive_nums)


# numbers=[1,-2,3,-4,5,-6, 8,-7]
# # negative_nums=[ num for num in numbers if num<0] # thid would print all of th enumbers hat are negative in the list
# # print(negative_nums)

# even_nums=[ num for num in numbers if num % 2==0] # this will print out all the even numbers that are in the list
# print(even_nums)

# odd_nums=[ num for num in numbers if num % 2==1] # this will print out all the odd numbers that are in the list
# print(odd_nums)

# grades=[85,42,79,90,56,61,30]
# passing_grades= [ grade for grade in grades if grade>=60] #every grade that is above 60 will be printed out for the output
# print(passing_grades)

#PRACTICE WORKSHEET 

#1
# numbers=[3,7,10,15,21]
# doubles=[x*2 for x in numbers]
# print(doubles)

#2
# values=[8,11,20,25,32,47,55]
# odd=[x for x in values if x %2 ==1]
# print(odd)

#3
# words=['apple','banana','cherry','date']
# length=[ len(words) for words in words]
# print(length)

#4
# nums=[4,5,6,7,8,9,10]
# squared_e=[x**2 for x in nums if x % 2==0]
# print(squared_e)

#5
# names=['Alice','Bob','Amanda','Charlie','Anna',"David"]
# start_a=[x for x in names if x[0]=='A']
# print(start_a)

#6
# sentence=['hello','world','python','is','great']
# upper=[x.upper() for x in sentence]
# print(upper)



# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]
# squared_e=[value**2 for value in values if value % 2==0]
# print(squared_e)



# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

#values = [1, 2, 3, 4, 5, 6, 9.5]
# valueseven=[ value for value in values if value%2==0]
# print(valueseven)


# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius





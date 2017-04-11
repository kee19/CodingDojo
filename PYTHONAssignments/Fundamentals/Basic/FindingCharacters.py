# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# input
l = ['hello','world','my','name','is','Lolly']
char = 'o'
n = []


for i in l:
    for index in range(0, len(i)):
        if i [index]==char:
            n.append(i)

print n
            


# output
# n = ['hello','world']




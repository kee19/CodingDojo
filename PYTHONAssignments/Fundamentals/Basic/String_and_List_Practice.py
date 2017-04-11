#Find and Replace
str= "It's Thanksgiving day.It's my Birthday,too!"
print str.find("day")
print str.replace("day", "month")

# Min and Max
x = [2,6,10,-5,15,25]
print min(x)
print max(x)

# First and Last
x = ["Hi",2,6,10,-5,15,25,"Bye"]
print x
print x[0], x[len(x)-1]
y = [x[0],x[len(x)-1]]
print y
 

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print(x)
       
x.sort()

print x

first_list = x[0:len(x)/2]
second_list = x[len(x)/2:len(x)]

print "first_list", first_list
print "second_list", second_list

second_list.insert(0,first_list)
print second_list


 





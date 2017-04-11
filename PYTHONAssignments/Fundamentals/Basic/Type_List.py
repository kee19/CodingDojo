# l = [2, 4, 6, 10, 14, 18]
# l = ["The Originals","then","underworld"]
l = ["The Originals",19,"then",20.17,"underworld"]
sum = 0
strNew = ""
listnew = []
typeoflist = ""
for i in l:
    if isinstance(i, (int,float)):
        sum=sum+i
        typeoflist = "integer"

    elif sum!=0:
        typeoflist = "mixed"
        strNew +=i + ""
        continue

    else: #isinstance(i, str):
        strNew +=i + ""
        typeoflist = "string"


print "The array you entered is of",typeoflist, "type"
if typeoflist == "integer" or typeoflist == "mixed":
    print "Sum:", sum
if typeoflist == "string" or typeoflist == "mixed":
    print "String", strNew

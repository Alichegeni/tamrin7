mydict = {}
list_empty = []

myfile = open("tarjoomeh.txt","r")
data = myfile.read().split("\n")
for i in range (0,(len(data)),2):
    mydict["english"] = data[0]
    mydict["farsi"] = data[1]
    list_empty.append(mydict)
print(list_empty)
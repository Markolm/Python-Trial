user = input("What is your user folder? ")
text = input("What file on your desktop do you want to open? ")
txt = open("C:/Users/"+user+"/Desktop/"+text, "r")
fst = []
global fst
read = ""
while read != " ":
    read = txt.read(1)
    fst.append(read)
fst = "".join(fst)
print(fst)

file = open("newfile","w")
file.write("This is the New file")

fileappend = open("newfile","a")
file.write(" and writing more data using append.")

fileread = open("newfile","r")
data = fileread.read()
print(data)

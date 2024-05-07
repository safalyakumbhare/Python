f = open("copy.txt", "r")
data = f.read()

f = open("paste.txt", "w")
f.write(data)
# f.close()

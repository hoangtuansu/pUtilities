file = open("data.txt", "w")
file.write("Hello World")
file.close()

#write an array to a file
a = [1,2,3]
file = open("data.txt", "w")
for i in a:
    file.write(str(i) + ' ')
file.close()


from asyncore import read


# fhandle = open("myfile1.txt","r")
# content = fhandle.readlines()
# print(content)
# fhandle.close()

# wFile = open("writeFile.txt","w")
# message = "6,7,8,9,10"
# message2 = "$$$$$$$$$$$$$$$$$$$$$"

# wFile.write(message)
# wFile.close()


rfile = open("myfile11.txt","r")
content1 = rfile.readline()
content2 = rfile.readline()
rfile.close()

wfile = open("file2.txt","w")
wfile.write(content1+content2)
wfile.close()

rfile2 = open("file2.txt","r")
newText = rfile2.read()
print(newText)

rfile2.close()










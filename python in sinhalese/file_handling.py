''' 
open() - open a file descriptor
'r'   - read only(default)
'w'   - if the file exists it will create a new file & write
'x'   - if the file exists it will give an error
'a'   - concatanate a string
'''

file = open(file="movies.txt") # default mode - 'r'
# content = file.read(5)

for i,line in enumerate(file):
    print(f"Line {i+1} -> {line}")
# while True:
#     contents = file.readline()
#     if not contents:
#         break
#     print(contents)

file.close()

# write to a file
w_file = open("new_movies.txt","w")
# w_file = open("new_movies.txt","a")
# w_file = open("new_movies.txt","x")
# w_file.write("Luther")
w_file.write("\nPathaan\n")

# for i in range(1,11):    
#     w_file.write(str(i))

x = [str(i) for i in range(1,11)]
msg = ', '.join(x)
w_file.write(msg)
w_file.close()


# context managers - no need to close the file in this way
with open("new_movies.txt","a") as write_file:
    text = "\n196/8"
    write_file.write(text)



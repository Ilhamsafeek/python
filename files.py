file=open("myfile.txt","w")
file.write("\n")
file.write("3. this is third")
file.close()

file=open("myfile.txt","r")
print(file.read())



# r-read
# a-append
# w-write
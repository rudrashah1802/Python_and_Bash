file=open("student_data.txt","w+")
write=file.write("Hello World")
if(write):
    print("Data Written Successfully")
else:
    print("Data Not Written")
file.seek(0)
print(file.read())
file.close()
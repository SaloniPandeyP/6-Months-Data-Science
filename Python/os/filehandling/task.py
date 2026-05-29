import os
First_name= input("Enter  your first name: ")
Last_name = input("Enter your last name: ")
Address= input("Enter your addresss: ")
Gender=input("Enter your Gender: ")
DOB = input("enter your DOB: ")
# create a folder
folder_name = First_name
if not os.path.exists(folder_name):
    os.mkdir(folder_name)



a=os.getcwd()
print("Current Path:", a)

file = open(f"{folder_name}/record.txt", "w")
file.write("----- User Record -----\n")
file.write(f"First Name : {First_name}\n")
file.write(f"Last Name  : {Last_name}\n")
file.write(f"Address    : {Address}\n")
file.write(f"Gender     : {Gender}\n")
file.write(f"DOB        : {DOB}\n")


file.close()

print("record successfully")

# file = open("heyt.txt",'w')
# file.write("Hello my name is Saloni")
# file.close()

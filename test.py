import BE

name = input("Enter Student name : ")
f_name = input("Enter Father\'s name : ")
m_name = input("enter Mother\'s name : ")

gender = input("Enter the Gender : ")

while True:
    age = input("Enter the age : ")
    try:
        age = int(age)
    except:
        print("Please enter valid digit for age.")
        continue
    if age < 1:
        print("Please enter the valid digit from 1 to 255  for age.")
        continue
    break

data_dict = {"Name" : name,
             "Father\'s Name" : f_name,
             "Mother\'s Name" : m_name,
             "Age" : age,
             "Gender" : gender}
data = BE.BEStudent(name)
data.Set_FamilyBackground(data_dict)


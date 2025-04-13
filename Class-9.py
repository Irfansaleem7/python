Name = "pakistan"



print(Name.count('a'))
NewName = "My Name is Rizwan My Nationality is Pakistani"
print(NewName.find('is'))


my_list = ["Aneeq","Sami","Sohaib","Aisha","Hifza"]
my_list.append('Ameen Alam')
print(my_list)

 # insert :
my_list.insert(2,'Sir Zia')
print(my_list)

# reverse
my_list.reverse()
print(my_list)

# pop kisi data ko delete krny ky liye use krty hain.
print(my_list)
print(my_list.pop(1))

# remove :
# my_list.remove('Sohaib')
# print(my_list)

# sort :
my_list.sort(reverse=False)
print(my_list)

# extend :
new_faculty = ['Abdullah','Ghous']
print("Old list ", my_list)
my_list.extend(new_faculty)

print("Updated list ", my_list)

# extend :
new_faculty = ['Abdullah','Ghous']
print("Old list ", my_list)
my_list.extend(new_faculty)

print("Updated list ", my_list)

# Dictionary :

my_dict = {
    "name" : "John",
    "age" : 25,
    "city" : "Karachi"
}

    # values : 
print(my_dict.values())

# items:
print(my_dict.items())

# get :
print(my_dict.get("name"))
# # keys :
# student = {
#     "name" : "John",
#     "age" : 25,
#     "city" : "Karachi"
# }
# print(my_dict.keys())
# print(student.keys())
# for key in student.keys()


# Error Handling, agr koi program bna rahy houn to us main error ko handle krny ko error handling kehty hain.

# # Error Handling ky 3 methods hain,
# try-except	Catches exceptions to prevent crashes
# try-except-else	Runs else block if no exception occurs
# try-except-finally	Executes finally block always (clean-up code)
# raise	Manually raises an exception
# assert	Debugging tool to check conditions

# num : int = 10
# num2: int = 5
# result = num /num2
# print(result)

# try:
#     result = num / num2
#     print(result)
# except Exception as e:
#     print(e)
# except ZeroDivisionError:
#     print("this is error for zero value")
# User_Input = input("Enter your Number") convert into integer. or loop sy table bnana hy if,elif aur elise sy.


#Day3
firstname ="hello python"
print(firstname)
middlename = " musthafa"
print(middlename)
lastname = "shafi"
print(lastname)
location = "pallabi mitra"
print(location.title())
print(location.upper())
print(location.lower())
print(f"{firstname.title()}{middlename.upper()}musthafa")

#Day4
students = ["papi","sachita","suhail","harshal","iswarya","ananya"]
print(students)
print(students[3])
print(students[3].title())
#Insert
students.append("muskan")
print(students)
students.insert(2,"mani")
print(students)
print(students)
#ressign
students[3] = "harsha"
print(students)
students[3] = "harshal"
print(students)
print(students)
#delete
del students[2]
print(students)

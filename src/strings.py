
name="Sadık"

surName="Tepecik"

age=25

print('My name is '+name+" "+surName+ " and \nI am "+str(age)+" years old")
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(surName[len(surName)-1]) # uzunluk bulmak isin yapılaması gereken len(surname) ama son index ise len(surname)-1

print(name[2:4]) # burasıda substring methodunun kısa kullanımı istenilen parcayı al gel demek
print(name[2: ])

str="kadir bugun python ogreniyor"
print(len(str))
print(str[1:22:2])
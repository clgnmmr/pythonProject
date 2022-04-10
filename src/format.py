
name="Cınar"
age=25

surName="Turan"
print("My name is {} {}".format(name,surName))
#My name is Cınar Turan
print("My name is {0} {1}".format(name,surName)) # burda formatın elemanlarını sıraya göre yazdırabiliriz buranın cıktısı aynı olur ama
#My name is Cınar Turan
print("My name is {1} {0}".format(name,surName)) # burdaki degismis olucaktır
#My name is Turan Cınar
print("My name is {s} {n}".format(n=name,s=surName)) # degiskene verilen atamalr kullanılabilir
#My name is Turan Cınar
print("My name is {} {} and I am {} years old.".format(name,surName,age)) # str ve int degerler donusturmek yerine direk atama yapar
#My name is Cınar Turan and I am 25 years old.
print("My name is {} {} and I am {} years old.".format(name,name,name)) # aynı veriable art arda kullanılabilir
#My name is Cınar Cınar and I am Cınar years old.

result=200/700
print("The result is {r}".format(r=result))
#The result is 0.2857142857142857
print("The result is {r:5.4}".format(r=result)) #burdaki 5 (degisebilir) kac karekter bosluk belli eder 4 ise virgulden sonra kac karkter yazılsın onu belli eder
#The result is 0.2857

print(f"My name is {name} {surName} and I am {age} years old.") # yeni bir ozelliktir  basa f yazarak yapılır
#My name is Cınar Turan and I am 25 years old.
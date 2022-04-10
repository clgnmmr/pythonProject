'''
daire alanı : pi.r2
daire cevresi : 2.pi.r

* yarıcapı verilen bir dairenin alan ve cevresini hesaplayınız

r=3.14
'''

r=float(input("yarıCap :")) #string bir bilgi veriyor integer değiştirmek gerekir
pi=3.14


daireCevresi=2*pi*r
daireAlanı=pi*r*r

print("daire cevresi : "+str(daireCevresi)+" daire alanı : "+str(daireAlanı))

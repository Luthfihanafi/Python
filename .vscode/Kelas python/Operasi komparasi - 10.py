#OPERASI KOMPARASI (>,<,>=,<=,==,!=,is,is not)

#setiap hasil dari operasi komparasi adalah boolean (true/false)



a = 3
b = 3
c = 1

LebihDari = a > 2
print(a,'>',2,'hasilnya adalah =',LebihDari)

KurangDari = a < 4
print(a,'<',4,'hasilnya adalah =',KurangDari)

LebihDariSamaDengan = a >= 3
print(a,'>=',3,'hasilnya adalah =',LebihDariSamaDengan)

KurangDariSamaDengan = a <= 3
print(a,'<=',3,'hasilnya adalah =',KurangDariSamaDengan)

SamaDengan = a == 4
print(a,'==',4,'hasilnya adalah =',SamaDengan)

TidakSamaDengan = a != 4
print(a,'!=',4,'hasilnya adalah =',TidakSamaDengan)

IsSamaDengan = a is b
print(a,'is',b,'hasilnya adalah =',IsSamaDengan)

IsNotTidakSamaDengan = a is not c
print(a,'is not',c,'hasilnya adalah =',IsNotTidakSamaDengan)
#fahrenheit to celcius, kelvin, reamur
'''
untuk fahrenheit ke kelvin
rumus: (F-32) * 5/9 + 273.15
metode: hitung fahrenheit ke celcius terlebih dahulu, lalu celcius ke kelvin
'''

fahrenheit = float(input("masukkan suhu dalam fahrenheit"))

celcius = (fahrenheit - 32) * 5/9
print("suhu dalam celcius adalah=", celcius)
kelvin = (fahrenheit - 32) * 5/9 + 273.15
print("suhu dalam kelvin adalah=", kelvin)
reamur = (fahrenheit - 32) * 4/9
print("suhu dalam reamur adalah=", reamur)


#Kelvin to celcius, fahrenheit, reamur
'''
untuk kelvin ke fahrenheit
rumus: (kelvin-273.15) * 9/5 + 32
metode: hitung kelvin ke celcius terlebih dahulu, lalu celcius ke fahrenheit
'''

kelvin = float(input("masukkan suhu dalam kelvin="))

celcius = kelvin - 273.15
print("suhu dalam celcius adalah=", celcius)
fahrenheit = (kelvin-273.15) * 9/5 + 32
print("suhu dalam fahrenheit adalah=", fahrenheit)
reamur = (kelvin - 273.15) * 4/5
print("suhu dalam reamur adalah=", reamur)


#Celcius to Fahrenheit, kelvin, reamur

celcius = float(input('masukkan suhu dalam celcius='))

fahrenheit = (9/5 * celcius) + 32
print("suhu dalam fahrenheit adalah=", fahrenheit)
kelvin = celcius  + 273.15
print("suhu dalam kelvin adalah=", kelvin)
reamur = 4/5 * celcius
print("suhu dalam reamur adalah=", reamur)


#Reamur to celcius, fahrenheit, kelvin

reamur = float(input('masukkan suhu dalam reamur= '))

celcius = reamur / 0.8
print("suhu dalam celcius adalah=", celcius)
fahrenheit = (reamur * 2.25) + 32
print("suhu dalam fahrenheit adalah=", fahrenheit)
kelvin = (reamur / 0.8) + 273.15
print("suhu dalam kelvin adalah=", kelvin)



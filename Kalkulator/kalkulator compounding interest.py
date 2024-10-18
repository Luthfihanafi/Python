"""A = P (1 + r/n) ** n * t"""
"""
A = jumlah akhir (pokok + bunga)
P = pokok awal (investasi awal)
r = suku bunga tahunan (dalam desimal)
n = frekuensi penggabungan bunga per tahun
t = jangka waktu investasi dalam tahun



"""


p = int(input("masukkan jumlah deposit"))
r = 7 / 100
n = 1
t = int(input("jangka waktu investasi= "))
hitung1 = 1 + r/n
hitung2 = n * t
hitung3 = hitung1 ** hitung2
A = hitung3 * p
formatnumber = "{:,}".format(A).replace(",", ".") #kenapa ada koma dan titik di dalam kurung, karena mengganti koma dengan titik
print(formatnumber)
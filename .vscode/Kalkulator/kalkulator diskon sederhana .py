"""KALKULATOR DISKON SEDERHANA"""
"""
Jumlah diskon = (persentase diskon/100) * harga asli
Harga setelah diskon = harga asli - jumlah diskon

"""

hargaasli = int(input('masukan harga asli = '))
persentasediskon = 100
jumlahdiskon = (persentasediskon / 100) * hargaasli
hargaakhir = hargaasli - jumlahdiskon

print('harga asli = ', hargaasli, 'diskon = ', persentasediskon, '%', 'jumlah diskon = ', jumlahdiskon, 'harga setelah diskon', hargaakhir   )
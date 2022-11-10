#Soal 1 [Data Structure]
#List adalah tipe data yang terbentuk dari beberapa objek baik itu integer, float dll, dan list adalah tipe data ordered jadi kita bisa indexing dan slicing.
#Tuple adalah tipe data ordered yang mana tidak dapat diubah objectnya, ditandain dengan tanda () dan dia bersifat immutable.
#Dictionary adalah pasangan key-value dan ditandai dengan {} kurung kurawal.


#Soal 2: Akses List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]

print (a[1:5])

#Soal 3: Akses Nested List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

print (a[1][1:3])

#Soal 4: List Manipulation
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

a = [
    [5, 9, 8],
    [0, 0, 6]
    ]

a[0][2] = 10
a[1][0] = 11
print (a)

#Soal 5: Delete Element List
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]

areas.pop(9)
areas.pop(8)

print(areas)

#Soal 6: List Comprehension
#Gunakan metode **list comprehension** untuk mencari anggota dari S yang habis di bagi 2, kemudian assign hasilnya dalam bentuk list ke dalam variabel T.

S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x % 2 == 0] 

print (T)

#Soal 8: Menambahkan key-value baru ke Dictionary
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# tambahkan key itali ke objek dictionary dengan value roma

europe["itali"] = "roma"

print (europe)

#Soal 9: Boolean Comparison

#Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'and'
#Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'or'
#Berikan contoh gabungan multiple comparison menggunkan Boolean Comparisin 'not'

print((11 > 8) and (2 < 4))	
print((8 == 8) or (6 != 6))	
print(not(3 <= 1))			

#Soal 10: If-Else Statement
#Lengkapi kode untuk menghasilkan suatu output yang di harapkan

#Buatlah sebuah if-else statement yang dimana akan mem-print 'High' jika grade adalah 'A' dan price lebih dari 100000, kemudian mem-print 'Medium' jika grade adalah 'A' dan price lebih dari 50000 dan memprint 'low' jika grade adalah 'A' dan price lebih kecil dan sama dengan 50000.

A = 100001
if A >= 100000:
    print("High")
elif A >= 50000:
    print("Medium")
elif A <= 50000:
    print("Low")



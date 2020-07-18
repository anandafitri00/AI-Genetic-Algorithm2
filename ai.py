from random import randint
import csv
import random

individu =8
banyakbiner = 15
listindividu = []
listawal = []
datalatih =[]
datauji = []
b = 0
a = 0
c = 0
d = 0
lisfit = []
dekod = []
randomslice = 1 
#algoritma untuk mengenerate angka secara random

def random (banyakbiner):
        import random
        listindividu = []
        for i in range (banyakbiner) :        
                y = random.randrange(0, 2)
                listindividu.append(y)
        return listindividu

def randomindex (randomslice) :
        import random
        listrandomslice = []
        for i in range (randomslice) :
                p = random.randrange(0,14)
        return p
#algoritma untuk memasukkan tiap2 indivisu ke dalam list
for i in range(individu):
	j = random(banyakbiner)
	listawal.append(j)

#algoritma untuk menterjemahkan dari biner ke bahasa yang lebih dimengerti
def dikoding(listawal) :	
	for i in range (len(listawal)) :
		if (listawal[i][0] == 1 and listawal[i][1] == 1 and listawal[i][2] == 1) :
			suhu = "Tinggi"
		elif (listawal[i][0] == 1 and listawal[i][1] == 1 and listawal[i][2] == 0) or (listawal[i][0] == 1 and listawal[i][1] == 0 and listawal[i][2] == 1) or (listawal[i][0] == 0 and listawal[i][1] == 1 and listawal[i][2] == 1):
			suhu = "Normal"
		elif(listawal[i][0] == 0 and listawal[i][1] == 0 and listawal[i][2] == 0):
			suhu = '-'
		else :
			suhu = "Rendah"

		if (listawal[i][3] == 1 and listawal[i][4] == 1 and listawal[i][5] == 1 and listawal[i][6] == 1) :
			waktu = "Pagi"
		elif (listawal[i][3] == 1 and listawal[i][4] == 1 and listawal[i][5] == 1 and listawal[i][6] == 0 ) or (listawal[i][3] == 1 and listawal[i][4] == 0 and listawal[i][5] == 1 and listawal[i][6] == 1) or (listawal[i][3] == 1 and listawal[i][4] == 1 and listawal[i][5] == 0 and listawal[i][6] == 1) or (listawal[i][3] == 0 and listawal[i][4] == 1 and listawal[5] == 1 and listawal[i][6] == 1):
			waktu = "Siang"
		elif (listawal[i][3] == 0 and listawal[i][4] == 0 and listawal[i][5] == 0 and listawal[i][6] == 1 ) or (listawal[i][3] == 1 and listawal[i][4] == 0 and listawal[i][5] == 0 and listawal[i][6] == 0) or (listawal[i][3] == 0 and listawal[i][4] == 1 and listawal[i][5] == 0 and listawal[i][6] == 0) or (listawal[i][3] == 0 and listawal[i][4] == 0 and listawal[5] == 1 and listawal[i][6] == 0):
			waktu = "Sore"
		elif(listawal[i][3] == 0 and listawal[i][4] == 0 and listawal[i][5] == 0 and listawal[i][6] == 0):
			waktu = '-'
		else:
			waktu = "Malam"
			
		if (listawal[i][7] == 1 and listawal[i][8] == 1 and listawal[i][9] == 1 and listawal[i][10] == 1) :
			langit = "Cerah"
		elif (listawal[i][7] == 1 and listawal[i][8] == 1 and listawal[i][9] == 1 and listawal[i][10] == 0 ) or (listawal[i][7] == 1 and listawal[i][8] == 0 and listawal[i][9] == 1 and listawal[i][10] == 1) or (listawal[i][7] == 1 and listawal[i][8] == 1 and listawal[i][9] == 0 and listawal[i][10] == 1) or (listawal[i][7] == 0 and listawal[i][8] == 1 and listawal[i][9] == 1 and listawal[i][10] == 1):
			langit = "Berawan"
		elif (listawal[i][7] == 0 and listawal[i][8] == 0 and listawal[i][9] == 0 and listawal[i][10] == 1 ) or (listawal[i][7] == 1 and listawal[i][8] == 0 and listawal[i][9] == 0 and listawal[i][10] == 0) or (listawal[i][7] == 0 and listawal[i][8] == 1 and listawal[i][9] == 0 and listawal[i][10] == 0) or (listawal[i][7] == 0 and listawal[i][8] == 0 and listawal[i][9] == 1 and listawal[i][10] == 0):
			langit = "Rintik"
		elif(listawal[i][7] == 0 and listawal[i][8] == 0 and listawal[i][9] == 0 and listawal[i][10] == 0) :
			langit = '-'
		else:
			langit = "Hujan"
			
		if (listawal[i][11] == 1 and listawal[i][12] == 1 and listawal[i][13] == 1 ) :
			kelembapan = "Tinggi"
		elif (listawal[i][11] == 1 and listawal[i][12] == 1 and listawal[i][13] == 0) or (listawal[i][11] == 1 and listawal[i][12] == 0 and listawal[i][13] == 1) or (listawal[i][11] == 0 and listawal[i][12] == 1 and listawal[i][13] == 1):
			kelembapan = "Normal"
		elif (listawal[i][11] == 0 and listawal[i][12] == 0 and listawal[i][13] == 0) :
			kelembapan = '-'
		else :
			kelembapan = "Rendah"

		if (listawal[i][14] == 1) :
			kondisi = "Ya"
		else :
			kondisi = "Tidak"
		dekod.append([suhu, waktu, langit, kelembapan, kondisi])
	return(dekod)

wk = dikoding(listawal)

#algoritma untuk membuka dan membaca file csv

with open ('data.csv', 'r') as readFile :
	reader = csv.reader(readFile)
	lines = list(reader)
	lines = wk
with open('data.csv', 'w') as writeFile : 
	writer = csv.writer(writeFile)
	writer.writerows(lines)
	
with open('bismillah.csv') as File :
	angka = 1
	reader = csv.reader(File, delimiter=',', quotechar = ',', quoting =csv.QUOTE_MINIMAL)
	for row in reader :
		angka = 0
		datalatih.append(row)
		
#algoritma untuk membandingkan data latih dengan hasil generate dari komputer yang mana nantinya akan menjadi nilai fitness
		
temp = 0
for a in range (len(wk)) :
	for i in range (len(datalatih)) :
		for b in range (4) :
			if wk[a][b] == datalatih[i][b] or wk[a][b] == "-":
				temp = temp+1
			else :
				temp = 0
		yes = temp/80
	lisfit.append(yes)
	
print('\n')
print('==Data Acak==')
print('\n')
for i in range (len(listawal)) :
	print('data acak ke-',i+1, listawal[i])
	print('hasil decode data acak = ', wk[i])
	print('nilai fitness =', lisfit[i])

parent1 = []
parent2 = []
duplisfit = []
for i in range (len(lisfit)) :
	duplisfit.append(lisfit[i])

parent1.append(max(duplisfit))

for i in range (len(lisfit)) :
        if lisfit[i] == max(lisfit) :
                letakparent1 = i+1

#pemilihan orang tua generasi ke 0 

print('\n')
print('== PEMILIHAN ORANG TUA==')
print('\n')
print('list fitness = ', lisfit)
print('letak parent 1 = ',letakparent1)
print('parent 1 = ', parent1[0])

duplisfit.pop(letakparent1-1)
parent2.append(max(duplisfit))
for i in range (len(duplisfit)) :
	if lisfit [i] == max(duplisfit) :
		letakparent2 = i+1
		
print('letak parent 2 = ',parent2[0])
print('parent 2 = ',letakparent2)

#crossover generasi ke 0 

print('\n')
print('== CROSSOVER DAN MUTASI ==')
print('\n')
F = randomindex(randomslice)
print('Parent 1 = ' , listawal[letakparent1-1])
print('Parent 2 = ' , listawal[letakparent2])
print('crossover pada indeks ke-', F, '(perhitungan indeks list dimulai dari 0)')
print('Hasil crossover = ')
listanak1= []
listanak2= []

otwanak11 = listawal[letakparent1][F:]
otwanak12 = listawal[letakparent2][:F]
otwanak21 = listawal[letakparent1][:F]
otwanak22 = listawal[letakparent2][F:]

listanak1 = otwanak11+otwanak12
listanak2 = otwanak21+otwanak22

print(listanak1)
print(listanak2)
print('\n')
k = 0

#mutasi generasi ke 0 

import random
peluangmutasi = 1/banyakbiner
for i in range (banyakbiner) :
	nilairandom= random.random()
	if nilairandom>=0 and nilairandom<=peluangmutasi :
		if listanak1[i]==0 :
			listanak1[i]= 1
		elif listanak1[i]==1 :
			listanak1[i]=0
		else :
			k = 0
	else :
		k = 0

print('Mutasi pada anak 1 = ', listanak1)

for i in range (banyakbiner) :
	nilairandom= random.random()
	if nilairandom>=0 and nilairandom<=peluangmutasi :
		if listanak2[i]==0 :
			listanak2[i]=1
		elif listanak2[i]==1 :
			listanak2[i]=0
		else :
			k = 0
	else :
		k = 0
						
print('Mutasi pada anak 2 = ', listanak2)

listawal.pop(letakparent1)
listawal.pop(letakparent2)
listawal.append(listanak1)
listawal.append(listanak2)

lisfit.clear()
duplisfit.clear()
g = []
print('Individu untuk generasi selanjutnya adalah')
for i in range (len(listawal)) :
	print('individu ke-',i+1, listawal[i])
	print('hasil decode data acak = ', wk[i])
	print('\n')

# regenerasi untuk gnerasi selanjutnya

print("\n")
print('== REGENERASI ==')
print("\n")
generasi  = 3
gen = 0
for gen in range (generasi) :
	lisfit.clear()
	duplisfit.clear()
	print('Individu saat ini')
	print('\n')
	for i in range (len(listawal)) :
		print('individu ke-',i+1, 'generasi ke-',gen+1, listawal[i])
		print('hasil decode data acak = ', wk[i])
		print('\n')

	with open ('data.csv', 'r') as readFile :
		reader = csv.reader(readFile)
		lines = list(reader)
		lines = wk
	with open('data.csv', 'w') as writeFile : 
		writer = csv.writer(writeFile)
		writer.writerows(lines)
		
	with open('bismillah.csv') as File :
		angka = 1
		reader = csv.reader(File, delimiter=',', quotechar = ',', quoting =csv.QUOTE_MINIMAL)
		for row in reader :
			angka = 0
			datalatih.append(row)
			
	for a in range (len(wk)) :
		for i in range (len(datalatih)) :
			for b in range (4) :
				if wk[a][b] == datalatih[i][b] or wk[a][b] == "-":
					temp = temp+1
				else :
					temp = 0
			yes = temp/80
		lisfit.append(yes)
		
	for i in range(len(listawal)) :
		print('nilai fitness individu ke',i+1, 'generasi ke-',gen+1,'= ', lisfit[i])

	parent1 = []
	parent2 = []
	duplisfit = []
	for i in range (len(lisfit)) :
		duplisfit.append(lisfit[i])

	parent1.append(max(duplisfit))

	for i in range (len(lisfit)) :
			if lisfit[i] == max(lisfit) :
					letakparent1 = i+1

	print('\n')
	print('== PEMILIHAN ORANG TUA GENERASI KE-', gen+1, ' ==')
	print('\n')
	print('list fitness = ', lisfit)
	print('letak parent 1 = ',letakparent1)
	print('parent 1 = ', parent1[0])

	duplisfit.pop(letakparent1-1)
	parent2.append(max(duplisfit))
	for i in range (len(duplisfit)) :
		if lisfit [i] == max(duplisfit) :
			letakparent2 = i+1
			
	print('letak parent 2 = ',parent2[0])
	print('parent 2 = ',letakparent2)

	print('\n')
	print('== CROSSOVER DAN MUTASI GENERASI KE-', gen+1, ' ==')
	print('\n')
	F = randomindex(randomslice)
	print('Parent 1 = ' , listawal[letakparent1-1])
	print('Parent 2 = ' , listawal[letakparent2])
	print('crossover pada indeks ke-', F, '(perhitungan indeks list dimulai dari 0)')
	print('Hasil crossover = ')
	listanak1= []
	listanak2= []

	otwanak11 = listawal[letakparent1][F:]
	otwanak12 = listawal[letakparent2][:F]
	otwanak21 = listawal[letakparent1][:F]
	otwanak22 = listawal[letakparent2][F:]

	listanak1 = otwanak11+otwanak12
	listanak2 = otwanak21+otwanak22

	print(listanak1)
	print(listanak2)
	print('\n')
	k = 0

	import random
	peluangmutasi = 1/banyakbiner
	for i in range (banyakbiner) :
		nilairandom= random.random()
		if nilairandom>=0 and nilairandom<=peluangmutasi :
			if listanak1[i]==0 :
				listanak1[i]= 1
			elif listanak1[i]==1 :
				listanak1[i]=0
			else :
				k = 0
		else :
			k = 0

	print('Mutasi pada anak 1 = ', listanak1)

	for i in range (banyakbiner) :
		nilairandom= random.random()
		if nilairandom>=0 and nilairandom<=peluangmutasi :
			if listanak2[i]==0 :
				listanak2[i]=1
			elif listanak2[i]==1 :
				listanak2[i]=0
			else :
				k = 0
		else :
			k = 0
							
	print('Mutasi pada anak 2 = ', listanak2)

	listawal.pop(letakparent1)
	listawal.pop(letakparent2)
	listawal.append(listanak1)
	listawal.append(listanak2)
	
	for i in range (len(listawal)) :
		print('individu ke-',i+1, 'generasi ke-',gen+1, '= ', listawal[i])
		print('hasil decode data acak = ', wk[i])
		print('\n')

#algoritma untuk mengeluarkan individu terbaik
	
for i in range (len(lisfit)) :
			if lisfit[i] == max(lisfit) :
					letakfin = i+1
print('Individu terbaik dengan fitness', max(lisfit))
print('terletak pada individu ke-', letakfin)
print('dengan kromosom =', listawal[letakfin-1])

#algoritma untuk menterjemahkannya

dekodfin = []
for i in range (14) :
	if (listawal[letakfin-1][0] == 1 and listawal[letakfin-1][1] == 1 and listawal[letakfin-1][2] == 1) :
		suhu = "Tinggi"
	elif (listawal[letakfin-1][0] == 1 and listawal[letakfin-1][1] == 1 and listawal[letakfin-1][2] == 0) or (listawal[letakfin-1][0] == 1 and listawal[letakfin-1][1] == 0 and listawal[letakfin-1][2] == 1) or (listawal[letakfin-1][0] == 0 and listawal[letakfin-1][1] == 1 and listawal[letakfin-1][2] == 1):
		suhu = "Normal"
	elif(listawal[letakfin-1][0] == 0 and listawal[letakfin-1][1] == 0 and listawal[letakfin-1][2] == 0):
		suhu = '-'
	else :
		suhu = "Rendah"

	if (listawal[letakfin-1][3] == 1 and listawal[letakfin-1][4] == 1 and listawal[letakfin-1][5] == 1 and listawal[letakfin-1][6] == 1) :
		waktu = "Pagi"
	elif (listawal[letakfin-1][3] == 1 and listawal[letakfin-1][4] == 1 and listawal[letakfin-1][5] == 1 and listawal[letakfin-1][6] == 0 ) or (listawal[letakfin-1][3] == 1 and listawal[letakfin-1][4] == 0 and listawal[letakfin-1][5] == 1 and listawal[letakfin-1][6] == 1) or (listawal[letakfin-1][3] == 1 and listawal[letakfin-1][4] == 1 and listawal[letakfin-1][5] == 0 and listawal[letakfin-1][6] == 1) or (listawal[letakfin-1][3] == 0 and listawal[letakfin-1][4] == 1 and listawal[letakfin-1][5] == 1 and listawal[letakfin-1][6] == 1):
			waktu = "Siang"
	elif (listawal[letakfin-1][3] == 0 and listawal[letakfin-1][4] == 0 and listawal[letakfin-1][5] == 0 and listawal[letakfin-1][6] == 1 ) or (listawal[letakfin-1][3] == 1 and listawal[letakfin-1][4] == 0 and listawal[letakfin-1][5] == 0 and listawal[letakfin-1][6] == 0) or (listawal[letakfin-1][3] == 0 and listawal[letakfin-1][4] == 1 and listawal[letakfin-1][5] == 0 and listawal[letakfin-1][6] == 0) or (listawal[letakfin-1][3] == 0 and listawal[letakfin-1][4] == 0 and listawal[letakfin-1][5] == 1 and listawal[letakfin-1][6] == 0):
		waktu = "Sore"
	elif(listawal[letakfin-1][3] == 0 and listawal[letakfin-1][4] == 0 and listawal[letakfin-1][5] == 0 and listawal[letakfin-1][6] == 0):
		waktu = '-'
	else:
		waktu = "Malam"
			
	if (listawal[letakfin-1][7] == 1 and listawal[letakfin-1][8] == 1 and listawal[letakfin-1][9] == 1 and listawal[letakfin-1][10] == 1) :
		langit = "Cerah"
	elif (listawal[letakfin-1][7] == 1 and listawal[letakfin-1][8] == 1 and listawal[letakfin-1][9] == 1 and listawal[letakfin-1][10] == 0 ) or (listawal[letakfin-1][7] == 1 and listawal[letakfin-1][8] == 0 and listawal[letakfin-1][9] == 1 and listawal[letakfin-1][10] == 1) or (listawal[letakfin-1][7] == 1 and listawal[letakfin-1][8] == 1 and listawal[letakfin-1][9] == 0 and listawal[letakfin-1][10] == 1) or (listawal[letakfin-1][7] == 0 and listawal[letakfin-1][8] == 1 and listawal[letakfin-1][9] == 1 and listawal[letakfin-1][10] == 1):
		langit = "Berawan"
	elif (listawal[letakfin-1][7] == 0 and listawal[letakfin-1][8] == 0 and listawal[letakfin-1][9] == 0 and listawal[letakfin-1][10] == 1 ) or (listawal[letakfin-1][7] == 1 and listawal[letakfin-1][8] == 0 and listawal[letakfin-1][9] == 0 and listawal[letakfin-1][10] == 0) or (listawal[letakfin-1][7] == 0 and listawal[letakfin-1][8] == 1 and listawal[letakfin-1][9] == 0 and listawal[letakfin-1][10] == 0) or (listawal[letakfin-1][7] == 0 and listawal[letakfin-1][8] == 0 and listawal[letakfin-1][9] == 1 and listawal[letakfin-1][10] == 0):
		langit = "Rintik"
	elif(listawal[letakfin-1][7] == 0 and listawal[letakfin-1][8] == 0 and listawal[letakfin-1][9] == 0 and listawal[letakfin-1][10] == 0) :
		langit = '-'
	else:
		langit = "Hujan"
			
	if (listawal[letakfin-1][11] == 1 and listawal[letakfin-1][12] == 1 and listawal[letakfin-1][13] == 1 ) :
		kelembapan = "Tinggi"
	elif (listawal[letakfin-1][11] == 1 and listawal[letakfin-1][12] == 1 and listawal[letakfin-1][13] == 0) or (listawal[letakfin-1][11] == 1 and listawal[letakfin-1][12] == 0 and listawal[letakfin-1][13] == 1) or (listawal[letakfin-1][11] == 0 and listawal[letakfin-1][12] == 1 and listawal[letakfin-1][13] == 1):
		kelembapan = "Normal"
	elif (listawal[letakfin-1][11] == 0 and listawal[letakfin-1][12] == 0 and listawal[letakfin-1][13] == 0) :
		kelembapan = '-'
	else :
		kelembapan = "Rendah"

	if (listawal[letakfin-1][14] == 1) :
		kondisi = "Ya"
	else :

		kondisi = "Tidak"			
#algoritma untuk memasukkan terjemahan dari hasil individu terbaik
dekodfin.append([suhu, waktu, langit, kelembapan, kondisi])
print('hasil decode = ', dekodfin)
print('\n')

#algoritma untuk membuka data uji
datauji = []
with open('data_uji_opsi_1.csv') as File :
		angka = 1
		reader = csv.reader(File, delimiter=',', quotechar = ',', quoting =csv.QUOTE_MINIMAL)
		for row in reader :
			angka = 0
			datauji.append(row)

#algoritma untuk membandingkan individu terbaik dengan data uji

r = 0
e = 0
ty = 0
for i in range (len(datauji)) :
		if datauji[i][r] == dekodfin[0][r] or dekodfin[0][r] == '-' :
			ty = datauji[i].append('Ya')
		else :
			ty = datauji[i].append('Tidak')
			
print("\n")
for i in range (len(datauji)):
	print(datauji[i])

#algoritma untuk memasukkan data yang telah di bandingkan ke dalam csv

import csv

out = csv.writer(open("datafin.csv", "w"), delimiter = "\n", quoting=csv.QUOTE_ALL)
out.writerow(datauji)
print('data berhasil dimasukkan')


#bang masih banyak bugnya kalo error run lagi yaak 

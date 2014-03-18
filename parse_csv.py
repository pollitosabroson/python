import csv
count = 0
file = open('db_frente.csv')
reader = csv.reader(file)
for line in reader:
	count = count + 1
	calle = line[4]	
	numero = line[5]
	colonia = line[7]
	delegacion = line[10]
	print "Calle: ", calle," Numero: ",numero," Colonia: ",colonia," Delegacion", delegacion,"cuenta", count
	
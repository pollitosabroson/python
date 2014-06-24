import csv
import psycopg2
conn = psycopg2.connect("dbname = frente user = 'data4' host = 'localhost' password = '123'  port=5432")
cur = conn.cursor()
count = 0
file = open('prueba1.csv')
reader = csv.reader(file)
for line in reader:
	dele = ""
	cate = ""
	count = count + 1
	nombre = line[1]
	amaterno = line[2]
	aparterno = line[3]
	cumpleanos = line[4]
	telefono = line[5]
	mail = line[6]
	calle = line[7]
	cp = line[8]
	numeroexterno = line[9]
	numerointerno = line[10]
	colonia = line[11]
	delegacion = line[12]
	entregas = line[13]
	cupon = line[14]
	fvencimiento = line[15]
	activo = line[16]
	categoria = line[17]
	subcategoria1 = line[18]
	subcategoria2 = line[19]
	subcategoria3 = line[20]
	created = line[21]
	ruta = line[22]
	distribucion = line[23]
	empresa = line[24]
	puesto = line[25]
	referencia = line[26]
	dotacion = line[27]
	ordenentrega = line[28]
	embolsado = line[29]
	querycate = """SELECT id FROM app_categoria WHERE "descripcion_Categoria" = '%s'""" % categoria
	cur.execute(querycate)
	rowscate = cur.fetchall()
	for ro in rowscate:
		cate = ro
		print cate
	querydel = """SELECT id FROM app_delegacion_frente WHERE "descripcion_Delegacion" = '%s'""" % delegacion.title()
	cur.execute(querydel)
	rowsdel = cur.fetchall()
	for ro in rowsdel:
		dele = ro
		print dele
	query = """SELECT id FROM app_colonia_frente WHERE "descripcion_Colonia" = 'SANTA FE' AND delegacion_id = '%s' """ % dele
	cur.execute(query)
	rows = cur.fetchall()
	print "\nShow me the databases:\n"
	for row in rows:
		print row
	print "Empieza",nombre, aparterno,amaterno, cumpleanos, telefono, mail, calle, cp, numeroexterno, numerointerno, colonia, delegacion,  entregas, cupon, fvencimiento, activo, categoria, subcategoria1,
	subcategoria2, subcategoria3, created, ruta, distribucion, empresa, puesto, referencia, dotacion, ordenentrega, embolsado
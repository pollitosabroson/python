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
	col = ""
	sub1 = ""
	sub2 = ""
	sub3 = ""
	rutas = ""
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
	querysub1 = """SELECT id FROM app_subcategoria1 WHERE "descripcion_SubCategoria1" = '%s'""" % subcategoria1
	cur.execute(querysub1)
	rowsub1 = cur.fetchall()
	for rows1 in rowsub1:
		sub1 = rows1
	querysub2 = """SELECT id FROM app_subcategoria2 WHERE "descripcion_SubCategoria2" = '%s'""" % subcategoria2
	cur.execute(querysub2)
	rowsub2 = cur.fetchall()
	for rows2 in rowsub2:
		sub2 = rows2
	querysub3 = """SELECT id FROM app_subcategoria3 WHERE "descripcion_SubCategoria3" = '%s'""" % subcategoria3
	cur.execute(querysub3)
	rowsub3 = cur.fetchall()
	for rows3 in rowsub3:
		sub3 = rows3
	querydel = """SELECT id FROM app_delegacion_frente WHERE "descripcion_Delegacion" = '%s'""" % delegacion.title()
	cur.execute(querydel)
	rowsdel = cur.fetchall()
	for ro in rowsdel:
		dele = ro[0]
	query = """SELECT id FROM app_colonia_frente WHERE "descripcion_Colonia" = '%s' AND delegacion_id = '%s' """ % (colonia,dele)
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		col = row
	queryrut = """SELECT id FROM app_ruta WHERE "descripcion_Ruta" = '%s'""" % ruta
	cur.execute(queryrut)
	rowsrut = cur.fetchall()
	for rowrut in rowsrut:
		rutas = rowrut
		print "Rutas"
		print rutas
	print "Empieza",nombre, aparterno,amaterno, cumpleanos, telefono, mail, calle, cp, numeroexterno, numerointerno, colonia, delegacion,  entregas, cupon, fvencimiento, activo, categoria, subcategoria1,
	subcategoria2, subcategoria3, created, ruta, distribucion, empresa, puesto, referencia, dotacion, ordenentrega, embolsado
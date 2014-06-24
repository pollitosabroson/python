import json 
import requests
#importarmos la libreria de carton 
from cartodb import CartoDBAPIKey, CartoDBException
#Añadimos nuestros datos
user =  'User_name'
API_KEY ='Api_key'
cartodb_domain = 'User_domine'
cl = CartoDBAPIKey(API_KEY, cartodb_domain)
try:
	#hacemos la consulta
	consulta = cl.sql('select * from table_name')
	contador = 0
	contconsulta = 0
	nogeo = 0
	#buscamos dentro de las columnas las que vamos a necesitar
	for row in consulta['rows']:
		a = row['table_rows']
		print a
		estado = row['table_rows']
		calle = row['table_rows']
		municipio =row['municipio'] 
		url = "url que pedimos un json"
		req = requests.get(url).json()
		b = req['response']['numFound']
		contconsulta = contconsulta + 1
		print "Consultas realisadas: ", contconsulta
		#comparamos que la url que nose regrese un valor valido
		if b != 0:
			lat = req['response']['docs'][0]['latitud_coordinate']
			log = req['response']['docs'][0]['longitud_coordinate']
			#actualizamos la tabla
			otro =("UPDATE table_name SET the_geom = ST_SetSRID(ST_MakePoint(%s,%s), 4326) WHERE cct= '%s'") %(log, lat, a)
			insert = cl.sql(otro)
			contador = contador +1
			print "Numeros de insert validados",contador
		#no se encuentra en la url pedimos la ubicacion a google maps
		else:
			#agregamos los campos que requerimos
			add = "%s %s,%s, Mexico" % (calle,municipio, estado)
			print add
			# agreamos los campos a la url de google
			geocode_url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false&region=mx" % add
			respuesta = requests.get(geocode_url).json()
			#parseamos el resultado y obtenmos la latitud y lomgitu
			for results in respuesta['results']:
				lati = results['geometry']['location']['lat']
				longi = results['geometry']['location']['lng']
				#actualizamos la tabla  con la posision que nos diao google
				update =("UPDATE table_name SET the_geom = ST_SetSRID(ST_MakePoint(%s,%s), 4326) WHERE cct= '%s'") %(longi, lati, a)
				insert = cl.sql(update)
				nogeo = nogeo +1
				print "contador sin geoposicion",nogeo
except CartoDBException as e:
    print ("some error ocurred", e)
#! /usr/bin/env python3
import time
import requests
import re

URL_BASE = 'https://www.infosubvenciones.es/bdnstrans/' 
sesion = requests.Session() # gestion de cookies
sesion.verify = False # ignora certificado SSL
requests.packages.urllib3.disable_warnings() 

# obtengo csrf
html = sesion.get(URL_BASE + 'GE/es/concesiones').text
csrf = re.findall('csrf\" value=\"(.*)\"',html)[0]

# post filtros de busqueda y csrf
filter_data = {'_ministerios': '1', '_organos': '1', '_cAutonomas': '1', '_departamentos': '1', '_locales': '1', '_localesOculto': '1', 'beneficiarioFilter': 'DNI', 'beneficiarioDNI': '', 'beneficiarioNombre': '', 'beneficiario': '', 'fecDesde': '', 'fecHasta': '', 'tipoBusqPalab': '1', 'titulo': '', '_regiones': '1', '_actividadesNACE': '1', '_instrumentos': '1'}
filter_data['_csrf'] = csrf
request_2 = sesion.post(URL_BASE + 'GE/es/concesiones', data=filter_data)

page=1
# maximo 200 entradas ordenado por fecha de concesion de antiguas a nuevas
search_params = {'type': 'concs','rows': '200','sidx': '8', 'sord': 'asc'} 
search_params['page']=str(page)
print(f'pagina {1:05d}\t🔽')
t=time.time()
data = sesion.get('https://www.infosubvenciones.es/bdnstrans/busqueda', params=search_params)
t=time.time()-t
print(f'pagina {1:05d}\t✅  {t:.1f}secs')

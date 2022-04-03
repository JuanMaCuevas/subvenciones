#!/bin/bash
ND=`gdate +%s%N | cut -b1-13`
echo Descargando página $1...
curl --silent --output page_`printf %03d $1`.json 'https://www.infosubvenciones.es/bdnstrans/busqueda?type=concs&_search=false&nd='$ND'&rows='$ROWS'&page='$1'&sidx=8&sord=asc' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Referer: https://www.infosubvenciones.es/bdnstrans/GE/es/concesiones' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  -H 'Connection: keep-alive ' \
  -H 'Cookie: TS014c174a=01b3ae6da89274eb53063b910b8981c37c1ea802e862a3458499000a118151422c4e7d30c14c8b3ab059ae8b8fa46d819a5e988d7a; JSESSIONID=aPTmp1WSF9Qz4GUi_dXdRymtJQG6nSGb3Ihppmdo3ygrjLpv6FYk!-184169369!431308930; TS01bc68c4=01b3ae6da8e2f88ab301d93528a7ae3fbe0f531009366f99dd87c60228963bc86fe2040d12dbadd63c6ff6b66e37e4011abaef4bd9; TSeafa35b3027=0841270cedab2000232c1cb96d66cbdffae075b66a3b54d0dfde46d580a16c399d3364965ab0e3dc08b2b2613411300028940746a494b2d57a8f5f6fbadf89fd0abf7f01d917f7f0cbd93483ceb9ec43af5dec0781835c5e6d61ea7ab07a6716' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' 
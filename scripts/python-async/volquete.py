import aiohttp
import asyncio
import time
import json

headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36' ,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'Referer': 'https://www.infosubvenciones.es/bdnstrans/GE/es/concesiones',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Cookie': 'TS014c174a=01b3ae6da881ed67355143c0100b7e9bb5e10742c6e8002386c9987423999057a16d86ceb430a0dc5e755810d0696811ce71fefe01; JSESSIONID=PFHnr-gr0Hr1K08RcUYVAkls1D6fduZ_T3Y_W_kJl3g75E4b4O_a\u0021561571137\u00211075146980; TS01bc68c4=01b3ae6da8419b9a39db5c7324e27f66e99cf5492210a783ca97cef5a346113eee2a35b354d19e0cb7fae8a07ee8ac874e6d3e9eaf; TSeafa35b3027=0841270cedab20007ac38edfe473acf6fdb640e161728b1517f9a02daf98f0199628895c881679f00860076838113000e8a1993a85370e5123b0480ad07fc3b5a5bb01717151035ebc37e595ee25f3a5e89efdaa78a0468d5df1a11eca320cc3',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache' 
}

def get_url(rows,page):
    time_millis = int(time.time()*1000)
    return  f'https://www.infosubvenciones.es/bdnstrans/busqueda?type=concs&_search=false&nd={time_millis}&rows={rows}&page={page}&sidx=8&sord=asc'


start_time = time.time()


async def get_page(session, index):
    async with session.get(get_url(*index),headers=headers,ssl=False) as resp:
        print('fetching',index[1])
        j = await resp.json()
        data = (index,j)
        return data


async def main():

    async with aiohttp.ClientSession() as session:

        tasks = []
        rows = 200
        for page in range(1, 10):
            tasks.append(asyncio.ensure_future(get_page(session, (rows,page))))

        list_all = await asyncio.gather(*tasks)
        with open('json_data.json', 'w') as outfile:
            for page_data in list_all:
                json.dump(page_data, outfile)
                print(page_data[0],'saved to json')
            

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

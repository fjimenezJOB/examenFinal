# Scraping
from bs4 import BeautifulSoup
import requests
import lxml
import re
from pymongo import MongoClient

# Mongo URL Atlas
MONGO_URL_ATLAS = 'mongodb+srv://franjimenez:Francisco1231998@develop-0hasi.mongodb.net/test?authSource=admin&replicaSet=develop-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
db = client['Web_Scraping']

def subirLinks(link):
    collection = db['linksHoteles']
    collection.insert_one({'link' : link})

def subirInfoHabitacion(diccionario_info):
    collection = db['hoteles']
    collection.insert_one(diccionario_info)

def sacarInfo():
    collection = db['hoteles']
    hoteles = collection.find_all({},{'_id':0})
    print(hoteles)


def recolectarLinks(url):
    links = []
    html = requests.get(url)

    if html.status_code == 200:
        hotel = BeautifulSoup(html.text, 'lxml')
    
    # Extraer el link de cada hotel
        busqueda_links = hotel.find_all('a', attrs={'itemprop':'url'})
        for link in busqueda_links:
            link_parcial = link.get('href')
            links.append(link_parcial)
    else:
        links = None

    return links

def recolectarHotel(urlReservaHotel):

    # Crear diccionario vacio para poblarlo con la información
    hotelRural= {}

    # recoger el html del artículo
    html = requests.get(urlReservaHotel)

    # si el code devuelto es 200 entramos con BeautifulSoup
    if html.status_code == 200:
        hotel = BeautifulSoup(html.text, 'lxml')

        # Extraer titulo de la noticia
        nombreHotel = hotel.find_all('span', attrs={'itemprop': 'name'})[4]

        if nombreHotel:
            hotelRural['titulo'] = nombreHotel.getText()
        else:
            hotelRural['titulo'] = None

        # Extraemos el precio por noche del Hotel
        precioHotel = hotel.find('span', attrs={'style': 'font-size:22px;color:#517500;font-weight:700;'})

        if precioHotel:
            hotelRural['precio'] = precioHotel.getText()
        else:
            hotelRural['titulo'] = None

    return hotelRural

# links = recolectarLinks('https://www.casasrurales.net/hoteles-rurales/mallorca')

# for link in links:
#     subirLinks(link)
#     info_habitacion = recolectarHotel(link)
#     subirInfoHabitacion(info_habitacion)

sacarInfo()
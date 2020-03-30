# Scraping
from bs4 import BeautifulSoup
import requests
import lxml
import re

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

        # # Extraer imagen del hotel
        # media = hotel.find('div', attrs={'class': 'foto_desa'}).get('img')
        # if media:
        #     imagenes = media.find_all('img')
        #     if len(imagenes) == 0:
        #         print('No hay imagenes')
        #     else:
        #         imagen = imagenes[-1]
        #         img_src = imagen.get('src')
        #         try:
        #             img_req = requests.get(img_src)
        #             if img_req.status_code == 200:
        #                 noticias_dic['imagen'] = img_req.content
        #             else:
        #                 noticias_dic['imagen'] = None
        #         except:
        #             print('No se puedo obtener la imagen') 
        # else:
        #     print('No se encontro media')

    return hotelRural

# recolectarLinks('https://www.casasrurales.net/hoteles-rurales/mallorca')

recolectarHotel('https://www.casasrurales.net/hoteles-rurales/finca-son-vivot--c63229')


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
        linkGeneral = 'https://www.booking.com/hotel/es'
        links_hoteles = []
        links = hotel.find_all('a', attrs={'class':'hotel_name_link url'})
        for link in links:
            link_actual = link.get('href')
            linkCompleto = linkGeneral+link_actual
            links_hoteles.append(linkCompleto)
    else:
        links_hoteles = None

    return links_hoteles



def recolectarHotel(urlReservaHotel):

    # Crear diccionario vacio para poblarlo con la información
    hotelRural= {}

    # recoger el html del artículo
    html = requests.get(urlReservaHotel)

    # si el code devuelto es 200 entramos con BeautifulSoup
    if html.status_code == 200:
        noticia = BeautifulSoup(html.text, 'lxml')

        # Extraer titulo de la noticia
        titulo = noticia.find('h1', attrs={'itemprop': 'headline'})
        if titulo:
            noticias_dic['titulo'] = titulo.text
        else:
            noticias_dic['titulo'] = None

        # Extraer fecha de la noticia
        fecha = noticia.find(
            'time', attrs={'itemprop': 'dateCreated'}).get('datetime')
        if fecha:
            noticias_dic['fecha'] = fecha
        else:
            noticias_dic['fecha'] = None

        # Extraer imagen de la noticia
        media = noticia.find('div', attrs={'class': 'foto_desa'}).get('img')
        if media:
            imagenes = media.find_all('img')
            if len(imagenes) == 0:
                print('No hay imagenes')
            else:
                imagen = imagenes[-1]
                img_src = imagen.get('src')
                try:
                    img_req = requests.get(img_src)
                    if img_req.status_code == 200:
                        noticias_dic['imagen'] = img_req.content
                    else:
                        noticias_dic['imagen'] = None
                except:
                    print('No se puedo obtener la imagen')
        else:
            print('No se encontro media')

    return noticias_dic

    def sacarLinks(url):
        ''' Saca los links de la pagina de busqueda donde están todos los Hoteles, para despues poder sacar la información de cada uno'''


def recolectarLinks(url):
    links = []
    html = requests.get(url)

    if html.status_code == 200:
        hotel = BeautifulSoup(html.text, 'lxml')
    
    # Extraer el link de cada hotel
        linkGeneral = 'https://www.booking.com/hotel/es'
        links_hoteles = []
        links = hotel.find_all('a', attrs={'class':'hotel_name_link url'})
        for link in links:
            link_actual = link.get('href')
            linkCompleto = linkGeneral+link_actual
            links_hoteles.append(linkCompleto)
    else:
        links_hoteles = None

    return links_hoteles



recolectarLinks('https://www.booking.com/searchresults.es.html?aid=356980&label=gog235jc-1DCAYYmgQoRjhlSApYA2hGiAEBmAEKuAEXyAEP2AED6AEB-AECiAIBqAIDuAK1uob0BcACAQ&sid=6827b38af34a72f723ee472ae7e2d3e1&sb=1&sb_lp=1&src=theme_landing_region&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fcountry-houses%2Fregion%2Fes%2Fmallorca.es.html%3Faid%3D356980%3Blabel%3Dgog235jc-1DCAYYmgQoRjhlSApYA2hGiAEBmAEKuAEXyAEP2AED6AEB-AECiAIBqAIDuAK1uob0BcACAQ%3Bsid%3D6827b38af34a72f723ee472ae7e2d3e1%3B&theme_id=29&theme_source=theme_landing_region&ss=Mallorca&is_ski_area=0&ssne=Mallorca&ssne_untouched=Mallorca&dest_id=767&dest_type=region&checkin_year=2020&checkin_month=4&checkin_monthday=6&checkout_year=2020&checkout_month=4&checkout_monthday=8&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1')
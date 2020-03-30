# Scraping
from bs4 import BeautifulSoup
import requests
import lxml
import re


def scrap(url):
    # Recogida de HTML
    diariomallorca = requests.get(url)

    # VAMOS A EMPEZAR A PREPARAR LA 'SOUP'
    soup = BeautifulSoup(diariomallorca.text, 'lxml')

    # busca por toda la página donde aparece esta unión de carácteres
    soup.findAll(text=re.compile('corona'))

    # sacar enlaces con las palabras
    cantidad = soup.findAll('a')
    enlaces_corona = []
    palabras = ['coronavirus', 'Coronavirus',
                'CORONAVIRUS', 'COVID-19', 'Covid-19', 'covid-19']
    for i in range(0, len(palabras)):
        if soup.findAll('a', text=re.compile(palabras[i])):
            enlaces_corona.append(soup.findAll(
                'a', attrs={'href': re.compile('http')}, text=re.compile('coronavirus')))

    # limpiar las url con http
    links = []
    for i in range(0, len(enlaces_corona)):
        for link in enlaces_corona[i]:
            links.append(link.get('href'))

    # eliminar dublicados
    linksNuevo = set(links)

    # links la lista con las url, necesarias para hacer un seguimiento de las noticias del coronavirus, en primera página del UltimaHora
    links = list(linksNuevo)

    return links


def recolectar_noticia(articulo):

    # Crear diccionario vacio para poblarlo con la información
    noticias_dic = {}

    # recoger el html del artículo
    html = requests.get(articulo)

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
        # Recoje el HTML
        diariomallorca = requests.get(url)

        # Creamos la sopa
        soup = BeautifulSoup(diariomallorca.text, 'lxml')

        # sacar enlaces con las palabras
        cantidad = soup.findAll('a')

        return links


import requests
from bs4 import BeautifulSoup

class Scrapper:
    def __init__(self, url):
        self.url = url
        self.response = self.get_url()

    def get_url(self):
        """
        Metodo para obtener el contenido de la pagina web
        :return: contenido de la pagina web
        validamos una posible respuesta invalida o un error al
        utlizar la libreria requests
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            if response.status_code == 200:
                return response.content
            else:
                print(f"Error: status code {response.status_code}")
                return None
        except response.exceptions.RequestException as e:
            print(f"Error making request to {self.url}: {e}")
            return None


    def analize_content(self):
        """
        Metodo para analizar el contenido de la pagina web
        :return: informacion de los productos
        usamos la libreria beautifulsoup para analizar el contenido
        obtenemos mediante el metodo find_all los divs con la clases
        tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem, limitamos la busqueda a solo 15 productos
        hacemos una iteracion para obtener los nombres, precios y promociones de cada uno de los productos
        generamos un diccionario con la informacion de cada producto y la devolvemos
        en una lista de diccionarios que contiene la url consultada y los productos
        """
        data_products = list()
        content = self.response
        product_info = {}
        soup = BeautifulSoup(content, "lxml")
        products = soup.find_all("div", class_="tiendasjumboqaio-cmedia-integration-cencosud-0-x-galleryItem", limit=15)
        for product in products:
            name = product.find("div", class_="vtex-product-summary-2-x-nameContainer").find("span").text
            price = product.find("div", class_="tiendasjumboqaio-jumbo-minicart-2-x-price").text
            promo_price = product.find("div", class_="tiendasjumboqaio-jumbo-minicart-2-x-price").text
            product = {"name": name, "price": price, "promo_price": promo_price}
            data_products.append(product)

        product_info = {"url": self.url, "products": data_products}
        return product_info

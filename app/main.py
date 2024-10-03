from fastapi import FastAPI
from pydantic import BaseModel
from app.scrapping import Scrapper

app = FastAPI()

class Product(BaseModel):
    name: str
    price: str = None
    promo_price: str = None


class ProductResponse(BaseModel):
    url: str
    product : Product = None


@app.post("/create-product")
async def create_product(data: ProductResponse):
    """
    Metodo POST para procesar la informacion de los productos
    :url: url de la pagina web
    :return: informacion de los productos
    generamos un diccionario con la informacion de cada producto y la devolvemos
    en una lista de diccionarios que contiene la url consultada y los productos.
    """
    url = data.url
    scrapper = Scrapper(url)
    content_product = scrapper.analize_content()

    return content_product

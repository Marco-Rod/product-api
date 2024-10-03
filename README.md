Proyecto desarrollado con FastAPI
=================================

Este proyecto es una aplicación de scrapping de productos de un sitio web.

Requisitos
----------

- Python 3.11
- FastAPI
- Requests
- BeautifulSoup
- lxml

Instalación
-----------

1. Clonar el repositorio
2. Entrar al directorio del proyecto
3. Ejecutamos el comando docker build -t fastapi-prodcut-post .
4. Ejecutamos el comando docker run -d --name fastapi-product-container -p 8000:8000 fastapi-product-post
5. Abrimos el navegador y accedemos a la url http://localhost:8000/docs
   

Probando la API /create-product
-------------------------------
Se puede usar Swagger para probar la API. Para ello, abrimos el navegador y accedemos a la url http://localhost:8000/docs
ó con el comando: curl -X 'POST' \
  'http://localhost:8000/create-product' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://www.tiendasjumbo.co/supermercado/despensa/harinas-y-mezclas-para-preparar"
}'
desde una terminal.


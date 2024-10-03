# Dockerfile
# Usamos una imagen base de python
FROM python:3.11-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo requirements.txt
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de la aplicacion dentro del contenedor
COPY ./app /app/app

# Comando para correr la aplicacion con uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

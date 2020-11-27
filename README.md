
# Calculadora sobre microservicios

Servicio que permite resolver operaciones matematicas simples, dado un input con la forma 1+5-6/2*3 y retornando un output con la forma 9+5-6/2*3= 5.
Donde cada operación básica aritmetica corresponde a un microservicio

### Pre-requisitos 📋

_Estas herramientas son necesarias para instalar el software_

-Instalar [git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git)

-Instalar [docker]( https://docs.docker.com/get-docker/) y [docker compose](https://docs.docker.com/compose/gettingstarted/) 

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

1- Clonar el repositorio en su totalidad en caso de quieras verificar código, mejorar el desarrollo, sumar nuevas funcionalidades o simplemente probar. 

``` 
git@github.com:Marbex4x4/test_calculator.git
```
  
4- Desde la consola y parado en la carpeta raíz, ejecuta el comando _docker-compose.yml_ en caso de que solo desees de manera rápida iniciar / apagar la totalidad de los servicios contemplando los microservicios satelites que dan vida a las operaciones aritmeticas.

3- En este punto tendrás el servicio levantado localmente en el puerto 8080.
   
   Esta linea de comando te permitirá, descargar las imagenes de cada uno de los servicios, así como el iniciar la ejecución de los mismos. En este punto tendrás todos los servicios ejecutandose en los puertos correspondientes.  
    ``` docker-compose up``` 
    
   Si deseas validar la ejecución de los servicios, utiliza: 
    ``` docker-compose ps``` 
    
   Si deseas apagar la ejecución de todos los servicio activos, utiliza:
    ``` docker-compose down``` 
    

## Probemos el desarrollo ⚙️

_Con estas instrucciones podrás probar los servicio que exitosamente has levantado_

### Endpoint 🔩

_/calculate_ : Te permite resolver operaciones matematicas simples.

```
Method: POST
URL: {URL_BASE}/calculate
Headers: 
  Content-Type: application/json
```

Payload:
```
{"data":"3 X 4 + 4 / 2"}
```

Comando para prueba con curl:
```
curl -d '{"data":"3 X 4 + 4 / 2"}' -H "Content-Type: application/json" -X POST "http://0.0.0.0:8080/calculate
```

## Construido con 🛠️

_Herramientas utilizas para la creación del proyecto_
* [python3.8.3](https://www.python.org/downloads/release/python-383/) - Lenguaje usado (imagen base :python:3.8.3-slim-buster)
* [flask](https://flask.palletsprojects.com/en/1.1.x/) - Framework web usado
* [rabbitMQ](https://www.rabbitmq.com/) - Comunicación asincrónica basada en evento

## Versionado 📌

Se utilizó [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/Marbex4x4/test_calculator/tags).

## Autores ✒️

* **Marbely Graterol** - *Trabajo Inicial* - [Marbex4x4](https://github.com/Marbex4x4)

## Test dev Seguros Falabella 🎁

* [test](https://github.com/JosephCastro/Katas/blob/master/Calculadora.md)



---
😊

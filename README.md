<h1 align="center">Hunti</h1>

## 📝 Tabla de Contenido

- [Sobre](#about)
- [Comenzando](#getting_started)
- [Desplegar](#deployment)
- [Construido Con](#built_using)

## 🧐 Sobre <a name = "about"></a>

Hunti es un bot de Twitter creado para hacer capturas a las publicaciones

## 🏁 Comenzando <a name = "getting_started"></a>

Intrucciones para crear el entorno y ejecutar a Hunti en su máquina local

### Prerrequisitos

- Linux
- Python (3.8.10)
- Tener [cuenta de desarrolldor](https://developer.twitter.com/en/portal/dashboard) en Twitter

### Instalando

Clonar repositorio

```
git clone git@github.com:raulodev/hunti.git
```

Acceder al directorio , crear y activar entorno virtual

```
cd hunti/
python3 -m venv .venv
source .venv/bin/activate
```

instalar dependencias de python.

```
pip3 install -r requirements.txt
```

instalar dependencias de shot-scraper.

```
shot-scraper install
```

Otorgar permisos de ejecución a los script.

```
chmod +x ./run.sh
chmod +x ./server/run.sh
chmod +x ./client/run.sh
```

Cargar variables de entorno.

`CONSUMER_KEY` ,
`CONSUMER_SECRET` ,

`ACCESS_TOKEN` ,
`ACCESS_TOKEN_SECRET` ,

`BEARER_TOKEN`

Paso final lanzar aplicación

```
./run.sh
```

## 🚀 Desplegar <a name = "deployment"></a>

El despliegue se hará en un vps con Ubuntu 20.04 y Docker

### Prerrequisitos

- Docker
- vps con Ununtu 20.04

Clonar repositorio

```
git clone git@github.com:raulodev/hunti.git
```

Acceder al proyecto

```
cd hunti/
```

Otorgar permisos de ejecución a los script dentro del vps

```
$ chmod +x ./run.sh
$ chmod +x ./server/run.sh
$ chmod +x ./client/run.sh
```

Crear imagen docker

```
docker build -t hunti-image .
```

Paso final lanzar contenedor docker

```
docker run -d -m="200mb" --restart always --name hunti -v `pwd`:/`pwd` -w `pwd`  -it hunti-image
```

## ⛏️ Construido con <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/)
- [Jquery](https://jquery.com/)
- [Tailwindcss](https://tailwindcss.com/)
- Tweepy

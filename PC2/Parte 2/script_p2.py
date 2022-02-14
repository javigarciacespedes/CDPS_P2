import os
import sys


### Definición del fichero Dockerfile ###
os.chdir('practica_creativa2/bookinfo/src/productpage')

### Generación del Fichero Dockerfile automatizado ###
f1 = open("Dockerfile","w")
f1.write("FROM python:3.7.7-slim \n")
f1.write("\n")

f1.write("WORKDIR /practica_creativa2/bookinfo/src/productpage \n")
f1.write("\n")

f1.write("COPY requirements.txt . ./ \n")
f1.write("\n")

f1.write("COPY productpage_monolith.py . ./ \n")
f1.write("\n")

f1.write("COPY templates/index.html . ./templates/ \n")
f1.write("\n")

f1.write("COPY templates/productpage.html . ./templates/ \n")
f1.write("\n")

f1.write("ENV GROUP_NUMBER - 'Equipo 16' \n")

f1.write("RUN apt-get update \n")

f1.write("RUN apt-get -y install python3 \n")

f1.write("RUN apt-get -y install python3-pip \n")

f1.write("RUN pip3 install -r requirements.txt \n")

f1.write("EXPOSE 9080 \n")

f1.write('CMD  ["python3","productpage_monolith.py","9080" ]\n')
f1.close()

### Fin del Fichero Dockerfile ###

### Comandos para el despliegue del contenedor Docker ###
    ## Para ejecutar en el navegador : IPexterna/productpage ##

os.system("sudo docker build -t 'g16/product-page' .")
os.system("sudo docker run --name g16-product-page -p 80:9080 -e GROUP_NUMBER=16 -d g16/product-page")

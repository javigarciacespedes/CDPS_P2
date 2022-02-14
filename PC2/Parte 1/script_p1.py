import sys
import os

###Descarga del repositorio ###
os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")
os.chdir('practica_creativa2/bookinfo/src/productpage')

### Asignación de la variable global ###
os.environ['GROUP_NUMBER'] = 'Equipo 16'

### Instalación del pip3 ###
os.system("pip3 install -r requirements.txt") 

### Edicion del archivo HTML y asignación de la variable global GROUP_NUMBER ###
    ## Busqueda de la variable grupal y asignación del número de grupo ##

fin = open("templates/productpage.html", "r")
fin2 = open("group.html","w")
for line in fin:
    if '''{% block title %}Simple Bookstore App{% endblock %}''' in line:
        fin2.write('''{% block title %}'''+ os.environ['GROUP_NUMBER'] + '''{% endblock %}''')
    else:
        fin2.write(line)

fin2.close()
fin.close()
            
### Escritura en la web de product page ###
fin3 = open("group.html","r")
fin4 = open("templates/productpage.html","w")

for line in fin3:
    fin4.write(line)
fin3.close()
fin4.close()

os.system("rm group.html")

### Instalación del entorno de las máquinas virtuales pesadas ###
    ## Para ejecutar en el navegador : IPexterna:9080/productpage ##

os.system("python3 productpage_monolith.py 9080")


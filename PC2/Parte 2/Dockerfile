FROM python:3.7.7-slim

WORKDIR /practica_creativa2/bookinfo/src/productpage
COPY requirements.txt . ./
COPY productpage_monolyth.py . ./
COPY templates/productpage.html . /templates/
COPY templates/index.html . /templates/

ENV GROUP_NUMBER = "Equipo 16"
RUN apt-get update
RUN apt-get -y install python3 
RUN apt-get -y install python3-pip 
RUN pip3 install -r requirements.txt 

EXPOSE 9080
CMD ["python3","productpage_monolith.py","9080"]



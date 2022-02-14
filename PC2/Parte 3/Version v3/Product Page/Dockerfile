FROM python:3.7.7-slim
WORKDIR /practica_creativa2/bookinfo/src/productpage/
COPY requirements.txt . ./
COPY templates/productpage.html . /templates/
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install -r requirements.txt
ENV GROUP_NUMBER 16
EXPOSE 9080
CMD ["python3","productpage.py", "9080"]

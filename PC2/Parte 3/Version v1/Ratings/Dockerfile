FROM node:12.18.1-slim
WORKDIR /opt/microservices
COPY package.json . /opt/microservices/
COPY ratings.js . /opt/microservices/
RUN npm install
ENV SERVICE_VERSION v1
EXPOSE 9080
CMD ["node","ratings.js","9080"]


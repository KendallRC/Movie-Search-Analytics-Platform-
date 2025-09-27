docker login

cd docker/api/

docker build -t favargasc/app:latest .

sudo docker push favargasc/app:latest

cd ../prometheus

docker build -t favargasc/prometheus:latest .

sudo docker push favargasc/prometheus:latest
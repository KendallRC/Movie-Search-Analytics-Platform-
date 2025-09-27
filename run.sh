# ./build.sh

cd charts/

helm upgrade --install application application

helm upgrade --install observability observability
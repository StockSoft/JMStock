sudo docker build -t web_stock .
sudo docker stop web_stock
sudo docker rm web_stock
sudo docker run -d --name web_stock -p 80:80 --link mongo:mongo web_stock python manage.py runserver 0.0.0.0:80
sudo docker ps

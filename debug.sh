sudo docker stop web_stock
sudo docker rm web_stock
sudo docker run -it --name web_stock -p 80:80 --link mongo:mongo web_stock /bin/bash

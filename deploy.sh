#!/usr/bin/env bash
echo "> Gongbae Editor 배포"
sudo su
cd /home/ec2-user/prod-back
chmod +x ./deploy.sh
python3 manage.py makemigrations wc
python3 manage.py migrate
docker build -t cuu2253/deform-gongbae-editor-back:latest .
docker compose up -d
systemctl restart nginx

# npm -v
# npm install next@latest
# pm2 delete phymmr
# pm2 start "npx next start" --name phymmr
### connect to droplet digital ocean for updating

```
ssh u_shortly@165.227.119.154
```

```
source bin/activate

cd short.ly

git pull origin master

python manage.py collectstatic

python manage.py migrate

sudo supervisorctl restart shortly

exit
```

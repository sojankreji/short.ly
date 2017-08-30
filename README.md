### short.ly

#### run project
```
python manage.py runserver
```


### configure postgres db
```
su - postgres
createuser u_shortly
createdb shortly_prod --owner u_shortly
psql -c "ALTER USER u_shortly WITH PASSWORD '123'"
```


### deploy to digital ocean
[Deploy a Django App on Digital Ocean](https://simpleisbetterthancomplex.com/tutorial/2016/10/14/how-to-deploy-to-digital-ocean.html)

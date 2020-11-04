from django.test import TestCase

# Create your tests here.


#ver esse código
#https://github.com/matheusbattisti/horadecodar-django-youtube




#https://www.geeksforgeeks.org/textfield-django-models/
#https://realpython.com/django-redirects/#passing-parameters-with-redirects
#https://www.w3schools.com/css/css_table.asp

#pip3 install django-crispy-forms

#Zerar senha do admin
#python manage.py shell
#from django.contrib.auth.models import User
#User.objects.filter(is_superuser=True)

#usr = User.objects.get(username='nome-do-administrador')
#usr.set_password('nova-senha')
#usr.save()



'''Upload documents on Github
git clone <nome>
<entra na pasta criada>
git add .
git commit -m "texto"
git push
git pull
'''

'''git checkout -b nome cria uma branch
git checkout nome entra na branch
git branch - verifica as branchs
git checkout master - entra na master
git merge origin "nome" 
git push origin master - subir commit
git branch -D "nome"- deletar branch
'''



#Heroku
#https://github.com/Gpzim98/django-heroku

#git add .gitignore
#colocar no gitignore

'''.idea
.pyc
.DS_Store
*.sqlite3'''

'''
Publishing the app
git add .
git commit -m "Configuring the app"
git push heroku master --force
'''








#VENV
""" 
Instalar Python
pip install virtualenv
pip install django

#MAC / Linux
source venv/bin/activate

#Windows
source venv/Scripts/activate   == ou   
Se não pegar a venv, abrir Windows PowerShell com adminitrador:

Set-ExecutionPolicy Unrestricted
S ou A >> depois:

.\activate


 """
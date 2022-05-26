# Minha primeira aplicação utilizando o framework Django

Comandos Django e comandos CMD usados: 

python -m pip install django

cmd code .

import django

python -m venv env (nome da pasta) <- Criar ambiente virtual

dir <- listar conteúdo da pasta

env\Scripts\activate <- abrir ambiente virtual

cd ../.. <- recuo pastas

Criar projeto

django-admin startproject mysite

instalar django <- pip install (instalar - unistall desinstalar) django

atualizar -m pip install --upgrade pip

django-admin startproject mysite . <- criar na pasta especificada

cd mysite

python manage.py startapp core

python manage.py makemigrations 

python manage.py migrate -> fazer a migração

python manage.py shell <- usar a tabela | 

exit() <- sair do console interativo

python manage.py runserver <- levantar servidor

Já esperado ter Python 3.8 instalado na máquina.

Preparando ambiente

Instalar ambiente virtual caso não tenha: pip install virtualenv

Criar ambiente virtual: python3 virtualenv (nome do ambiente virtual)

Iniciar ambiente virtual: venv\Scripts\activate

Instalar dependências: pip install -r requirements.txt

Criar migrações: python manage.py makemigrations

Sincronizar migrações: python manage.py migrate

Criar superusuário: python manage.py createsuperuser

Iniciar servidor: python manage.py runserver

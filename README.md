# Sistema de hotelaria - Django

---

## Comandos inicias:

Para criar um ambiente virtual:

```powershell
python -m venv venv
```

---

Ativar o ambiente virtual: 

```powershell
venv\Scripts\Activate.ps1
```

---

Instalação do Django:

```powershell
pip install django pillow
```

---

Criação do projeto Django:

```powershell
django-admin startproject nome_do_projeto
cd nome_do_projeto
```

---

Rodar servidor Django:

```powershell
python manage.py runserver
```

---

Para iniciar app dentro do Django:

```powershell
django-admin startapp nome_do_projeto
cd nome_do_projeto
```

---

### Configuração dentro do projeto:

E adicione o app em `INSTALLED_APPS:`

```powershell
INSTALLED_APPS = [
    # apps nativos
    'django.contrib.admin',
    'django.contrib.auth',
    # ...
    
    # o app
    'nome_do_app',
]
```

---

### Criação das pastas:

Dentro da raiz do projeto (onde está o `manege.py`) rode:

```powershell
mkdir templates
mkdir static
mkdir media
```

Também é possível separar por tipo no `static:`

```powershell
mkdir static\css
mkdir static\js
mkdir static\img

```

---

### `Static` files

No final do `settings.py`, adiciona:

```powershell
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # pasta onde seus arquivos estão durante o dev
STATIC_ROOT = BASE_DIR / 'staticfiles'    # usado quando rodar collectstatic
```

### Media Files

```powershell
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

Será necessário adicionar isso no final do arquivo:

```powershell
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # suas urls aqui
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### Configurar o `settings.py`

Abra o arquivo: 

```powershell
code .\nome_do_projeto\settings.py
```

Você pode editar ou simplesmente adicionar:

```powershell
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # <- adiciona essa linha
        'APP_DIRS': True,
        ...
    },
]
```

---

Criar e aplicar as migrações do banco de dados:

```powershell
python manage.py makemigrations
python manage.py migrate
```

---

Criar super usuário para acessar o adm:

```powershell
python manage.py createsuperuser
```

Vai pedir o username, email e senha. Depois disso, você consegue logar em:

http://127.0.0.1:8000/admin

---

Rodar servidor: 

```powershell
python manage.py runserver
```

---

Usar no HTML:

Para carregar arquivos estáticos:

```powershell
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

Para imagens enviadas:

```powershell
<img src="{{ objeto.imagem.url }}" alt="Imagem">
```

---

# ACESSOS

## Acesso ADMINISTRADOR:

- O Administrador é responsável por gerenciar o sistema. Ele tem permissão para criar os grupos **GERENTE** e **ATENDENTE**, definir suas respectivas permissões e cadastrar novos usuários. Além disso, o Administrador tem total acesso aos **Quartos**, podendo **criar, editar e excluir** conforme necessário.

USUÁRIO

```less
Carlos01
```

SENHA

```less
admin123
```

---

## Acesso GERENTE:

- O GERENTE é capaz de cadastrar novos quartos, cadastrar novos colaboradores(atendentes), visualizar a lista de todos os quartos cadastrados e realizar reservas para os hóspedes.

USUÁRIO

```less
Carlos01
```

SENHA

```less
admin123
```

---

## Acesso ATENDENTE:

- O ATENDENTE é capaz de visualizar a lista de quartos disponíveis e realizar reservas para os hóspedes, o atendente não pode acessar funcionalidades que são exclusivas para GERENTE.

USUÁRIO E SENHA

- De acordo com os dados que o GERENTE cadastrar o ATENDENTE


# DESENVOLVEDORES:

- Pedro Ribeiro
- João Gabriel Pincinato
- Isadora da Silva
- Leonardo Felix
- Daniel Augusto Batista
- Marcos Néfi

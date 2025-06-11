from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import *


# Create your views here.
def Homepage(request):
    context = {}
    dados_home = homepage.objects.all()
    context['dados_home'] = dados_home
    return render(request, 'homepage.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        
        else:
            context = {
                "alerta" : "Usuário ou Senha Invalida"
            }
            return render(request, 'Login.html', context)

    else:
        return render(request, 'Login.html')
    
    
@login_required(login_url='/') 
def addQuarto(request):
    if request.method == 'POST':
        numero_quarto = request.POST.get('num_Quarto')
        form = quartoForms(request.POST, request.FILES)

        if form.is_valid():
            if quarto.objects.filter(num_Quarto=numero_quarto).exists():
                messages.error(request, "Já existe um quarto cadastrado com esse número")
            else:
                form.save()
                messages.success(request, "Quarto cadastrado com sucesso!")
                return redirect('listar_quartin')
    else:
        form = quartoForms()

    context = {'form': form}
    return render(request, 'addQuartos.html', context)

    
@login_required(login_url='/') 
def addColabo(request):
    if request.method == 'POST':
        form = AtendenteForms(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user.groups.clear()
            grupo = Group.objects.get(name='Atendente')
            user.groups.add(grupo)

            messages.success(request, 'Atendente cadastrado com sucesso!')
            return redirect('addColabo')
    else:
        form = AtendenteForms()
    return render(request, 'addColabos.html', {'form': form})

@login_required(login_url='/')  
def reserva(request):
    hoje = date.today()
    
    quartos = quarto.objects.all()
    
    listar_quartos = []

    for quart in quartos:
        ativo = hospede.objects.filter(quarto=quart, data_final__gte=hoje)
        if ativo.exists():   
            quart.status = 'RESERVADO'
        else:
            quart.status = 'DISPONIVEL'
        quart.save()
        listar_quartos.append((quart, quart.status, ativo))
    return render(request, 'reservas.html', {'listar_quartos': listar_quartos})

@login_required(login_url='/')
def listar_quartin(request, tipo=None):

    if tipo: 
        quartin = quarto.objects.filter(tipo=tipo)
    else:
        quartin = quarto.objects.all()

    context = {
        'quartos': quartin,
        'tipo_selecionado': tipo,
    }

    return render(request, 'listar_quartin.html', context)

@login_required(login_url='/')
def editar_quartin(request, id):
    quarto_editar = quarto.objects.get(id=id)

    if request.method == 'POST':

        # Cria um forms com os dados enviados
        # Editar o 'quarto_editar' existente (instance=)
        form = quartoForms(request.POST, request.FILES, instance=quarto_editar)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Editado com sucesso!')
            return redirect('listar_quartin')
    else:
        # Vai criar o form preenchido com os dados do quarto
        form = quartoForms(instance=quarto_editar)

    return render(request, 'editar_quartin.html', {'form': form})


@login_required(login_url='/')
def addHospede(request, id):
    quarto_get = quarto.objects.get(id=id)
    
    if request.method == 'POST':
        form = HospedeForms(request.POST)
        if form.is_valid():
            new_hospede = form.save(commit=False)
            new_hospede.quarto = quarto_get

            mesma_data = hospede.objects.filter(
                quarto=quarto_get,
                data_inicio__lte=new_hospede.data_final, # menor ou igual a
                data_final__gte=new_hospede.data_inicio # maior ou igual a
            ).exists()
            
            if mesma_data:
                messages.error(request, 'Esta data já está em uso!')
            else:
                new_hospede.save()
                messages.success(request, 'Hospede Cadastrado com sucesso')
                return redirect('reserva')
    else:
        form = HospedeForms()

    return render(request, 'addHospede.html', {'form': form})

def Sair(request):
    logout(request)
    return redirect ('homepage')    


# EXEMPLO DE INSTANCE= (stackoverflow)

# >>> author = Author.objects.get(name='Mike Royko')
# >>> formset = BookFormSet(instance=author)
# Editando um livro de um autor em especifico
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import PhoneBook
from .forms import CreateUserForm, AddUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from datetime import datetime, timedelta



def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Аккаунт был создан для ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'main/register.html',context)



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            messages.info(request, 'Логин или пароль не верны')
            

    context = {}
    return render(request, 'main/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def createUser(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        

    form = AddUserForm()
    form_1 = {
        'form': form
    }
    return render(request, 'main/create.html', form_1)
 
 


# @login_required(login_url='login')
def object_list(request):
    '''Функция object_list возвращает HTML страницу телефонного справочника с пагинацие и строкой поиска '''

    query = request.GET.get('text1')
    query_1 = request.GET.get('text2')
    query_2 = request.GET.get('text3')
    query_3 = request.GET.get('text4')
    query_4 = request.GET.get('text5')


    requester = request.user
    if request.user.role == 'ADM':
        object_list = PhoneBook.objects.all()

    elif request.user.role == 'MNG':
        object_list = PhoneBook.objects.filter(city=requester.country)

    else:
        object_list = PhoneBook.objects.filter(owner=requester)

    
    if query or query_1 or query_2 or query_3 or query_4:
        object_list = PhoneBook.objects.filter(
            Q(first_name__icontains=query), Q(last_name__icontains=query_1), Q(phone_number__icontains=query_2), Q(age__icontains=query_3), Q(city__icontains=query_4)).distinct()
    paginator = Paginator(object_list, 10) 
    page = request.GET.get('page')

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    context = {
        'data': data,
        
    }
    return render(request, "main/index.html", context)




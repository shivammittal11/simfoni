from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from user import forms
from user.forms import UpdateUserSecondaryForm, UpdateUserPrimaryForm
from user.models import ProductData, User
from user.serializer import ProductSerializer, UserSerializer


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'launchar.html', {'success': 1})
        else:
            login(request, user)
            return redirect('/home/')
    else:
        return render(request, 'launchar.html')


def user_signup(request):
    if request.method == 'POST':
        user_form = forms.UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return redirect('/user/message/')
    else:
        user_form = forms.UserCreationForm()
    return render(request, 'signup.html',
                  {
                      'user_form': user_form,
                      'error': user_form.errors,
                      'success': True
                  }
                  )


def message(request):
    return render(request, 'message.html')


@login_required
def home(request):
    if request.method == 'POST':
        if 'primary' in request.POST:
            user_form = UpdateUserPrimaryForm(request.POST, instance=request.user)
            print('user_form', user_form)
            user = user_form.save()
        elif 'secondary' in request.POST:
            user_form = UpdateUserSecondaryForm(request.POST, instance=request.user)
            user = user_form.save()
        else:
            name = request.POST.get('name')
            ProductData.objects.create(user=request.user, name=name)
        return redirect('/home/')
    else:
        if request.user.is_staff:
            supplier_list = User.objects.filter(is_staff=False)
            serializer = UserSerializer(supplier_list, many=True)
            return render(request, 'admin.html',
                          {'supplier_list': serializer.data
                           })
        else:
            product_queryset = ProductData.objects.filter(user=request.user)
            product_serializer = ProductSerializer(product_queryset, many=True)
            return render(request, 'home.html',
                      {'product_list': product_serializer.data
                       })


def search_supplier(request):
    name = request.GET.get('name')
    user_queryset = User.objects.filter(Q(supplier_business_name__icontains=name, is_staff=False) | Q(username__icontains=name, is_staff=False) | Q(supplier_address__icontains=name, is_staff=False))
    serializer = UserSerializer(user_queryset, many=True)
    return render(request, 'search.html',
                  {'supplier_list': serializer.data
                   })


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
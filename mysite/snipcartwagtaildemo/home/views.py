from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Product
from django.urls import reverse



def canjear(request, page_ptr_id):
    producto = get_object_or_404(Product, pk=page_ptr_id)

    # Se resta el saldo del usuario
    """ user_profile, created = UserProfile.objects.get_or_create(
        user_id=request.user.pk
    )
    user_profile.valor_market_balance =- home.models.Product.price
    user_profile.save() """

    saldoActual = int(request.session['saldo'])
    
    if (saldoActual >= producto.price):
        saldoActual = int(saldoActual - producto.price)

        request.session['saldo'] = str(saldoActual)
        request.session['canjeado'] = True
    else:
        request.session['canjeado'] = False
        
    request.session['alert'] = 0
        
    

    new_port='8080'
    hostname = request.get_host().split(':')[0]
    url = 'http://' + hostname + ':' + new_port + '/'
    return redirect(url)


    #return HttpResponseRedirect(reverse('polls:results', args=(page_ptr_id,)))
    

def guardar_saldo(request, id, saldo):
    request.session['saldo'] = saldo
    request.session['id'] = id
    new_port='8080'
    hostname = request.get_host().split(':')[0]
    url = 'http://' + hostname + ':' + new_port + '/'
    return redirect(url)

def home(request):
    request.session['alert'] = 1
    saldo = request.session['saldo']
    saldo_str = str(saldo)
    user_id = request.session['id']
    id_str = str(user_id)
    new_port='8000'
    hostname = request.get_host().split(':')[0]
    url = 'http://' + hostname + ':' + new_port + '/saldo/' + id_str + '/' + saldo_str + '/'
    return redirect(url)




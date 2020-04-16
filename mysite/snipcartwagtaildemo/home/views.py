from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import home.models
from django.urls import reverse



def canjear(request, page_ptr_id):
    producto = get_object_or_404(home.models.Product, pk=page_ptr_id)

    # Se resta el saldo del usuario
    user_profile, created = UserProfile.objects.get_or_create(
        user_id=request.user.pk
    )
    user_profile.valor_market_balance =- home.models.Product.price
    user_profile.save()

    return HttpResponseRedirect(reverse('polls:results', args=(page_ptr_id,)))


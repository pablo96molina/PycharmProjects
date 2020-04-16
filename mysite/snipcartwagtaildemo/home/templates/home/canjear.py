from django.shortcuts import HttpResponse

def canjear(request,id):
    idproducto=id
    monto = ("%s", idproducto)
    print('%s',idproducto)
    return HttpResponse(monto)

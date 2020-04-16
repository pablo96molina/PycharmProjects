def canjear(request, question_id):
    producto = get_object_or_404(Product, pk=page_ptr_id)

        # Se resta el saldo del usuario
       user_profile, created = UserProfile.objects.get_or_create(
           user_id=request.user.pk
       )
       user_profile.valor_market_balance =- product.price
            question.ValorMarket
        user_profile.save()

    return HttpResponseRedirect(reverse('polls:results', args=(page_ptr_id,)))


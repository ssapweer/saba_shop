from django.shortcuts import render
from .models import Promotion

def promotion_list(request):
    promotions = Promotion.objects.all()
    return render(request, 'feedback/promotions.html', {'promotions': promotions})
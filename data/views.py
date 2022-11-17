from django.shortcuts import render
from .models import Country

# Create your views here.
def data(request):
    data = Country.objects.all()
    context = {'data': data}
    return render(request, 'data.html', context)
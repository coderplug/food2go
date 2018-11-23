from django.shortcuts import render
from django.views import generic

def custom_400_view(request):
    return render(request, 'errors/400.html')
    
def custom_403_view(request):
    return render(request, 'errors/403.html')

def custom_404_view(request):
    return render(request, 'errors/404.html')

def custom_500_view(request):
    return render(request, 'errors/500.html')

class IndexView(generic.TemplateView):
    template_name = 'food2go/index.html'
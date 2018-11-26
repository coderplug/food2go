from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

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

def loging(request):
    pass

def logout(request):
    pass

def signup(request):
    #Only at POST request (when we change information)
    if request.method == 'POST':
        #Form is created
        form = SignUpForm(request.POST)
        #Checks if information is valid (no empty fields, right values)
        if form.is_valid():
            #Saves to database
            form.save()
            #is_valid fills cleaned_data values as validated (dictionary)
            #Logging user in:
            #---START---
            username = form.cleaned_data.get('username')
            #password1 is first password field value (not hashed)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #---END---
            return redirect('/')
    else:
        #If not POST, just return form
        form = SignUpForm()
    return render(request, 'food2go/signup.html', {'form': form})
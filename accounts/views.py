from django.urls import reverse_lazy
from django.views import generic

from .forms import SignUpForm
# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    #Only at POST request (when we change information)
    """
    if self.request.method == 'POST':
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
    """
    
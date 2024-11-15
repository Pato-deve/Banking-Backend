from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Customer
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

@login_required
def customer_detail(request):
    customer = get_object_or_404(Customer, user=request.user)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'customers/register.html', {'form': form})

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('home')

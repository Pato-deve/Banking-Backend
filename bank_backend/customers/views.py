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

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

    def get_object(self):
        return get_object_or_404(Customer, pk=self.kwargs['pk'], user=self.request.user)

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

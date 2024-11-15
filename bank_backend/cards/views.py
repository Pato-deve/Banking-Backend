from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Card
from .forms import CardForm

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = 'cards/card_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        return Card.objects.filter(customer__user=self.request.user)

class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = 'cards/card_detail.html'
    context_object_name = 'card'

@login_required
def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.customer = request.user.customer
            card.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'cards/card_form.html', {'form': form})

@login_required
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk, customer__user=request.user)
    card.delete()
    return redirect('card_list')
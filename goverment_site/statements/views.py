
# Create your views here.
from . import models
from django.views.generic import ListView, TemplateView,DetailView,CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import StatementForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context

class StatementListView(ListView):
    model = models.Statement
    context_object_name = 'statements'


class StatementDetailView(DetailView):
    model = models.Statement
    context_object_name = 'statement_detail'

class StatementCreateView(CreateView, LoginRequiredMixin):
   #ver. bez formsow
   # model = models.Statement
   #fields = ('title', 'text')
    model = models.Statement
    login_url = '/login/'
    redirect_field_name = 'gover/statement_detail.html'
    form_class = StatementForm

class StatementUpdateView(UpdateView, LoginRequiredMixin):
   # model = models.Statement
  #  fields = ('title','text')
    model = models.Statement
    login_url = '/login/'
    redirect_field_name = 'gover/statement_detail.html'
    form_class = StatementForm

class StatementDeleteView(DeleteView, LoginRequiredMixin):
    model = models.Statement
    success_url = reverse_lazy("statements:list")

@login_required
def statement_publish(request, pk):
    statement = get_object_or_404(models.Statement, pk=pk)
    statement.publish()
    return redirect('statement_detail', pk=pk)
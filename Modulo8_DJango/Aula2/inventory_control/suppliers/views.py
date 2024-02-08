from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import Supplier
from .forms import SupplierForm
# Importando as views genéricas
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier #Modelo onde a classe vai buscar os dados
    template_name = "suppliers/index.html" #Template que a classe vai usar
    paginate_by = 100 #Incluindo quantos itens por página
    ordering = "-id" #Ordenando os itens pelo id
    
class SupplierSearchView(LoginRequiredMixin, ListView):
    model = Supplier #Modelo onde a classe vai buscar os dados
    template_name = "suppliers/index.html" #Template que a classe vai usar
    paginate_by = 1 #Incluindo quantos itens por página
      
    #O que vai ser retornado - Filtrado
    def get_queryset(self):
        search_value = self.request.GET.get("q").strip()
        
        if not search_value:
            return Supplier.objects.all().order_by("-id")
        
        return Supplier.objects.filter(Q(fantasy_name__icontains=search_value) |
                                        Q(company_name__icontains=search_value)).order_by("-id")
        
class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = "suppliers/create.html"
    form_class = SupplierForm
    success_url = reverse_lazy("suppliers:index")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        messages.success(self.request, "Fornecedor cadastrado com sucesso!")
        
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        
        messages.error(self.request, "Erro ao cadastrar o fornecedor!")
        
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_action"] = reverse("suppliers:create")
        return context
    

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = "suppliers/update.html"
    form_class = SupplierForm
    success_url = reverse_lazy("suppliers:index")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        
        messages.success(self.request, "Fornecedor atualizado com sucesso!")
        
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        
        messages.error(self.request, "Erro ao atualizar o fornecedor!")
        
        return response
    
class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier #Modelo onde a classe vai buscar os dados
    success_url = reverse_lazy("suppliers:index")

@require_POST
def delete(request, id):
    supplier = get_object_or_404(Supplier, pk=id)
    supplier.delete()
    
    return redirect("suppliers:index")

@require_POST
def toggle_enabled(request, id):
    supplier = get_object_or_404(Supplier, pk=id)
    
    supplier.enabled = not supplier.enabled
    supplier.save()
    
    return JsonResponse({ "message": "success" })
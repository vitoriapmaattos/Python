from django.contrib import admin
from .models import Supplier

# Register your models here.
@admin.register(Supplier)
class SupplierAdmin (admin.ModelAdmin):
    list_display = ["id", "company_name", "fantasy_name", "email", "enabled"] #Modifica o que aparece na tabela no admin
    exclude = ["slug"] #Exclui os itens da tela de cadastro do Admin
    ordering = ["-id"] #Modificar a ordenação do itens de forma decrescente
    list_filter = ["enabled", "created_at"] #Filtro
    search_fields = ["company_name", "email"] #Incluir critérios de pesquisa
    list_display_links = ["company_name"] #Link para página de detalhes
    list_editable = ["fantasy_name", "enabled"] #Possibilita a edição
    list_per_page = 100 #Quantos itens por página 
    list_max_show_all = 1000
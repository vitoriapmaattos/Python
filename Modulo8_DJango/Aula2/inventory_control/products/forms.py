from django import forms
from .models import Product
import re

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["thumbnail", "slug", "is_perishable"]
        
        labels = {
            "name": "Nome",
            "description": "Descrição",
            "sale_price": "Preço de Venda",
            "expiration_date": "Data de Expiração",
            "photo": "Imagem do Produto",
            "enabled": "Ativo",
            "category": "Categoria"
        }
        
        error_messages = {
            "name": {
                "required": "O campo do nome é obrigatório.",
                "unique": "Já existe um produto cadastrado com esse nome."
            },
            
            "description": {
                "required": "O campo de descrição é obrigatório."
            },
            
            "sales_price": {
                "required": "O campo de descrição é obrigatório."
            },            
        }
        
        widgets = {
            "expiration_date": forms.DateInput(attrs={"type":"date"}, format="%y-%m-%d")
        }

    
from . import views
from django.urls import path

urlpatterns = [
    path("",  views.index, name="index"),
    # Parametro para a rota: Se fosse nome do cliente: <str:client_name>
    # localhost:8000/1 -> Id do cliente -> Cliente 1
    path("<int:client_id>/", views.detail, name="detail"),
    path("cadastro/", views.create, name="create"),
    path("<int:client_id>/editar", views.update, name="update"),
    path("<int:client_id>/remover", views.delete, name="delete"),
]
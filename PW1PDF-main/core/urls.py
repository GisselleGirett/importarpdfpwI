from django.urls import path
from . import views

urlpatterns = [
    path('importar-pdf/', views.importar_pdf, name='importar_pdf'),
    path('import-success/', views.import_success, name='import_success'),
    path('select_pdf/', views.filtrar_materias, name='filtrar_materias'),
    path('filtrar_materias/', views.filtrar_materias, name='filtrar_materias'),
    path('mostrar_pdf/', views.mostrar_pdf, name='mostrar_pdf'),
]


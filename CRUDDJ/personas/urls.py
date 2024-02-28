from django.urls import path
from . import views


urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('registrar_persona/',views.registrar_persona,name='registrar_persona'),
    path('listar_personas/',views.listar_personas,name='listar_personas'),
    path('eliminar_persona/<str:id>',views.eliminar_persona,name='eliminar_persona'),
    path('pre_editar_persona/<str:id>',views.pre_editar_persona,name='pre_editar_persona'),
    path('actualizar_persona/<str:id>',views.actualizar_persona,name='actualizar_persona'),
]
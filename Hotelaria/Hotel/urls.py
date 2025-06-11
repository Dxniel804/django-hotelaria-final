from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Homepage, name='homepage'),
    path('login', views.Login, name='login'),
    path('logout', views.Sair, name='logout'),
    path('addQuarto', views.addQuarto, name="addQuarto"),
    path('addColabo', views.addColabo, name="addColabo"),
    path('listar_quartin/', views.listar_quartin, name='listar_quartin'),
    path('listar_quartin/<str:tipo>/', views.listar_quartin, name='listar_quartin'),
    path('editar_quartin', views.editar_quartin, name='editar_quartin'),
    path('editar_quartin/<int:id>/', views.editar_quartin, name='editar_quartin'),
    path('reserva', views.reserva, name='reserva'),
    path('addHospede/<int:id>/', views.addHospede, name='addHospede'),
    path('addHospede', views.addHospede, name='addHospede')
    

]
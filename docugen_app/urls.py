
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kompleksen-doklad', views.kompleksen_doklad, name='kompleksen_doklad'),
    # path('okonchatelen-doklad', views.okonchatelen_doklad, name='okonchatelen_doklad'),

]


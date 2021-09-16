from django.urls import path
from . import views
from .views import ProfileObject, ProfileObjectUpdate

app_name = 'app'

urlpatterns = [
   path('', views.index, name='index'),
   path('profile_data/', ProfileObject.as_view()),
   path('profile_update/<int:item_id>', ProfileObjectUpdate.as_view()),
]

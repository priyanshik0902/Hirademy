from django.urls import path
from .views import *

urlpatterns = [
    path('assistant/', AddAssistant.as_view(), name='create--assistant'),
path('assistant/<int:pk>/del/', DeleteAssistant.as_view(), name='delete--assistant'),
path('assistant/<int:pk>/', GetAssistantById.as_view(), name='read--assistant'),
path('assistant/<int:pk>/up/', UpdateAssistant.as_view(), name='update--assistant'),
]
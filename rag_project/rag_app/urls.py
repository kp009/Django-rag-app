from django.urls import path
from .views import rag_view

urlpatterns = [
    path('', rag_view, name='rag_view'),
]

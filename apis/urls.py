from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.TodoView.as_view()),
    path('<int:id>/',views.TodoDetail.as_view())
]
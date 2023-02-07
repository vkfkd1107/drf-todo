from django.contrib import admin
from django.urls import path, include
from todo import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('todo', views.TodoListViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

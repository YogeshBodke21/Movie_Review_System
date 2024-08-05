from django.urls import path
from .views import home, show, delete, update, search,search1

urlpatterns = [
    
    path("h", home, name = "home"),
    path("s", show, name = "show"),
    path("d/<int:pk>", delete, name = "delete"),
    path("u/<int:pk>", update, name = "update"),
    path("search", search, name = "search"),
    path("search1", search1, name = "search1"),

]
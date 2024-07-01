from django.urls import path
from task.views import *
urlpatterns = [
    path("", loginuser , name ="loginuser"),
    path("tasks/", tasks , name ="tasks"),
    path("task/<int:pk>", task , name ="task"),
    path("create/", create , name ="create"),
    path("update/<int:pk>" , update ,name ="update"),
    path("delete/<int:pk>" , delete ,name ="delete"),
    path("logout/", logoutuser , name ="logoutuser"),
    path("register/", register , name ="register"),
]

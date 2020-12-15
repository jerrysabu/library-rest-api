from django.conf.urls import url
from django.conf.urls import include


from . import views

urlpatterns = [
    url('Library/', views.LibraryAPIView.as_view()),

]

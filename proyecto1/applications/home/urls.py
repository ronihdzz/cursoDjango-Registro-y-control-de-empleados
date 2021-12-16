
from django.urls import path
from .  import views
app_name='home_app'

urlpatterns = [
    path('',
        views.Index.as_view(),
        name='index'
        )
]

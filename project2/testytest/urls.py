from django.urls import path
# Импортируем созданное нами представление
from .views import home_view, contact_view, about_view, product_detail_view


urlpatterns = [
    path('home/', home_view, name = 'home'),
    path('contact/', contact_view, name = 'contact'),
    path('about/', about_view, name = 'about'),
    path('det/', product_detail_view, name = 'det'),


]
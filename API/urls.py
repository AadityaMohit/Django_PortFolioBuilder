from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('portfolio_form/', views.portfolio_form, name='portfolio_form'),
    path('template1/', views.template1, name='template1'),
    path('template2/', views.template2, name='template2'),
    path('template3/', views.template3, name='template3'),
    path('collections/', views.collections, name='collections'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

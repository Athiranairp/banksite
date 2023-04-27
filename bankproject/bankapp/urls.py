from django.urls import path
from . import views



urlpatterns = [
    path('', views.base, name='base'),
    path('submission/', views.submission, name='submission'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # # path('home/', views.home_view, name='home'),
    # path('registration/', views.person_create_view, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX

]




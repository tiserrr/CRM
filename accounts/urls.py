from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>', views.customer, name='customer'),

    path('create_order/<int:pk>', views.create_Order, name='create_order'),
    path('update_order/<int:pk>', views.update_Order, name='update_order'),
    path('delete_order/<int:pk>', views.deleteOrder, name='delete_order'),

    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),
        name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_sent.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_resset_form.html'),
        name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_done.html'),
        name='password_reset_complete')
]
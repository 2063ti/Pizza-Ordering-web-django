from django.urls import path
from pizza import cust_views
from django.contrib.auth import views as auth_views

urlpatterns=[

    path('',cust_views.home,name="indux"),
    path('about/',cust_views.about,name="about"),
    path('booking/',cust_views.booking,name="booking"),
    path('services/',cust_views.services,name="services"),
    path('menu/',cust_views.menu,name="menu"),
    path('contact/',cust_views.contact,name="contact"),
    path('registration/',cust_views.registration,name="registration"),
    path('log/',cust_views.log,name="log"),
    path('logout/',cust_views.logout,name="logout"),
    path('forgot/',cust_views.forgot,name="forgot"),
    path('p_view/',cust_views.p_view,name="p_view"),
    path('update_user',cust_views.update_user,name='update_user'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="reset1.html"),name="password_reset_complete"),
    path('product/<int:pk>', cust_views.product, name='product'),
    path('payment_success', cust_views.payment_success, name='payment_success'),
    path('update_info/', cust_views.update_info, name='update_info'),
    path('checkout/', cust_views.checkout, name='checkout'),
    path('contact/',cust_views.contact,name='contact'),
    path('feedback',cust_views.feedback,name='feedback'),


]
from django.urls import path
from FrontEnd import views




urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('tenant_singlepage/<Tname>',views.tenant_singlepage,name="tenant_singlepage"),
    path('property_page/',views.property_page,name="property_page"),
    path('property_singlepage/<int:dataid>',views.property_singlepage,name="property_singlepage"),
    path('blogpage/',views.blogpage,name="blogpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('login_register/',views.login_register,name="login_register"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('UserLogin/',views.UserLogin,name="UserLogin"),
    path('user_Logout/',views.user_Logout,name="user_Logout"),
]
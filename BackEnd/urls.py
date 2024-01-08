from django.urls import path
from BackEnd import views


urlpatterns=[

    path('index/',views.index,name="index"),
    path('admin_loginpage/',views.admin_loginpage,name="admin_loginpage"),
    path('adminLogin/',views.adminLogin,name="adminLogin"),
    path('AdminLogOut/',views.AdminLogOut,name="AdminLogOut"),
    path('add_property/',views.add_property,name="add_property"),
    path('save_property/',views.save_property,name="save_property"),
    path('show_property/',views.show_property,name="show_property"),
    path('editproperty_page/<int:dataid>',views.editproperty_page,name="editproperty_page"),

    path('updateProperty/<int:dataid>', views.updateProperty, name="updateProperty"),

    path('delete_prop/<int:dataid>',views.delete_prop,name="delete_prop"),

    path('add_tenant/',views.add_tenant,name="add_tenant"),
    path('save_tenant/',views.save_tenant,name="save_tenant"),
    path('tenant_details/',views.tenant_details,name="tenant_details"),
    path('edit_tenant/<int:dataid>',views.edit_tenant,name="edit_tenant"),
    path('updatetenants/<int:dataid>',views.updatetenants,name="updatetenants"),
    path('delete_tenants/<int:dataid>',views.delete_tenants,name="delete_tenants"),


]
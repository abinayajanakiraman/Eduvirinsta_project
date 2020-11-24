
from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.login,name="login"),
    path('login/',views.login,name="login"),
    path('superuser/',views.superuser,name="superuser"),
    path('superAdmin/',views.superAdmin,name="superAdmin"),
    path('delete_data/<int:id>/',views.delete_data,name="delete_data"),
    path('<int:id>/',views.update_data,name="update_data"),

    path('student/',views.Student_page,name="student"),
    path('<int:id>/update_stu_data/',views.update_stu_data,name="update_stu_data"),
    path('delete_stu_data/<int:id>',views.delete_stu_data,name="delete_stu_data"),

    path('staff_page/',views.staff_page,name="staff_page"),
    path('<int:id>/update_staff_data/',views.update_staff_data,name="update_staff_data"),
    path('delete_staff_data/<int:id>',views.delete_staff_data,name="delete_staff_data"),

    path('superstaff/',views.superstaff,name="superstaff"),
    #path('delete_mark',views.delete_mark,name='delete_mark'),
    path('<int:id>/update_mark/',views.update_mark,name='update_mark'),

    path("superstud/",views.superstud,name="superstud")
]


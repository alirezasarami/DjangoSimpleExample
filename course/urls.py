from . import views
from django.urls import path , include ,re_path
urlpatterns = [
    path(r'course_list/',views.course_list),
    path(r'departman_list/',views.departman_list),
    re_path(r'course_department/(\d+)/',views.course_department),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path("delete/<int:id>/", views.delete_task, name="delete_task"),
    path("completed/<int:id>/", views.completed_task, name="completed_task"),
    path("edit/<int:id>/", views.edit_task, name="edit_task"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_out/", views.sign_out, name="sign_out"),
]

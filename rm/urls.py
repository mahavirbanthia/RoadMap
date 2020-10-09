from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "RmHome"),
    path("about/",views.about,name = "AboutUs"),
    path("save/<int:id>",views.save,name = "Save"),
    path("saved/",views.saved,name = "Saved"),
    path("course/",views.course,name = "CourseView"),
    path("search/",views.search,name = "search"),
    path("learn_more/<int:id>",views.learn_more,name = "Learn_More"),
    path("display/<str:category>", views.display, name = "Display")

]

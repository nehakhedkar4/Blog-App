from django.urls import path
from blog import views
from django.views.generic import TemplateView

urlpatterns = [  
    path('',TemplateView.as_view(template_name='index.html'),name="index"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('register/',views.user_register,name="register"),
    path('blog_home_page/',views.blog_home_page,name="blog_home_page"),
    path('user_profile/',views.user_profile,name="user_profile"),
    path('<int:id>',views.edit_post,name="edit_post"),
    path('new_post/',views.new_post,name="new_post"),
    path('delete_post/<int:id>',views.delete_post,name="delete_post"),
    # path('undo_post/',views.undo_post,name="undo_post"),
]

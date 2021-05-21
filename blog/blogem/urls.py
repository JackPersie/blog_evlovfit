from django.urls import path
from . import views
app_name = 'blogem'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),

    path('', views.HomeView.as_view(), name='home'),

    path('all/', views.PostsListView.as_view(), name='all_posts'),
    path('posts/new/', views.PostsCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/', views.PostsDetailView.as_view(), name='posts_detail'),
    path('posts/<int:pk>/delete/',
         views.PostsDeleteView.as_view(), name='delete_post'),
    path('posts/<int:pk>/update/',
         views.PostsUpdateView.as_view(), name='update_post'),
    path('posts/<int:pk>/comment', views.add_comment, name='create_comment'),
    # path('comment/<int:pk>/remove',
    #      views.remove_comment, name='delete_comment'),
]

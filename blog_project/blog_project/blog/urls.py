from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path(r'post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path(r'post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    path(r'post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path(r'post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    path(r'comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path(r'post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),


]

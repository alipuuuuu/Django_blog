from django.urls import path
from posts.views import PostDetailView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path("category/<slug:category_slug>/", PostListView.as_view(), name='post_list_by_category'),
]

from django.urls import path
from django.views.decorators.cache import cache_page
from .views import CategoryListAPIView, latest_post_api_view, PostListView, posts_list_view_from_category, search_posts_api_view, PostDetailAPIView

urlpatterns = [
    path('posts/', cache_page(60*1)(PostListView.as_view()), name='posts-url'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail)'),
    path('latest_post/', latest_post_api_view, name='latest-url'),
    path('categories/', cache_page(60*2)(CategoryListAPIView.as_view()), name='categories'),
    path('posts/category/<slug:slug>/', posts_list_view_from_category, name='category-posts'),
    path('search/posts/<str:name>/', cache_page(60*2)(search_posts_api_view), name='search-url'),
]

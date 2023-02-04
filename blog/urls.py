from django.urls import path
from .views import HomePageViews,DetailPageViews,BlogCreateViews,BlogUpdateViews,BlogDeleteView,AboutPageViews
urlpatterns=[
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name='post_delete'),
    path('',HomePageViews.as_view(),name='homes'),
    path('about/',AboutPageViews.as_view(),name='about'),
    path('post/<int:pk>/',DetailPageViews.as_view(),name='post_detail'),
    path('post/new/',BlogCreateViews.as_view(),name='blog_create'),
    path('post/<int:pk>/edit',BlogUpdateViews.as_view(),name='post_edit'),
]
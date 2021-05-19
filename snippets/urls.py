# without using routers
'''
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# for function based views
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]

# for generic class based views
urlpatterns = [
    # snippets url
    path('snippets/', views.SnippetList.as_view(), name="snippet-list"),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name="snippet-detail"),
    # users url
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user-detail"),
    # login and logout url
    path('api-auth/', include('rest_framework.urls')),
    # home url
    path('', views.api_root),
    # highlighted snippet url
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name="snippet-highlight"),


]

urlpatterns = format_suffix_patterns(urlpatterns)
'''


# using routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # login and logout url
    path('api-auth/', include('rest_framework.urls')),
]

from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include
from django.conf.urls import include
"""
urlpatterns = [
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.api_root),
]
"""

##########################################################################################################
"""
# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/',
         views.SnippetList.as_view(),
         name='snippet-list'),
    path('snippets/<int:pk>/',
         views.SnippetDetail.as_view(),
         name='snippet-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail')
])
"""
##########################################################################################################
"""
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
         snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])
"""

########################################################################################################
# becuase we are using viewset


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

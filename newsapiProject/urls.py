from django.urls import include, path

urlpatterns = [
    path('api/', include('news_api.urls')),
]

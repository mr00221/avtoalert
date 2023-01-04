from django.urls import path, include
from . import views
from django.contrib import admin

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Post API",
        default_version='1.0.0',
        description="API documentation of app1"
    ),
    public=True
)

urlpatterns = [
    #path('', views.index, name='index'),
    path('users/', views.users_list),
    path('users/<int:userID>/', views.users_detail),
    path('avti/', views.avti_list),
    path('avti/<int:carID>/', views.avti_detail),
    path('filters/', views.filters_list),
    path('regkode/', views.regkode_list),
    path('regkode/<int:koda>/', views.regkode_detail),
    path('admin/', admin.site.urls),
    path('openapi', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('liveliness', views.liveliness),
    path('readiness', views.readiness)
]


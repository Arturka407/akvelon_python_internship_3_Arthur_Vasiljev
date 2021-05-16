from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Akvelon",
      default_version='v1',
      description="Finance",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="artur_vasiljev99@mail.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/<int:pk>/transactions', views.TransactionViewList.as_view()),
    path('users/<int:pk>/transactionsbydates', views.SumTransactionViewGroupedByDate.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transactions/<int:pk>/', views.TransactionDetail.as_view()),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
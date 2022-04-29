from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='index'),
    path('houses/<int:house_id>/', views.house_details, name='detail'),
    path('houses/create', views.HouseCreate.as_view(), name='houses_create'),
    path('houses/<int:pk>/update',views.HouseUpdate.as_view(), name='houses_update'),
    path('houses/<int:pk>/delete',views.HouseDelete.as_view(), name='houses_delete'),
    path('houses/<int:house_id>/add_housespace/', views.add_housespace, name='add_housespace'),
    path('features/', views.FeatureList.as_view(), name='features_index'),
    path('features/<int:pk>/', views.FeatureDetail.as_view(), name='features_detail')
]

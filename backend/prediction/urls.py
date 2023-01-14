app_name = 'prediction'

from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("<int:districtid>/", views.predict_info),
    path("ranking/order/<int:ordertype>/", views.ranking_option),
    path("ranking/<int:districtid>/", views.ranking_info),
    path("economics/", views.economics),
]
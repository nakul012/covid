from django.urls import path
from .views import (CovidChartView, StateApiListView, CountryApiListView
                    )


urlpatterns = [
    path('chart', CovidChartView.as_view()),
    path('state-wise-chart', CovidChartView.as_view()),
    path('api/state/', StateApiListView.as_view()),
    path('api/state/<pk>/', StateApiListView.as_view()),
    path('api/state/', CountryApiListView.as_view()),
    path('api/state/<pk>/', CountryApiListView.as_view()),
]

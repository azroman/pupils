from django.urls import path, include
from . import views
# from .api.views import CarAPIView

urlpatterns = [
    path('grades', views.grades, name='grades'),
    path('grades/<slug:grade_value>/', views.grades, name='by_grade'),
    path('pupil/<int:pk>/scores', views.pupil_scores, name='pupil_scores'),
    path('scores', views.scores, name='scores'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Liste des projets
    path('plateforme-integre/projects/', views.ProjectListCreate.as_view(), name='list_projects'),
    # Détails d'un projet (afficher, mettre à jour ou supprimer un projet spécifique)
    path('plateforme-integre/projects/<int:pk>/', views.ProjectRetrieveUpdateDestroy.as_view(), name='project_detail'),
    
    # Liste des décaissements
    path('plateforme-integre/decaissements/', views.DecaissementListCreate.as_view(), name='list_decaissements'),
    # Détails d'un décaissement
    path('plateforme-integre/decaissements/<int:pk>/', views.DecaissementRetrieveUpdateDestroy.as_view(), name='decaissement_detail'),
    
    # Liste des signalements citoyens
    path('plateforme-integre/reports/', views.CitizenReportListCreate.as_view(), name='list_reports'),
    # Détails d'un signalement citoyen
    path('plateforme-integre/reports/<int:pk>/', views.CitizenReportRetrieveUpdateDestroy.as_view(), name='report_detail'),
    
    # Liste des notifications
    path('plateforme-integre/notifications/', views.NotificationListCreate.as_view(), name='list_notifications'),
    # Détails d'une notification
    path('plateforme-integre/notifications/<int:pk>/', views.NotificationRetrieveUpdateDestroy.as_view(), name='notification_detail'),
]

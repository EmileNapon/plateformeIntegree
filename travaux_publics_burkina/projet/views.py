from rest_framework import generics
from .models import Project, Decaissement, CitizenReport, Notification
from .serializers import ProjectSerializer, DecaissementSerializer, CitizenReportSerializer, NotificationSerializer

# Vues pour gérer les projets
class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Vues pour gérer les décaissements
class DecaissementListCreate(generics.ListCreateAPIView):
    queryset = Decaissement.objects.all()
    serializer_class = DecaissementSerializer

class DecaissementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decaissement.objects.all()
    serializer_class = DecaissementSerializer

# Vues pour gérer les signalements citoyens
class CitizenReportListCreate(generics.ListCreateAPIView):
    queryset = CitizenReport.objects.all()
    serializer_class = CitizenReportSerializer

class CitizenReportRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CitizenReport.objects.all()
    serializer_class = CitizenReportSerializer

# Vues pour gérer les notifications
class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

from rest_framework import serializers
from .models import Project, Decaissement, CitizenReport, Notification, ProjectLocation

class ProjectLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLocation
        fields = ['latitude', 'longitude']

class ProjectSerializer(serializers.ModelSerializer):
    location = ProjectLocationSerializer()  

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'location', 'start_date', 'end_date', 'budget', 'contractor', 'status', 'progress']

class DecaissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decaissement
        fields = ['id', 'project', 'step_name', 'amount', 'paid_on', 'actual_deliverables', 'status']

class CitizenReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenReport
        fields = ['id', 'project', 'citizen_name', 'report_date', 'report_text', 'photo', 'status']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'project', 'message', 'send_date', 'sent_to', 'platform']

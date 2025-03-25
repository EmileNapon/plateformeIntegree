# models.py
from django.db import models

from userAuth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)  # Nom du projet
    description = models.TextField()  # Description du projet
    location = models.CharField(max_length=255)  # Localisation du projet
    start_date = models.DateField()  # Date de début prévue
    end_date = models.DateField()  # Date de fin prévue
    budget = models.DecimalField(max_digits=12, decimal_places=2)  # Budget alloué
    contractor = models.ForeignKey(User, related_name='prestataire', on_delete=models.CASCADE)  # Entreprise prestataire
    status = models.CharField(max_length=100, choices=[('Planning', 'Planning'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])  # Statut du projet
    geo_coordinates = models.JSONField()  # Coordonnées géographiques (Latitude, Longitude)
    progress = models.DecimalField(max_digits=5, decimal_places=2)  # Progrès en pourcentage (de 0 à 100%)

    def __str__(self):
        return self.name


class Decaissement(models.Model):
    project = models.ForeignKey(Project, related_name='decaissements', on_delete=models.CASCADE)  # Lien vers le projet
    step_name = models.CharField(max_length=100)  # Nom de l'étape (ex. "Phase 1", "Phase 2")
    amount = models.DecimalField(max_digits=12, decimal_places=2)  # Montant du décaissement
    paid_on = models.DateField()  # Date de paiement
    actual_deliverables = models.TextField()  # Livrables réels pour cette étape
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])  # Statut du paiement

    def __str__(self):
        return f"Décaissement {self.step_name} pour {self.project.name}"


class CitizenReport(models.Model):
    project = models.ForeignKey(Project, related_name='reports', on_delete=models.CASCADE)  # Lien vers le projet
    citizen_name = models.CharField(max_length=200)  # Nom du citoyen ou anonyme
    report_date = models.DateField(auto_now_add=True)  # Date du signalement
    report_text = models.TextField()  # Description du problème observé
    photo = models.ImageField(upload_to='reports/', null=True, blank=True)  # Photo (optionnelle)
    status = models.CharField(max_length=100, choices=[('New', 'New'), ('Reviewed', 'Reviewed'), ('Resolved', 'Resolved')])  # Statut du rapport

    def __str__(self):
        return f"Signalement de {self.citizen_name} pour {self.project.name}"


class Notification(models.Model):
    project = models.ForeignKey(Project, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()  # Message de notification
    send_date = models.DateTimeField(auto_now_add=True)  # Date d'envoi
    sent_to = models.CharField(max_length=200)  # Destinataires (peut inclure les groupes de citoyens)
    platform = models.CharField(max_length=100, choices=[('Facebook', 'Facebook'), ('SMS', 'SMS')])  # Canal de notification

    def __str__(self):
        return f"Notification pour {self.project.name} le {self.send_date}"


class ProjectLocation(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f"Location for {self.project.name}"

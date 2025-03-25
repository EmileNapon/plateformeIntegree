from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'role', 'phone_number', 'profile_pic', 'is_verified',
            'profession', 'enabled_notifications', 'name_organization',
            'nom_entreprise', 'secteur_activite', 'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True},  # Le mot de passe ne doit pas être récupéré dans les réponses
        }
    
    def create(self, validated_data):
        # On retire le mot de passe avant de créer l'utilisateur
        password = validated_data.pop('password', None)
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user





from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajout des informations utilisateur au token
        token['id'] = user.id
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['role'] = user.role
        token['phone_number'] = user.phone_number
        token['profile_pic'] = user.profile_pic.url if user.profile_pic else None
        token['profession'] = user.profession
        token['enabled_notifications'] = user.enabled_notifications
        token['name_organization'] = user.name_organization
        token['nom_entreprise'] = user.nom_entreprise
        token['secteur_activite'] = user.secteur_activite
        token['is_verified'] = user.is_verified

        return token

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        
        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Les identifiants sont incorrects.")
        data = super().validate(attrs)  # Authentifie l'utilisateur et génère les tokens

        # Récupérer l'utilisateur authentifié
        user = self.user

        # Si l'utilisateur est None (authentification échouée), lève une erreur
        if user is None:
            raise serializers.ValidationError("L'authentification a échoué.")

        # Ajout des données utilisateur à la réponse du token
        data.update({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'role': user.role,
            'phone_number': user.phone_number,
            'profile_pic': user.profile_pic.url if user.profile_pic else None,
            'profession': user.profession,
            'enabled_notifications': user.enabled_notifications,
            'name_organization': user.name_organization,
            'nom_entreprise': user.nom_entreprise,
            'secteur_activite': user.secteur_activite,
            'is_verified': user.is_verified
        })
        return data

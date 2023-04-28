from django.contrib.auth import get_user_model
from django.db.models import Q
from dynaconf import ValidationError
from rest_framework import serializers


User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token'
        ]

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("a username is required")
        user = User.objects.filter(Q(username=username))
        if user.exists():
            user_obj = user.first()
        else:
            raise ValidationError("this username i not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Uncorrected password. try again")
        data["token"] = "some random token"
        return data
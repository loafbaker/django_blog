from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=False)
    email2 = serializers.EmailField(label='Confirm Email', write_only=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            },
        }

    def validate_email(self, value):
        user_qs = User.objects.filter(email=value)
        if user_qs.exists():
            raise serializers.ValidationError('This email has already been registered.')
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email = data.get('email')
        if email != value:
            raise serializers.ValidationError('Email must match.')
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(username, email, password)
        return validated_data
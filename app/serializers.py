from rest_framework import routers, serializers, viewsets
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.id = validated_data.get('id', instance.id)
            instance.name= validated_data.get('name', instance.name)
            instance.roll = validated_data.get('roll', instance.roll)
            instance.city = validated_data.get('city', instance.city)
            instance.save()
            return instance

        # field level validation

        # def validate_roll(self, value):d
        #     if value < 100:
        #         raise serializers.ValidationError("The roll no should be greater than 100")
        #     return value

        # object level validation

        def validate(self, data):
            if (data.get('roll') < 100):
                raise serializers.ValidationError("The roll no should be greater than 100")
            else:
                return data





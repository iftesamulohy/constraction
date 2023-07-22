from rest_framework import serializers

from users.models import Employee

class AllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['email','password','first_name','last_name']
    def create(self, validated_data):
       user = Employee.objects.create(
       email = validated_data['email'],
       first_name =validated_data['first_name'],
       last_name =validated_data['last_name'],
       )
       user.set_password(validated_data['password'])
       user.save()
       return user
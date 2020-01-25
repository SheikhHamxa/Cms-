from rest_framework import serializers
from location.models import Franchise
from vehicle.models import Vehicle
from .models import USer
# from .models import Sender
from .models import UserType
# from .models import Receiver
# from .models import Manager
# from .models import PostPerson
# from .models import Staff

from django.contrib.auth.models import User


class USerSerializer(serializers.ModelSerializer):
    sender=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=1), slug_field='first_name', allow_null=True)
    receiver=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=2), slug_field='first_name', allow_null=True)
    manager=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=3), slug_field='first_name', allow_null=True)
    staff=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=4), slug_field='first_name', allow_null=True)
    admin=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=5), slug_field='first_name', allow_null=True)
    driver=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=6), slug_field='first_name', allow_null=True)
    post_person=serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=7), slug_field='first_name', allow_null=True)
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username', allow_empty=True,
                                         allow_null=True)
    usertype = serializers.SlugRelatedField(queryset=UserType.objects.all(), slug_field='user_type')
    franchise = serializers.SlugRelatedField(queryset=Franchise.objects.all(), slug_field='name')

    # vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(),slug_field='name',allow_empty=True, allow_null=True)
    # vehicle=VehicleSerializer(Vehicle, allow_null=True, read_only=True)
    # vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(),slug_field='name',allow_empty=True, allow_null=True)

    # franchise= FranchiseSerializer(read_only=True)
    # "" packagerates = serializers.SlugRelatedField(queryset=PackageRates.objects.all(), slug_field='price_per_gram')
    # vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='name', many=True)
    # vehicle = VehicleSerializer(allow_null=True)
    # postperson = serializers.StringRelatedField(many=True, read_only=True)
    # manager = serializers.StringRelatedField(many=True, read_only=True)
    # staff = serializers.StringRelatedField(many=True, read_only=True)
    # package = serializers.StringRelatedField(many=True, read_only=True)
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = USer
        fields = '__all__'


class UserTypeSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = UserType
        fields = '__all__'


"""
class SenderSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receievr = serializers.StringRelatedField()

    class Meta:
        model = Sender
        fields = '__all__'


class ReceiverSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Receiver
        fields = '__all__'

"""
"""
class PostPersonSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PostPerson
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Manager
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Staff
        fields = '__all__'
"""
"""sender = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=1), slug_field='first_name',
                                      allow_empty=True, allow_null=True)

receiver = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=2), slug_field='first_name',
                                        allow_empty=True, allow_null=True)

manager = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=3), slug_field='first_name',
                                       allow_null=True)
admin = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=4), slug_field='first_name',
                                     allow_null=True, allow_empty=True)
postperson = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=5), slug_field='first_name',
                                          allow_null=, allow_empty=True)
driver = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=6), slug_field='first_name',
                                      allow_null=True)

staff = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=7), slug_field='first_name',
                                     allow_empty=True, allow_null=True)
"""
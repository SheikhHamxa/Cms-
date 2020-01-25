from rest_framework import serializers
from django.db import models

from location.models import Franchise
from location.serializations import FranchiseSerializer
from vehicle.models import Vehicle
from .models import Package, PackageRates, PackageStatus, PackageBilling

from django.contrib.auth.models import User
from USer.models import USer


class PackageSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    packagerates = serializers.SlugRelatedField(queryset=PackageRates.objects.all(), slug_field='price_per_gram')
    # vehicle = serializers.SlugRelatedField(queryset=Vehicle.objects.all(), slug_field='name')
    sender = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=1), slug_field='first_name', allow_null=True)
    receiver = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=2), slug_field='last_name',allow_null=True)
    post_person = serializers.SlugRelatedField(queryset=USer.objects.filter(usertype=6), slug_field='email',allow_null=True)

    packagestatus = serializers.SlugRelatedField(queryset=PackageStatus.objects.all(), slug_field='status')

    # usertype = serializers.StringRelatedField(many=True, read_only=True)
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # packagestatus = serializers.StringRelatedField(many=True,read_only=True)
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Package
        fields = '__all__'


class PackageBillingSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    franchise = serializers.SlugRelatedField(queryset=Franchise.objects.all(), slug_field='email')
    # franchise=FranchiseSerializer(read_only=True)
    # package=PackageSerializer(read_only=True)
    package = serializers.SlugRelatedField(queryset=Package.objects.all(), slug_field='name')

    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PackageBilling
        fields = '__all__'


class PackageRatesSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # user = serializers.StringRelatedField(many=True, read_only=True)
    # package = serializers.StringRelatedField(many=True, read_only=True)
    # location = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = PackageRates
        fields = '__all__'


class PackageStatusSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    # owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # franchise = models.OneToOneField(PackageRates, related_name='packagerates', on_delete=models.CASCADE)
    # pacakage = serializers.SlugRelatedField(queryset=Package.objects.all(), slug_field='name')

    class Meta:
        model = PackageStatus
        fields = '__all__'

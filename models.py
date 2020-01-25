from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


# from package.models import Package, PackageRates
# from vehicle.models import Vehicle
# from vehicle.models import Vehicle
from location.models import Franchise
# from vehicle.models import Vehicle
from vehicle.models import Vehicle

LEXERS = [item for item in get_all_lexers() if item[1]]
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class UserType(models.Model):
    User_Type = (
        ('SENDER', 'Sender'),
        ('RECEIVER', 'Receiver'),
        ('MANAGER', 'Manager'),
        ('STAFF', 'Staff'),
        ('ADMIN', 'Admin'),
        ('DRIVER', 'Driver'),
        ('POST_PERSON', 'post_person'),

    )
    user_type = models.CharField(max_length=15, choices=User_Type, unique=True)
    owner = models.ForeignKey('auth.User', related_name='usertype', on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.user_type} '
        return template.format(self)


"""
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    post_person = models.CharField(max_length=100)
    staff = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    Admin = models.CharField(max_length=100)

    def __str__(self):
        return self.sender
"""


class USer(models.Model):
    select_gender = (('M', 'MALE'),
                     ('F', 'FEMALE'),
                     )
    status = (
        ('Punjab', 'PUNJAB'),
        ('Sindh', 'SINDH'),
        ('Balochistan', 'BALOCHISTAN'),
        ('kpk', 'KPK'),
    )
    dist = (
        ('Rawalpindi', 'RAWALPINDI'),
        ('Islamabd', 'ISLAMAABAD'),
        ('Faislabad', 'FAISALABAD'),
        ('Peshawer', 'PESHAWER'),
        ('Karachi', 'KARACHI'),
        ('Lahore', 'LAHORE'),
        ('Abbotabad', 'ABBOTABAD'),
        ('Quetta', 'QUETTA'),
        ('Hyderabd', 'HYDERABAD'),
        ('Attock', 'ATTOCK'),
        ('Bahawalnager', 'BAHAWALNAGR'),
        ('Bahawalpur', 'BAHAWALPUR'),
        ('Bhakker', 'BHAKKER'),
        ('Chakwal', 'CHAKWAL'),
        ('Gujrat', 'GUJRAT'),
        ('Gujranwala', 'GUJRANWALA'),
        ('Hafzabad', 'HAFIZABAD'),
        ('Multan', 'MULTAN'),
        ('Rahim yar khan', 'RAHIM_YAR_KHAN'),
        ('Sahiwal', 'SAHIWAL'),
        ('Sarghoda', 'SARGHODA'),
        ('Sialkot', 'SIALKOT'),
        ('Layyah', 'LAYYAH'),
        ('Tibbet', 'TIBBET'),
        ('Chamman', 'CHAMMAN'),
        ('Sui', 'SUI'),
        ('ZHOB', 'ZHOB'),
        ('Gawader', 'GAWADAR'),
        ('Sukhhar', 'SUKKHAR'),
        ('Ghotki', 'GHOTKI'),
        ('Naushro feroz', 'NAUSHERO FEROZ'),
        ('Tharphar', 'THARPAR'),
        ('Mirpur khas', 'MIRPUR KHAS'),
        ('Sheikupura', 'SHIKHARPUR'),
        ('Larkana', 'LARKANA'),
        ('Jacobabad', 'JACOBABAD'),
        ('Malir', 'MALIR'),
        ('Karachi east', 'KARACHI EAST'),
        ('Karachi west', 'KARACHI WEST'),
        ('Bannu', 'BANUU'),
        ('Laki marawat', 'LAKI MARAWAT'),
        ('Dera Ismail khan', 'DERA ISMAIL'),
        ('Mansehra', 'MANSEHARA'),
        ('Haripur', 'HARIPUR'),
        ('Kohat', 'KOHAT'),
        ('Shingla', 'SHANGLA'),
        ('Chitral', 'CHITRAL'),
        ('Swat', 'SAWAT'),
        ('Mardan', 'MARDAN'),
        ('Swabi', 'SAWABI'),
        ('Charsada', 'CHARSEDA'),
        ('Bagh', 'BAGH'),
        ('Mirpur', 'MIRPUR'),
        ('Rawalakot', 'RAWALAKOT'),

    )
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, null=True)
    cnic = models.CharField(max_length=100, unique=True, null=True)
    gender = models.CharField(max_length=1, choices=select_gender)
    province = models.CharField(max_length=100, choices=status)
    district = models.CharField(max_length=100, choices=dist)
    sector = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    house_no = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    driver_liesence_number=models.CharField(max_length=100, null=True)
    sender = models.ForeignKey('self', on_delete=models.CASCADE, related_name='a_user', null=True, blank=True)
    receiver = models.ForeignKey('self', on_delete=models.CASCADE, related_name='bb_user', null=True)
    manager = models.ForeignKey('self', on_delete=models.CASCADE, related_name='cc_user',blank=True, null=True)
    admin = models.ForeignKey('self', on_delete=models.CASCADE, related_name='aaaaa_user', null=True, blank=True)
    driver = models.ForeignKey('self', on_delete=models.CASCADE, related_name='e_user',blank=True,null=True)
    post_person = models.ForeignKey('self', on_delete=models.CASCADE, related_name='f_user',null=True)
    staff = models.ForeignKey('self', on_delete=models.CASCADE, related_name='g_user', null=True)
    usertype = models.ForeignKey(UserType, related_name='user', on_delete=models.CASCADE,null=True)
    # "" package=models.ForeignKey(Package,related_name='package',on_delete=models.CASCADE)
    franchise = models.ForeignKey(Franchise, related_name='user', on_delete=models.CASCADE,null=True)
    vehicle = models.ManyToManyField(Vehicle,related_name='vehicle', blank=True)
    # location = models.ForeignKey(Location, related_name='user', on_delete=models.CASCADE)
    # packagerates = models.ForeignKey(PackageRates, related_name='user', on_delete=models.CASCADE)
    # highlighted = models.TextField(default=None)
    # class Meta:
    # ordering = ['created', ]

    def __str__(self):
        template = '{0.first_name} {0.last_name} {0.email} '
        return template.format(self)


"""
    def save(self, *args, **kwargs):  # new
        
        

        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Employe, self).save(*args, **kwargs)
"""

"""
class Sender(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    USer = models.ForeignKey(Employe, related_name='sender', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='sender', on_delete=models.CASCADE)

    def __str__(self):
        return self.USer.first_name


class Receiver(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    USer = models.ForeignKey(Employe, related_name='receiver', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='receiver', on_delete=models.CASCADE)
    sender = models.ManyToManyField(Sender)

    def __str__(self):
        return self.USer.first_name

"""
"""
class PostPerson(models.Model):
    USer = models.ForeignKey(Employe, related_name='postperson', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='postperson', on_delete=models.CASCADE)
    employe_number = models.IntegerField()
    duty_tyming = models.DateTimeField()


class Manager(models.Model):
    USer = models.ForeignKey(Employe, related_name='manager', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='manager', on_delete=models.CASCADE)
    employe_number = models.IntegerField()
    duty_tyming = models.DateTimeField()


class Staff(models.Model):
    USer = models.ForeignKey(Employe, related_name='staff', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='staff', on_delete=models.CASCADE)
    employe_number = models.IntegerField()
    duty_tyming = models.DateTimeField()
    
"""""

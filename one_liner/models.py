from django.core.validators import RegexValidator

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None):
        """
        Creates and saves a Userwith the given username, phone_number and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username = username,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password):
        """
        Creates and saves a superuser with the given username, phone_number and password.
        """
        user = self.create_user(
            username,
            password=password,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class One_liner(models.Model):
    one_liner_id = models.AutoField(primary_key=True)
    one_liner_text = models.TextField('Daily update text')
    pub_date = models.DateField('one_liner date')
    create_date = models.DateTimeField('created at date', auto_now_add=True, blank=True)
    author = models.ForeignKey('CustomUser', related_name='updates', on_delete=models.CASCADE)
    update_image = models.ImageField(upload_to='images', blank=True, null=True)
    one_liner_count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %s' % (self.pub_date, self.one_liner_text)



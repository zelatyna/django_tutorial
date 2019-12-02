from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    phone_number = models.TextField(verbose_name="Full phone  number", blank=False, max_length=50)

    def __str__(self):
        return self.username


class One_liner(models.Model):
    one_liner_id = models.IntegerField(primary_key=True)
    one_liner_text = models.TextField('Daily update text')
    pub_date = models.DateField('one_liner date')
    create_date = models.DateTimeField('created at date', auto_now_add=True, blank=True)
    author = models.ForeignKey('CustomUser', related_name='updates', on_delete=models.CASCADE)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updates')
    one_liner_count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %s' % (self.pub_date, self.one_liner_text)



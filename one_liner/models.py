from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return "%s : %s" % (self.id, self.user_name)

class One_liner(models.Model):
    one_liner_id = models.IntegerField(primary_key=True)
    one_liner_text = models.TextField()
    pub_date = models.DateField('one_liner date')
    create_date = models.DateTimeField('created at date', auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updates')
    one_liner_count = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %s' % (self.pub_date, self.one_liner_text)



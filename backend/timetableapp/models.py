from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings


class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,user_name,first_name,password, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        return self.create_user(email,user_name,first_name,password,**other_fields)
    
    def create_user(self,email,user_name,first_name,password,**other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,
                          first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    user_name = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'),max_length=500,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return self.user_name


class Subjects(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='subject_posts')
    y = [('I-Year','I-year'),('II-Year','II-year'),('III-Year','III-year'),('IV-Year','IV-year')]
    year = models.CharField(choices=y,blank=True,max_length=100)
    s = [('I-Semester','I-semester'),('II-Semester','II-sem'),('III-Semester','III-sem'),('IV-Semester','IV-sem'),
         ('V-Semester','V-sem'),('VI-Semester','VI-sem'),('VII-Semester','VII-sem'),('VIII-Semester','VIII-sem')]
    sem = models.CharField(choices=s,blank=True,max_length=100)
    subject_code = models.CharField(max_length=150,blank=True)
    subject_name = models.CharField(max_length=150,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.subject_name

    class Meta:
        ordering = ['-updated','-created']
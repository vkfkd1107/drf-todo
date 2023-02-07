from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=10, verbose_name='이름')
    email = models.EmailField(max_length=100, verbose_name='이메일', unique=True)
    phonenumber = models.CharField(
        max_length=11, verbose_name='전화번호'
    )
    birthday = models.DateField(null=True, verbose_name='생년월일')
    status = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    remarks = models.TextField(blank=True, default='', verbose_name='비고')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name_plural = '가입 정보'

    def __str__(self):
        return f"{self.name}_{self.phonenumber}"

    @property
    def is_staff(self):
        return self.is_admin

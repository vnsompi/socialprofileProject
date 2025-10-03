from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserProfileManager(BaseUserManager):
    """handles user profile """

    def create_user(self, email, name, password=None):
        """create user profile """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        """change the user password and hash it """
        user.save(using=self._db)
        return user


    def create_superuser(self, email, name, password):
        """"create superuser profile """
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """handles user profile """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Return the first_name plus the last_name, with a space in between"""
        return self.name

    def get_short_name(self):
        """ Return the short name for the user"""
        return self.name

    def __str__(self):
        """ Return a string representation of the user """
        return self.email

"""feed items class """

class FeedItem(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='feed_image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user_profile.email} - {self.content[:25]}..."







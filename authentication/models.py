from django.apps import apps
from django.contrib.auth.hashers import make_password

from django.db import models
from django.contrib.auth.models import (PermissionsMixin,AbstractBaseUser,UserManager)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class MyUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
            """
        Create and save a user with the given username, email, and password.
        """
            # if not username:
            #     raise ValueError("The given username must be set")
            if not email:
                raise ValueError("The given email must be set")
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
            email = self.normalize_email(email)

            GlobalUserModel = apps.get_model(
                self.model._meta.app_label, self.model._meta.object_name
             )
            # username = GlobalUserModel.normalize_username(username)
            user = self.model( email=email, **extra_fields)
            user.password = make_password(password)
            user.save(using=self._db)
            return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user( email, password, **extra_fields)

    
class User(AbstractBaseUser,PermissionsMixin):

    # username_validator = UnicodeUsernameValidator()

    # username = models.CharField(
    #     _("username"),
    #     max_length=150,
    #     unique=True,
    #     help_text=_(
    #         "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
    #     ),
    #     validators=[username_validator],
    #     error_messages={
    #         "unique": _("A user with that username already exists."),
    #     },
    # )
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    confirm_password = models.CharField(_("confirm_password"), max_length=150, blank=False)
    mobile_phone = models.CharField(_("mobile_phone"), max_length=150, blank=False)
    email = models.EmailField(_("email address"), blank=False,unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    email_verified=models.BooleanField(
        _("email_verified"),
        default=False,
        help_text=_(
            "Designates whether this user email verified should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile_phone","confirm_password","password","last_name","first_name"]
    
    @property
    def token(self):
        return ''
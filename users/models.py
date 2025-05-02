# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('client', 'Client'),
#         ('admin', 'Administrator'),
#         ('receptionist', 'Receptionist'),
#         ('technician', 'Technician'),
#     )
#     role = models.CharField(max_length=20, choices=ROLE_CHOICES)

#     def __str__(self):
#         return f"{self.username} ({self.role})"


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('admin', 'Administrator'),
        ('receptionist', 'Receptionist'),
        ('technician', 'Technician'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES ,default='receptionist')
    email = models.EmailField(unique=True)  # جعل email حقلًا فريدًا
    # account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, default='client')
    # تحديد email كحقل تسجيل الدخول الرئيسي
    USERNAME_FIELD = 'email'
    # جعل username اختياريًا (غير مطلوب)
    REQUIRED_FIELDS = ['username']  # يمكن تغييره إلى حقول أخرى إذا لزم الأمر

    def __str__(self):
        return f"{self.email} ({self.role})"  # تعديل لعرض email بدلاً من username
from django.db import models

# Create your models here.
class StudentsFilter(models.Model):

    FILTER_CHOICES = (
        ('students', 'students'),
        ('teachers', 'teachers'),
        ('parents', 'parents'),
        ('admins', 'admins'),

    )
    SPECILIZED_CHOICES = (
        ('Web Dev','Web Dev'),
        ('Mobile Dev','Mobile Dev'),
        ('Game Dev','Game Dev'),
        ('security', 'security'),
        )
    
    LEVEL_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        )
    
    CLASS_CHOICES = (
        ('Class 1','Class 1'),
        ('Class 2','Class 2'),
        ('Class 3','Class 3'),
        )
    FilteringLevel = models.CharField(max_length=20, choices=FILTER_CHOICES, default = '')
    StudentSpecilized = models.CharField(max_length=20, choices=SPECILIZED_CHOICES, default = '')
    StudentLevel = models.CharField(max_length=20, choices=LEVEL_CHOICES, default = '')
    StudentClass = models.CharField(max_length=20, choices=CLASS_CHOICES, default = '')
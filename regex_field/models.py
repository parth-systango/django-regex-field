from django.db import models
from regex_field import fields


# Create your models here.
class RegularExpression(models.Model):
    
    regex = fields.RegexField(max_length=256)

    class Meta:
        verbose_name = 'RegularExpression'
        verbose_name_plural = 'RegularExpressions'
        db_table = 'regular_expression'

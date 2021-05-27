from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


def image_upload_path(instance: models.Model, filename: str) -> str:
    '''
    Function that create path for saving item img depends on item slug field.
    '''
    return f"images/{slugify(instance.name)}.{filename.split('.')[-1]}"


class RangeValidator(BaseValidator):
    
    def __init__(self, start: float, stop: float):
        self._min = start
        self._max = stop

    def __call__(self, value: Any):
        value = float(value)
        if value > self._max or value < self._min:
            raise  ValidationError(
                _(f'Value must be between {self._min} and {self._max}')
            )


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        _('created at'),
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


# Create your models here.
class Beer(TimestampedModel):
    name = models.CharField(
        _('beer name'),
        max_length=255
    )
    description = models.TextField(
        _('beer description'),
        blank=True,
        null=True,
    )
    mark = models.DecimalField(
        _('beer mark'),
        decimal_places=1,
        max_digits=3,
        validators=[
            RangeValidator(0, 10)
        ]
    )
    price = models.DecimalField(
        _('beer price'),
        decimal_places=2,
        max_digits=5,
        help_text=_(
            'Beer price in UAH'
        ),
        validators=[
            RangeValidator(0, 1000)
        ]
    )
    image = models.ImageField(
        _('beer image'),
        blank=True,
        null=True,
        upload_to = image_upload_path,
    )

    #relations:
    # user_marks
    # user_comments

    class Meta:
        ordering = ['-updated_at']

    def __str__(self) -> str:
        return self.name


class UserComment(TimestampedModel):
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        help_text=_('owner of this mark')
    )
    beer = models.ForeignKey(
        'Beer',
        on_delete=models.CASCADE,
        related_name='user_comments',
        help_text=_(
            'shows for which beer this comment is'
        )
    )
    mark = models.DecimalField(
        _('beer mark'),
        decimal_places=1,
        max_digits=3,
    )
    text = models.TextField(blank=True)

    class Meta:
        ordering = ['-updated_at']
        unique_together = ['owner', 'beer']

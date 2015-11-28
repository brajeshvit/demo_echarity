# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

def upload_to(instance, filename):
    return '/'.join(['images', unicode(instance.pk), filename])


class Product(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    quentity = models.IntegerField()
    image = models.ImageField(_("Image"), upload_to=upload_to)
    zipcode = models.CharField(max_length=6)
    discription = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)
    expiry_date = models.DateTimeField(
            blank=True, null=True)
    address = models.CharField(max_length=200)
    
    def __unicode__(self):
        return (self.title)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ("image",)

    def __unicode__(self):
        return self.image.path

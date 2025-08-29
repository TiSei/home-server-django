from copy import Error
from django.db import models
from django.utils import timezone

class FileCleanupMixin:
    file_fields = []

    def delete(self, *args, **kwargs):
        for file_field in self.file_fields:
            file = getattr(self, file_field)
            if file:
                file.delete(False)
        return super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        print('test2')
        if self.pk:
            instance = type(self).objects.filter(pk=self.pk).first()
            if instance:
                for file_field in self.file_fields:
                    old = getattr(instance, file_field)
                    new = getattr(self, file_field)
                    if not new or (old and old != new):
                        old.delete(False)
        return super().save(*args, **kwargs)

class DBObject(models.Model):
    # id generated automatic
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        print('test1')
        if not self.pk and not self.created:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
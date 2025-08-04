from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

HEX_COLOR_VALIDATOR = RegexValidator(
    regex=r'^#([A-Fa-f0-9]{6})$',
    message='Farbe muss ein 6-stelliger Hex-Code sein, z.B. #FF0000',
)

VERSION_VALIDATOR = RegexValidator(
    regex=r'^\d+\.\d{1,2}$',
    message='Version muss eine valide Versionsbezeichnung sein, z.B. 1.1',
)

class DBObject(models.Model):
    # id generated automatic
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created:
            self.created = timezone.now()
        super().save(*args, **kwargs)


class Tag_Group(DBObject):
    name = models.CharField(max_length=40, unique=True)
    color = models.CharField(max_length=7, validators=[HEX_COLOR_VALIDATOR])

    def __str__(self):
        return self.name

class Tag(DBObject):
    name = models.CharField(max_length=40, unique=True)
    desc = models.TextField(max_length=200)
    tag_group = models.ForeignKey(Tag_Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='tags')

    def __str__(self):
        return self.name

class Print_Profil(DBObject):
    name = models.CharField(max_length=40, unique=True)
    desc = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Project(DBObject):
    name = models.CharField(max_length=40, unique=True)
    target = models.TextField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_tags(self):
        tag_set = set()
        for part in self.parts.all():
            tag_set.update(part.tags.all())
        return sorted(tag_set, key=lambda tag: tag.name)

class Part(DBObject):
    name = models.CharField(max_length=40)
    desc = models.TextField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='parts')
    tags = models.ManyToManyField(Tag, related_name='parts')

    def __str__(self):
        return self.project.name+': '+self.name

    def get_img_url(self):
        last_modified_variant = self.Variants.all().order_by('last_modified').first()
        if last_modified_variant:
            return last_modified_variant.image.url
        return None

class Variant(DBObject):
    name = models.CharField(max_length=40)
    version = models.CharField(max_length=4, validators=[VERSION_VALIDATOR])
    image = models.ImageField(upload_to='uploads/img', blank=True, null=True)
    fc_file = models.FileField(upload_to='uploads/fc_file', blank=True, null=True)
    stl_file = models.FileField(upload_to='uploads/stl_file')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='Variants')
    printprofil = models.ForeignKey(Print_Profil, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

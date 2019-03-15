from django.db import models


class Images(models.Model):
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'images'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return str(self.id)


class DeviceFirmware(models.Model):
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    device_id = models.IntegerField()
    hidden_flag = models.IntegerField(default=0)
    tag = models.CharField(max_length=255, null=True, default=None)
    en = models.TextField(max_length=65535, null=True, default=None)
    ru = models.TextField(max_length=65535, null=True, default=None)

    class Meta:
        db_table = 'device_firmware'
        verbose_name = 'Device firmware'
        verbose_name_plural = 'Device firmwares'


class ImageVariants(models.Model):
    image_id = models.ForeignKey(Images, related_name='image', on_delete=models.DO_NOTHING)
    language_id = models.IntegerField()
    value = models.CharField(max_length=200)

    class Meta:
        db_table = 'image_variants'
        verbose_name = 'Image Variant'
        verbose_name_plural = 'Image Variants'

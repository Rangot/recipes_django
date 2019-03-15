from django.contrib import admin
from .models import *


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = Images


admin.site.register(Images, ImagesAdmin)


class DeviceFirmwareAdmin(admin.ModelAdmin):
    list_display = ['major_version', 'minor_version', 'device_id', 'hidden_flag', 'tag', 'en', 'ru']

    class Meta:
        model = DeviceFirmware


admin.site.register(DeviceFirmware, DeviceFirmwareAdmin)


class ImageVariantsAdmin(admin.ModelAdmin):
    list_display = ['image_id', 'language_id', 'value']

    class Meta:
        model = ImageVariants


admin.site.register(ImageVariants, ImageVariantsAdmin)

admin.site.site_header = 'Recipes administration'

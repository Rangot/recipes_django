from django.urls import path

from .views import index, DeviceFirmwareCreate, ImageVariantCreate, device_firmwares, image_variants

urlpatterns = [
    path('', index, name='index'),
    path('device_firmware/create/', DeviceFirmwareCreate.as_view(), name='device_firmware_create'),
    path('image_variant/create/', ImageVariantCreate.as_view(), name='image_variant_create'),
    path('device_firmwares/', device_firmwares, name='device_firmwares'),
    path('image_variants/', image_variants, name='image_variants'),
]

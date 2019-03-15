from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .forms import *
from .utils import ObjectCreateMixin


def index(request):
    return render(request, 'recipes/index.html')


def device_firmwares(request):
    device_firmwares_all = DeviceFirmware.objects.all()
    return render(request, 'recipes/device_firmwares.html', context={'device_firmwares_all': device_firmwares_all})


def image_variants(request):
    image_variants_all = ImageVariants.objects.all()
    return render(request, 'recipes/image_variants.html', context={'image_variants_all': image_variants_all})


class DeviceFirmwareCreate(ObjectCreateMixin, View):
    model_form = DeviceFirmwareForm
    template = 'recipes/device_firmware_create_form.html'
    redirect_url = 'device_firmwares'
    raise_exception = True


class ImageVariantCreate(ObjectCreateMixin, View):
    model_form = ImageVariantsForm
    template = 'recipes/image_variant_create_form.html'
    redirect_url = 'image_variants'
    raise_exception = True



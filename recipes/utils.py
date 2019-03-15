from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404

from .models import *


class ObjectCreateMixin:
    model_form = None
    template = None
    redirect_url = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(reverse(self.redirect_url))
        return render(request, self.template, context={'form': bound_form})

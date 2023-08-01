from django.contrib import admin
from django.apps import apps
# Register your models here.

website_models = apps.get_app_config('website').get_models()

for model in website_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


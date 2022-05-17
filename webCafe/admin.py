from django.contrib import admin

# from .models import Image
#
#
# admin.site.register(Image)
from webCafe.models import Contact, Blog

admin.site.register(Contact)
admin.site.register(Blog)

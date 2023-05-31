from django.contrib import admin
from .models import Payment
from .models import Trans

admin.site.register(Payment)
admin.site.register(Trans)

from django.contrib import admin
from .models import Produtor, Receita, Despesa, Documento

admin.site.register(Produtor)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Documento)

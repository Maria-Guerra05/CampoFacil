from django.contrib import admin
from .models import Produtor, Receita, Despesa, Documento, Contabilidade

admin.site.register(Produtor)
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Documento)
admin.site.register(Contabilidade)
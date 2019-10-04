from django.contrib import admin
from .models import Ativos_TI, Tipo_Equipamento, Modelos, Manutencao


admin.site.register(Ativos_TI)
admin.site.register(Tipo_Equipamento)
admin.site.register(Modelos)
admin.site.register(Manutencao)

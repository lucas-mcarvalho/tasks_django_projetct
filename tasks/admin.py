from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'titulo',
        'data_hora_agendada',
        'status',
        'prioridade',
        'criado_em',
    )

    search_fields = ['titulo', 'descricao']
    list_filter = ['status', 'prioridade']


admin.site.register(Task, TaskAdmin)
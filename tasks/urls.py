from django.urls import path
from tasks.views import ListarTasks, CriarTask, EditarTask, DeletarTask


urlpatterns = [
    path("", ListarTasks.as_view(), name="listar-tasks"),
    path("novo/", CriarTask.as_view(), name="criar-task"),
    path("editar/<int:pk>/", EditarTask.as_view(), name="editar-task"),
    path("deletar/<int:pk>/", DeletarTask.as_view(), name="deletar-task"),
]
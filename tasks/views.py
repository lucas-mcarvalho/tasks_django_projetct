from django.shortcuts import render

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task
from tasks.forms import FormularioTask


class ListarTasks(LoginRequiredMixin, ListView):
    """
    View para listar as tarefas cadastradas do usuário logado.
    """
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/listar.html"

    def get_queryset(self, **kwargs):
        pesquisa = self.request.GET.get("pesquisa", None)

        queryset = Task.objects.filter(user=self.request.user)

        if pesquisa is not None:
            queryset = queryset.filter(titulo__icontains=pesquisa)

        return queryset


class CriarTask(LoginRequiredMixin, CreateView):
    """
    View para criar uma nova tarefa.
    """
    model = Task
    form_class = FormularioTask
    template_name = "tasks/novo.html"
    success_url = reverse_lazy("listar-tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditarTask(LoginRequiredMixin, UpdateView):
    """
    View para editar uma tarefa do usuário logado.
    """
    model = Task
    form_class = FormularioTask
    template_name = "tasks/editar.html"
    success_url = reverse_lazy("listar-tasks")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class DeletarTask(LoginRequiredMixin, DeleteView):
    """
    View para deletar uma tarefa do usuário logado.
    """
    model = Task
    template_name = "tasks/deletar.html"
    success_url = reverse_lazy("listar-tasks")

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
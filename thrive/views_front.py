from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Thrive


class ThriveListView(LoginRequiredMixin, ListView):
    template_name = "thrive/thrive_list.html"
    model = Thrive
    context_object_name = "thrive"


class ThriveDetailView(LoginRequiredMixin, DetailView):
    template_name = "thrive/thrive_detail.html"
    model = Thrive


class ThriveUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "thrive/thrive_update.html"
    model = Thrive
    fields = "__all__"


class ThriveCreateView(LoginRequiredMixin, CreateView):
    template_name = "thrive/thrive_create.html"
    model = Thrive
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class ThriveDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "thrive/thrive_delete.html"
    model = Thrive
    success_url = reverse_lazy("thrive_list")

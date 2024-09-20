from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import DepartamentoSerializer, PaisSerializer
from django.core.paginator import Paginator

# Create your views here.

# Para País

class PaisListView(LoginRequiredMixin, ListView):
    model = Pais
    template_name = 'pais/pais_list.html'
    context_object_name = 'paises'
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.view_pais'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_add'] = self.request.user.has_perm('Catalogo.add_pais')
        context['can_change'] = self.request.user.has_perm('Catalogo.change_pais')
        context['can_delete'] = self.request.user.has_perm('Catalogo.delete_pais')

        # Paginación
        paginator = Paginator(context['paises'], 5)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        # Total de páginas
        context['total_pages'] = paginator.num_pages
        return context
    
class PaisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.add_pais'

class PaisUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.change_pais'

class PaisDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Pais
    template_name = 'pais/pais_delete.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.delete_pais'

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PaisSerializer, DepartamentoSerializer, MunicipioSerializer
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
        queryset = super().get_queryset().order_by('nombre')
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

# Para Departamento

class DepartamentoListView(LoginRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamento/departamento_list.html'
    context_object_name = 'departamentos'
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.view_departamento'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('pais')
        search_query = self.request.GET.get('search')
        pais_id = self.request.GET.get('pais')
        active = self.request.GET.get('active')

        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)

        if pais_id:
            queryset = queryset.filter(pais__id=pais_id)

        # Verifica si 'active' no es nulo 
        if active == '1':  # Si 'active' es "1", filtra solo los activos
            queryset = queryset.filter(active=True)
        elif active == '0':  # Si 'active' es "0", filtra solo los inactivos
            queryset = queryset.filter(active=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paises'] = Pais.objects.all()
        context['can_add'] = self.request.user.has_perm('Catalogo.add_departamento')
        context['can_change'] = self.request.user.has_perm('Catalogo.change_departamento')
        context['can_delete'] = self.request.user.has_perm('Catalogo.delete_departamento')

        # Paginación
        paginator = Paginator(context['departamentos'], 5)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        # Total de páginas
        context['total_pages'] = paginator.num_pages
        return context
    
class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class DepartamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.add_departamento'

class DepartamentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.change_departamento'

class DepartamentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_delete.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.delete_departamento'

# Para Municipio

class MunicipioListView(LoginRequiredMixin, ListView):
    model = Municipio
    template_name = 'municipio/municipio_list.html'
    context_object_name = 'municipios'
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.view_municipio'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('departamento')
        search_query = self.request.GET.get('search')
        departamento_id = self.request.GET.get('departamento')
        active = self.request.GET.get('active')

        if search_query:
            queryset = queryset.filter(nombre__icontains=search_query)

        if departamento_id:
            queryset = queryset.filter(departamento__id=departamento_id)

        # Verifica si 'active' no es nulo 
        if active == '1':  # Si 'active' es "1", filtra solo los activos
            queryset = queryset.filter(active=True)
        elif active == '0':  # Si 'active' es "0", filtra solo los inactivos
            queryset = queryset.filter(active=False)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departamentos'] = Departamento.objects.all()
        context['can_add'] = self.request.user.has_perm('Catalogo.add_municipio')
        context['can_change'] = self.request.user.has_perm('Catalogo.change_municipio')
        context['can_delete'] = self.request.user.has_perm('Catalogo.delete_municipio')

        # Paginación
        paginator = Paginator(context['municipios'], 5)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        
        # Total de páginas
        context['total_pages'] = paginator.num_pages
        return context
    
class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class MunicipioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.add_municipio'

class MunicipioUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.change_municipio'

class MunicipioDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Municipio
    template_name = 'municipio/municipio_delete.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'Catalogo.delete_municipio'
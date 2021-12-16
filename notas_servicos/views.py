from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import NotaServicoForm
from .models import NotaServico


# Create your views here.
class NotaServicoList(ListView):
    model = NotaServico
    context_object_name = 'lista_notaservico'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.
        servicos = []
        context['servicos'] = servicos
        return context


class NotaServicoCreate(CreateView):
    form_class = NotaServicoForm
    template_name = 'notas_servicos/notaservico_form.html'
    success_url = reverse_lazy('notaservico-list')


class NotaServicoUpdate(UpdateView):
    model = NotaServico
    form_class = NotaServicoForm
    template_name = 'notas_servicos/notaservico_form.html'
    success_url = reverse_lazy('notaservico-list')
    

class NotaServicoDelete(DeleteView):
    model = NotaServico
    success_url = reverse_lazy('notaservico-cliente')

from django.views.generic import CreateView
from .models import Vinicula
from .forms import ViniculaForm
from django.shortcuts import render, redirect

class MessageView(CreateView):
    model = Vinicula
    fields = ('nomeVinicula', 'endereco', 'vinho', 'produtor')
    template_name = 'vinicula/index.html'

    def post(self, request, *args, **kwargs):
        form = ViniculaForm(data=request.POST)

        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.save()
            return redirect('vinicula:vinicula_index')
        return self.render_to_response({'from', form})
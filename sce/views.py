from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import IntegrityError
from django.views.generic.edit import CreateView
from .models import *
from .forms import ManutencaoForm



class Create_Equipamento(CreateView):
    model = Ativos_TI
    template_name = 'ativos_ti/ativos_ti_form.html'
    fields = '__all__'

    def form_valid(self, form):
        try:
            form.save()
            return HttpResponseRedirect('/maquinas/listascanner')
        except IntegrityError:
            return HttpResponse("Duplicado")


def create_manutencao(request, pk):
    equipamento = get_object_or_404(Ativos_TI, pk=pk)
    form = ManutencaoForm()

    if request.method == "POST":
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.equipamento = equipamento
            manutencao.save()

            # messages.success(request, "Manutencao cadastrada")
    return render(request, "ativos_ti/manutencao_form.html", locals())

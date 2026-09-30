from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import ProdutorForm, ReceitaForm, DespesaForm, DocumentoForm
from .models import Produtor, Contabilidade, Receita, Despesa, Documento

def get_produtor(user):
    produtor, _ = Produtor.objects.get_or_create(
        usuario=user,
        defaults={"nome": user.get_full_name() or user.username}
    )
    return produtor

@login_required
def dashboard(request):

    # Se o usuário for da contabilidade,
    # mostra o painel específico da contabilidade.
    if hasattr(request.user, "contabilidade"):
        contabilidade = request.user.contabilidade

        return render(request, "contabilidade_dashboard.html", {
            "contabilidade": contabilidade,
            "produtores": contabilidade.produtores.all(),
        })

    # Caso contrário, continua funcionando como produtor.
    produtor = get_produtor(request.user)

    receitas = Receita.objects.filter(produtor=produtor)
    despesas = Despesa.objects.filter(produtor=produtor)

    total_receitas = sum(
        (x.valor for x in receitas),
        Decimal("0")
    )

    total_despesas = sum(
        (x.valor for x in despesas),
        Decimal("0")
    )

    saldo = total_receitas - total_despesas

    return render(request, "dashboard.html", {
        "produtor": produtor,
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo": saldo,
        "qtd_documentos": Documento.objects.filter(
            produtor=produtor
        ).count(),
        "ultimas_receitas": receitas[:5],
        "ultimas_despesas": despesas[:5],
    })
@login_required
def contabilidade_produtor(request, pk):
    contabilidade = get_object_or_404(
        Contabilidade,
        usuario=request.user
    )

    produtor = get_object_or_404(
        contabilidade.produtores,
        pk=pk
    )

    receitas = Receita.objects.filter(produtor=produtor)
    despesas = Despesa.objects.filter(produtor=produtor)
    documentos = Documento.objects.filter(produtor=produtor)

    total_receitas = sum(
        (x.valor for x in receitas),
        Decimal("0")
    )

    total_despesas = sum(
        (x.valor for x in despesas),
        Decimal("0")
    )

    saldo = total_receitas - total_despesas

    return render(request, "contabilidade_produtor.html", {
        "contabilidade": contabilidade,
        "produtor": produtor,
        "receitas": receitas,
        "despesas": despesas,
        "documentos": documentos,
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo": saldo,
    })
@login_required
def relatorio_produtor(request, pk):
    contabilidade = get_object_or_404(
        Contabilidade,
        usuario=request.user
    )

    produtor = get_object_or_404(
        Produtor,
        pk=pk,
        contabilidades=contabilidade
    )

    receitas = Receita.objects.filter(produtor=produtor)
    despesas = Despesa.objects.filter(produtor=produtor)
    documentos = Documento.objects.filter(produtor=produtor)

    total_receitas = sum(
        (x.valor for x in receitas),
        Decimal("0")
    )

    total_despesas = sum(
        (x.valor for x in despesas),
        Decimal("0")
    )

    saldo = total_receitas - total_despesas

    return render(request, "relatorio_produtor.html", {
        "produtor": produtor,
        "receitas": receitas,
        "despesas": despesas,
        "documentos": documentos,
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo": saldo,
    })
@login_required
def cadastro_produtor(request):
    produtor = get_produtor(request.user)
    if request.method == "POST":
        form = ProdutorForm(request.POST, instance=produtor)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro atualizado com sucesso!")
            return redirect("dashboard")
    else:
        form = ProdutorForm(instance=produtor)
    return render(request, "form.html", {"form": form, "titulo": "Meu cadastro", "voltar": "/"})

@login_required
def receitas(request):
    produtor = get_produtor(request.user)
    return render(request, "lista.html", {
        "titulo": "Receitas",
        "itens": Receita.objects.filter(produtor=produtor),
        "novo_url": "nova_receita",
        "tipo": "receita",
    })

@login_required
def nova_receita(request):
    produtor = get_produtor(request.user)
    form = ReceitaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False)
        item.produtor = produtor
        item.save()
        return redirect("receitas")
    return render(request, "form.html", {"form": form, "titulo": "Nova receita", "voltar": "/receitas/"})

@login_required
def excluir_receita(request, pk):
    item = get_object_or_404(Receita, pk=pk, produtor=get_produtor(request.user))
    if request.method == "POST":
        item.delete()
    return redirect("receitas")

@login_required
def despesas(request):
    produtor = get_produtor(request.user)
    return render(request, "lista.html", {
        "titulo": "Despesas",
        "itens": Despesa.objects.filter(produtor=produtor),
        "novo_url": "nova_despesa",
        "tipo": "despesa",
    })

@login_required
def nova_despesa(request):
    produtor = get_produtor(request.user)
    form = DespesaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False)
        item.produtor = produtor
        item.save()
        return redirect("despesas")
    return render(request, "form.html", {"form": form, "titulo": "Nova despesa", "voltar": "/despesas/"})

@login_required
def excluir_despesa(request, pk):
    item = get_object_or_404(Despesa, pk=pk, produtor=get_produtor(request.user))
    if request.method == "POST":
        item.delete()
    return redirect("despesas")

@login_required
def documentos(request):
    produtor = get_produtor(request.user)
    return render(request, "documentos.html", {
        "documentos": Documento.objects.filter(produtor=produtor)
    })

@login_required
def novo_documento(request):
    produtor = get_produtor(request.user)
    form = DocumentoForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False)
        item.produtor = produtor
        item.save()
        return redirect("documentos")
    return render(request, "form.html", {"form": form, "titulo": "Novo documento", "voltar": "/documentos/"})

@login_required
def excluir_documento(request, pk):
    item = get_object_or_404(Documento, pk=pk, produtor=get_produtor(request.user))
    if request.method == "POST":
        if item.arquivo:
            item.arquivo.delete(save=False)
        item.delete()
    return redirect("documentos")

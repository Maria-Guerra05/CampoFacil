from django import forms
from .models import Produtor, Receita, Despesa, Documento

class ProdutorForm(forms.ModelForm):
    email = forms.EmailField(
        label="E-mail",
        required=False,
        widget=forms.EmailInput(attrs={"class": "input", "placeholder": "Ex.: produtor@email.com"}),
        help_text="Usado para contato e, futuramente, recuperação de acesso."
    )

    class Meta:
        model = Produtor
        fields = ["nome", "cpf_cnpj", "propriedade", "telefone", "cidade"]
        labels = {
            "nome": "Nome completo",
            "cpf_cnpj": "CPF ou CNPJ",
            "propriedade": "Nome da propriedade",
            "telefone": "Telefone",
            "cidade": "Município",
        }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: João da Silva"}),
            "cpf_cnpj": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: 000.000.000-00"}),
            "propriedade": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Fazenda Boa Esperança"}),
            "telefone": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: (63) 99999-9999"}),
            "cidade": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Colinas do Tocantins"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.usuario_id:
            self.fields["email"].initial = self.instance.usuario.email

    def save(self, commit=True):
        produtor = super().save(commit=commit)
        produtor.usuario.email = self.cleaned_data.get("email", "")
        produtor.usuario.save(update_fields=["email"])
        return produtor

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["descricao", "valor", "data", "categoria", "observacao"]
        widgets = {
            "descricao": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Venda de milho"}),
            "valor": forms.NumberInput(attrs={"class": "input", "step": "0.01"}),
            "data": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "categoria": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Venda"}),
            "observacao": forms.Textarea(attrs={"class": "input", "rows": 3}),
        }

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ["descricao", "valor", "data", "categoria", "observacao"]
        widgets = {
            "descricao": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Compra de ração"}),
            "valor": forms.NumberInput(attrs={"class": "input", "step": "0.01"}),
            "data": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "categoria": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Insumos"}),
            "observacao": forms.Textarea(attrs={"class": "input", "rows": 3}),
        }

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ["nome", "data", "categoria", "valor", "arquivo", "observacao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Nota fiscal de adubo"}),
            "data": forms.DateInput(attrs={"class": "input", "type": "date"}),
            "categoria": forms.TextInput(attrs={"class": "input", "placeholder": "Ex.: Nota fiscal"}),
            "valor": forms.NumberInput(attrs={"class": "input", "step": "0.01"}),
            "arquivo": forms.ClearableFileInput(attrs={"class": "input"}),
            "observacao": forms.Textarea(attrs={"class": "input", "rows": 3}),
        }

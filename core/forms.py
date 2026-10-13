
from django import forms
from .models import Produtor, Receita, Despesa, Documento


# Categorias disponíveis para receitas
CATEGORIAS_RECEITA = [
    ("", "Selecione uma categoria"),
    ("Venda de animais", "Venda de animais"),
    ("Venda de produtos agrícolas", "Venda de produtos agrícolas"),
    ("Venda de leite e derivados", "Venda de leite e derivados"),
    ("Prestação de serviços", "Prestação de serviços"),
    ("Outras receitas", "Outras receitas"),
]


# Categorias disponíveis para despesas
CATEGORIAS_DESPESA = [
    ("", "Selecione uma categoria"),
    ("Alimentação animal", "Alimentação animal"),
    ("Insumos agrícolas", "Insumos agrícolas"),
    ("Medicamentos veterinários", "Medicamentos veterinários"),
    ("Combustível", "Combustível"),
    ("Manutenção e equipamentos", "Manutenção e equipamentos"),
    ("Mão de obra", "Mão de obra"),
    ("Outras despesas", "Outras despesas"),
]


# Categorias disponíveis para documentos
CATEGORIAS_DOCUMENTO = [
    ("", "Selecione uma categoria"),
    ("Nota fiscal", "Nota fiscal"),
    ("Recibo", "Recibo"),
    ("Comprovante de pagamento", "Comprovante de pagamento"),
    ("Contrato", "Contrato"),
    ("Outros documentos", "Outros documentos"),
]


class ProdutorForm(forms.ModelForm):

    email = forms.EmailField(
        label="E-mail",
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "input",
                "placeholder": "Ex.: produtor@email.com"
            }
        ),
        help_text="Usado para contato e, futuramente, recuperação de acesso."
    )

    class Meta:
        model = Produtor

        fields = [
            "nome",
            "cpf_cnpj",
            "propriedade",
            "telefone",
            "cidade",
        ]

        labels = {
            "nome": "Nome completo",
            "cpf_cnpj": "CPF ou CNPJ",
            "propriedade": "Nome da propriedade",
            "telefone": "Telefone",
            "cidade": "Município",
        }

        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: João da Silva"
                }
            ),
            "cpf_cnpj": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: 000.000.000-00"
                }
            ),
            "propriedade": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: Fazenda Boa Esperança"
                }
            ),
            "telefone": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: (63) 99999-9999"
                }
            ),
            "cidade": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: Colinas do Tocantins"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.usuario_id:
            self.fields["email"].initial = self.instance.usuario.email

    def save(self, commit=True):
        produtor = super().save(commit=commit)

        if commit:
            produtor.usuario.email = self.cleaned_data.get("email", "")
            produtor.usuario.save(update_fields=["email"])

        return produtor


class ReceitaForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        label="Categoria",
        choices=CATEGORIAS_RECEITA,
        required=False,
        widget=forms.Select(
            attrs={"class": "input"}
        )
    )

    class Meta:
        model = Receita

        fields = [
            "categoria",
            "descricao",
            "valor",
            "data",
        ]

        labels = {
            "descricao": "Descrição",
            "valor": "Valor",
            "data": "Data",
        }

        widgets = {
            "descricao": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: Venda de 2 bois"
                }
            ),
            "valor": forms.NumberInput(
                attrs={
                    "class": "input",
                    "step": "0.01",
                    "min": "0.01"
                }
            ),
            "data": forms.DateInput(
                attrs={
                    "class": "input",
                    "type": "date"
                }
            ),
        }

    def clean_valor(self):
        valor = self.cleaned_data["valor"]

        if valor <= 0:
            raise forms.ValidationError(
                "O valor da receita deve ser maior que zero."
            )

        return valor


class DespesaForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        label="Categoria",
        choices=CATEGORIAS_DESPESA,
        required=False,
        widget=forms.Select(
            attrs={"class": "input"}
        )
    )

    class Meta:
        model = Despesa

        fields = [
            "categoria",
            "descricao",
            "valor",
            "data",
        ]

        labels = {
            "descricao": "Descrição",
            "valor": "Valor",
            "data": "Data",
        }

        widgets = {
            "descricao": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: Compra de 20 sacos de ração"
                }
            ),
            "valor": forms.NumberInput(
                attrs={
                    "class": "input",
                    "step": "0.01",
                    "min": "0.01"
                }
            ),
            "data": forms.DateInput(
                attrs={
                    "class": "input",
                    "type": "date"
                }
            ),
        }

    def clean_valor(self):
        valor = self.cleaned_data["valor"]

        if valor <= 0:
            raise forms.ValidationError(
                "O valor da despesa deve ser maior que zero."
            )

        return valor


class DocumentoForm(forms.ModelForm):

    categoria = forms.ChoiceField(
        label="Categoria",
        choices=CATEGORIAS_DOCUMENTO,
        required=False,
        widget=forms.Select(
            attrs={"class": "input"}
        )
    )

    class Meta:
        model = Documento

        fields = [
            "nome",
            "data",
            "categoria",
            "valor",
            "arquivo",
            "observacao",
        ]

        widgets = {
            "nome": forms.TextInput(
                attrs={
                    "class": "input",
                    "placeholder": "Ex.: Nota fiscal de adubo"
                }
            ),
            "data": forms.DateInput(
                attrs={
                    "class": "input",
                    "type": "date"
                }
            ),
            "valor": forms.NumberInput(
                attrs={
                    "class": "input",
                    "step": "0.01",
                    "min": "0.01"
                }
            ),
            "arquivo": forms.ClearableFileInput(
                attrs={
                    "class": "input",
                    "accept": ".pdf,.jpg,.jpeg,.png"
                }
            ),
            "observacao": forms.Textarea(
                attrs={
                    "class": "input",
                    "rows": 3
                }
            ),
        }

    def clean_valor(self):
        valor = self.cleaned_data.get("valor")

        if valor is not None and valor <= 0:
            raise forms.ValidationError(
                "O valor do documento deve ser maior que zero."
            )

        return valor

    def clean_arquivo(self):
        arquivo = self.cleaned_data.get("arquivo")

        if not arquivo:
            raise forms.ValidationError(
                "Selecione um arquivo para enviar."
            )

        extensoes_permitidas = [
            ".pdf",
            ".jpg",
            ".jpeg",
            ".png"
        ]

        nome = arquivo.name.lower()

        if not any(
            nome.endswith(ext)
            for ext in extensoes_permitidas
        ):
            raise forms.ValidationError(
                "Formato não permitido. "
                "Envie um arquivo PDF, JPG, JPEG ou PNG."
            )

        tamanho_maximo = 10 * 1024 * 1024

        if arquivo.size > tamanho_maximo:
            raise forms.ValidationError(
                "O arquivo é muito grande. "
                "O tamanho máximo permitido é 10 MB."
            )

        return arquivo

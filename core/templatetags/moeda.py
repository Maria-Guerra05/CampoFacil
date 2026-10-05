from django import template

register = template.Library()


@register.filter
def moeda_br(valor):
    try:
        valor_formatado = f"{valor:,.2f}"
        valor_formatado = (
            valor_formatado
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        return f"R$ {valor_formatado}"
    except (ValueError, TypeError):
        return "R$ 0,00"
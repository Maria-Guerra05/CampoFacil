from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
    path(
    "contabilidade/produtor/<int:pk>/",
    views.contabilidade_produtor,
    name="contabilidade_produtor"),
    path("cadastro/", views.cadastro_produtor, name="cadastro_produtor"),
    path("receitas/", views.receitas, name="receitas"),
    path("receitas/nova/", views.nova_receita, name="nova_receita"),
    path("receitas/excluir/<int:pk>/", views.excluir_receita, name="excluir_receita"),
    path("despesas/", views.despesas, name="despesas"),
    path("despesas/nova/", views.nova_despesa, name="nova_despesa"),
    path("despesas/excluir/<int:pk>/", views.excluir_despesa, name="excluir_despesa"),
    path("documentos/", views.documentos, name="documentos"),
    path("documentos/novo/", views.novo_documento, name="novo_documento"),
    path(
    "documentos/visualizar/<int:pk>/",
    views.visualizar_documento,
    name="visualizar_documento",
),
    path("documentos/excluir/<int:pk>/", views.excluir_documento, name="excluir_documento"),
    path(
    "contabilidade/produtor/<int:pk>/relatorio/",
    views.relatorio_produtor,
    name="relatorio_produtor"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from .models import Product   # 👈 importamos el modelo


# Home
def homePageView(request):
    return render(request, "pages/home.html")


# About
class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Sobre nosotros - Tienda Online",
            "subtitle": "Sobre nosotros",
            "description": "Esta es la página de información de la tienda...",
            "author": "Desarrollado por: Mariana García",
        })
        return context


# Lista de productos
class ProductIndexView(View):
    template_name = "products/index.html"

    def get(self, request):
        viewData = {}
        viewData["title"] = "Productos - Tienda Online"
        viewData["subtitle"] = "Lista de productos"
        viewData["products"] = Product.objects.all()   # 👈 ahora vienen de la BD
        return render(request, self.template_name, viewData)


# Detalle de producto
class ProductShowView(View):
    template_name = "products/show.html"

    def get(self, request, id):
        viewData = {}
        product = Product.objects.get(pk=id)   # 👈 buscamos por id en la BD
        viewData["title"] = product.name + " - Tienda Online"
        viewData["subtitle"] = product.name + " - Información del producto"
        viewData["product"] = product
        return render(request, self.template_name, viewData)

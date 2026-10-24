"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings


def react_app(request, **kwargs):
    """Serve the compiled React single-page application."""
    index_path = os.path.join(
        settings.BASE_DIR, 'frontend', 'build', 'index.html')
    with open(index_path, 'r', encoding='utf-8') as index_file:
        return HttpResponse(index_file.read(), content_type='text/html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('about', TemplateView.as_view(template_name="About.html"),
         name='about'),
    path('contact', TemplateView.as_view(template_name="Contact.html"),
         name='contact'),
    # React routes
    path('login', react_app, name='login_page'),
    path('register', react_app, name='register_page'),
    path('dealers', react_app, name='dealers_page'),
    path('dealer/<int:dealer_id>', react_app, name='dealer_page'),
    path('postreview/<int:dealer_id>', react_app, name='postreview_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

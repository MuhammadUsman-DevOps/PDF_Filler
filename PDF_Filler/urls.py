"""PDF_Filler URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from PDF_Filler import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('test/', views.test, name="test"),
    path('co-trust-protector-only-default-ebinder/', views.co_trust_protector_only_default_ebinder,
         name="co_trust_protector_only_default_ebinder"),
    path('co-trustee-co-protector-default-ebinder/', views.co_trustee_co_protector_default_ebinder,
         name="co_trustee_co_protector_default_ebinder")
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

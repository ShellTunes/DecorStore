from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.views.generic import TemplateView
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.documentation import include_docs_urls
from django.views.static import serve
# schema_view = get_swagger_view(title='The Glass Decor')

urlpatterns = [
    # url(r'^swagger/docs/', schema_view),
    # url(r'^docs/', include_docs_urls(title='The DecorStore Documentations')),
    path('', admin.site.urls),
    path('',include('DecorStoreApp.urls')),
    # url(r'^advanced_filters/', include('advanced_filters.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
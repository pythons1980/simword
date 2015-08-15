from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib import admin


from simword.views import StringListCreateView, SearchView, SearchRESTView, StringListRESTView


urlpatterns = patterns('',
                       url(r'^$', StringListCreateView.as_view(), name='stringlist_input'),
                       url(r'^search/(?P<q>.*)', SearchView.as_view(), name='search'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/string-list/search/(?P<q>.*)$', SearchRESTView.as_view()),
                       url(r'^api/string-list$', StringListRESTView.as_view()),
    )
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

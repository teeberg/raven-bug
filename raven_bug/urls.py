from django.conf.urls import include, url
from tastypie.api import Api

from .api import EntryResource, ThingResource

v1_api = Api(api_name='v1')
v1_api.register(EntryResource())
v1_api.register(ThingResource())

urlpatterns = [
    # The normal jazz here then...
    url(r'^api/', include(v1_api.urls)),
]

from tastypie.resources import ModelResource

from .models import Entry, Thing


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()


class ThingResource(ModelResource):
    class Meta:
        queryset = Thing.objects.all()

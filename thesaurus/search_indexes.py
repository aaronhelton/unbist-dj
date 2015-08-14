from django.conf import settings
from django.utils import translation
from haystack import indexes
from .models import Resource
from .models import Property
from .models import Relationship

class ResourceIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    resource_type = indexes.CharField(model_attr='resource_type', faceted=True)
    content_auto = indexes.NgramField(model_attr='prefLabel')
    pref_labels = indexes.CharField(model_attr='all_preferred_labels', boost=2.0)
    alt_labels = indexes.CharField(model_attr='all_alternate_labels', boost=1.5)
    scope_notes = indexes.CharField(model_attr='all_scope_notes')
    #relationships = indexes.CharField(model_attr='all_relationships')
    
    def get_model(self):
        return Resource
        
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
        
#class PropertyIndex(indexes.SearchIndex,indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#    property_type = indexes.CharField(model_attr='property_type', faceted=True)
#    
#    def get_model(self):
#        return Property
#        
#    def index_queryset(self, using=None):
#        return self.get_model().objects.all()
#        
#class RelationshipIndex(indexes.SearchIndex,indexes.Indexable):
#    text = indexes.CharField(document=True, use_template=True)
#    relationship_type = indexes.CharField(model_attr='relationship_type', faceted=True)
#    
#    def get_model(self):
#        return Relationship
#        
#    def index_queryset(self, using=None):
#        return self.get_model().objects.all()
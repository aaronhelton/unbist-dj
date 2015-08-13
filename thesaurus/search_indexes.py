from haystack import indexes
from .models import Resource
from .models import Property
from .models import Relationship

class ResourceIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    resource_type = indexes.CharField(model_attr='resource_type', faceted=True)
    content_auto = indexes.NgramField(model_attr='prefLabel')
    
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
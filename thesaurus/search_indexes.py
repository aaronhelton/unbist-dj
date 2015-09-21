from haystack import indexes
from thesaurus.models import Concept, Collection, ConceptScheme

class ConceptIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, boost=1.0)
    labels = indexes.NgramField(use_template=True, boost=2.0)
    notes = indexes.NgramField(use_template=True, boost=1.125)
    relationships = indexes.NgramField(use_template=True, boost=1.125)
    resource_type = indexes.CharField(model_attr='resource_type')
    text_auto = indexes.NgramField(use_template=True)

    def get_model(self):
        return Concept

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class CollectionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    text_auto = indexes.NgramField(use_template=True)

    def get_model(self):
        return Collection

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

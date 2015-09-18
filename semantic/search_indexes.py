from haystack import indexes
from semantic.models import Resource

class ResourceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    text_auto = indexes.NgramField(use_template=True)

    def get_model(self):
        return Resource

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

from django.db import models
from django.db.utils import OperationalError, ProgrammingError
import semantic
from semantic.models import Resource, Relationship, Property, Match, OwlSuper, Prefix

# Create your models here.

#Managers for proxy models
class PreferredLabelManager(models.Manager):
    def get_queryset(self):
        return super(PreferredLabelManager, self).get_queryset().filter(
            property_type = OwlSuper.objects.get(name='prefLabel').id
        )

class AlternateLabelManager(models.Manager):
    def get_queryset(self):
        return super(AlternateLabelManager, self).get_queryset().filter(
            property_type = OwlSuper.objects.get(name='altLabel').id
        )

class ScopeNoteManager(models.Manager):
    def get_queryset(self):
        return super(ScopeNoteManager, self).get_queryset().filter(
            property_type = OwlSuper.objects.get(name='scopeNote').id
        )

class ConceptManager(models.Manager):
    def get_queryset(self):
        return super(ConceptManager, self).get_queryset().filter(
            resource_type = OwlSuper.objects.get(name='Concept').id
        )
class CollectionManager(models.Manager):
    def get_queryset(self):
        return super(CollectionManager, self).get_queryset().filter(
            resource_type = OwlSuper.objects.get(name='Collection').id
        )

class ConceptSchemeManager(models.Manager):
    def get_queryset(self):
        return super(ConceptSchemeManager, self).get_queryset().filter(
            resource_type = OwlSuper.objects.get(name='ConceptScheme').id
        )


#Proxy models from semantic.models
class Concept(Resource):
    objects = ConceptManager()

    class Meta:
        proxy = True
        app_label = "thesaurus"
  
    # The following try/except prevents the manage.py script from failing in case
    # migrations have not already succeeded. Since manage.py is how you invoke 
    # the migrations in the first place, it is essential that the script work.
    try:
        res_type = OwlSuper.objects.get(name='Concept').id
    except OperationalError:
        res_type = None
    except OwlSuper.DoesNotExist:
        res_type = None
    except ProgrammingError:
        res_type = None

    def create(cls, resource_type=res_type):
        concept = cls(resource_type=resource_type)
        return concept

    #def get_absolute_url(self):
    #    from django.core.urlresolvers import reverse
        #return reverse('thesaurus:detail', kwargs={'uri': self.uri})
        # below is wrong, but above doesn't work yet...
    #    return "/thesaurus/%i/" % self.uri

class Collection(Resource):
    objects = CollectionManager()

    class Meta:
        proxy = True
        app_label = "thesaurus"

class ConceptScheme(Resource):
    objects = ConceptSchemeManager()

    class Meta:
        proxy = True
        app_label = "thesaurus"

class PreferredLabel(Property):
    objects = PreferredLabelManager()

    class Meta:
        proxy = True
        app_label = "thesaurus"

class AlternateLabel(Property):
    objects = AlternateLabelManager()

    class Meta:
        proxy = True
        app_label = "thesaurus"

class ScopeNote(Property):
    objects = ScopeNoteManager()

    class Meta:
        proxy = True
        app_label = "thesaurus"


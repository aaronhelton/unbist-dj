from django.db import models
from django.utils import translation

# Create your models here.
class Resource(models.Model):
    LABEL_CLASS = 'skos:prefLabel'
    SKOS_CLASSES = (
        ('skos:ConceptScheme','Concept Scheme'),
        ('skos:Concept', 'Concept'),
        ('skos:Collection', 'Collection'),
        ('skos:OrderedCollection', 'Ordered Collection')
    )
    uri = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=200,choices=SKOS_CLASSES)
    
    
    #object_properties = models.ManyToManyField('Relationship', blank=True)
    #datatype_properties = models.ManyToManyField('Property', blank=True)
    
    def prefLabel(self):
        current_language = translation.get_language()
        # the Django way appears to be through try/except/etc. This will work, though.
        r = Property.objects.filter(property_source=self, property_type=self.LABEL_CLASS, property_language=current_language)
        r_fallback = Property.objects.filter(property_source=self, property_type=self.LABEL_CLASS, property_language='en')
        
        if r.count() > 0:
            return r[0].property_text
        elif r_fallback.count > 0:
            return r_fallback[0].property_text
        else:
            return self.uri
    
    def __unicode__(self):
        return self.prefLabel()
        
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('thesaurus:detail', kwargs={'uri': self.uri})
        
class Relationship(models.Model):
    SKOS_RELATIONSHIPS = (
        ('skos:inScheme', 'is included in Concept Scheme'),
        ('skos:hasTopConcept', 'has top Concept'),
        ('skos:topConceptOf', 'is a top Concept of'),
        ('skos:member', 'has member Concept'),
        ('skos:broader', 'has broader Concept'),
        ('skos:related', 'has related Concept'),
        ('skos:narrower', 'has narrower Concept')
    )
    relationship_source = models.ForeignKey('Resource')
    relationship_type = models.CharField(max_length=200, choices=SKOS_RELATIONSHIPS)
    relationship_target = models.ForeignKey('Resource', verbose_name='Target Resource', related_name='target_of')
    
    def __unicode__(self):
        return self.relationship_source.__str__() + ' ' + self.relationship_type + ' ' + self.relationship_target.__str__()
    
class Match(models.Model):
    # This is to handle external matches as opposed to internal relationships
    SKOS_MATCHES = (
        ('skos:broadMatch', 'has broad match'),
        ('skos:relatedMatch', 'has related match'),
        ('skos:narrowMatch', 'has narrow match'),
        ('skos:closeMatch', 'has close match'),
        ('skos:exactMatch', 'has exact match')
    )
    match_source = models.ForeignKey('Resource')
    match_type = models.CharField(max_length=200, choices=SKOS_MATCHES)
    match_target = models.URLField()
    
    class Meta:
        verbose_name_plural = 'matches'
    
    def __unicode__(self):
        return self.match_source + ' ' + self.match_type + ' ' + self.match_target
    
class Property(models.Model):
    SKOS_PROPERTIES = (
        ('skos:prefLabel', 'has preferred label'),
        ('skos:altLabel', 'has alternate label (UF)'),
        ('skos:hiddenLabel', 'has hidden label'),
        ('skos:notation', 'has notation'),
        ('skos:note', 'has note'),
        ('skos:changeNote', 'has change note'),
        ('skos:definition', 'has definition'),
        ('skos:editorialNote', 'has editorial note'),
        ('skos:example', 'has example'),
        ('skos:historyNote', 'has history note'),
        ('skos:scopeNote', 'has scope note')
    )
    property_source = models.ForeignKey('Resource')
    property_text = models.CharField(max_length=200)
    property_language = models.CharField(max_length=2)
    property_type = models.CharField(max_length=200, choices=SKOS_PROPERTIES)
    
    class Meta:
        verbose_name_plural = 'properties'
        ordering = ['property_type','property_language','property_text']
    
    def __unicode__(self):
        return_string = self.property_type + ' ' + self.property_text
        
        if self.property_language is not None:
            return_string += '@' + self.property_language
            
        return return_string

class ConceptManager(models.Manager):
    def get_queryset(self):
        return super(ConceptManager, self).get_queryset().filter(
            resource_type='skos:Concept')
        
class Concept(Resource):
    objects = ConceptManager()
        
    class Meta:
        proxy = True
        
    @classmethod
    def create(cls, resource_type='skos:Concept'):
        concept = cls(resource_type=resource_type)
        return concept

#Can I make this more DRY?        
class PrefLabelManager(models.Manager):
    def get_queryset(self):
        return super(PrefLabelManager, self).get_queryset().filter(
            property_type='skos:prefLabel'
        )
        
class PrefLabel(Property):
    objects = PrefLabelManager()
    
    class Meta:
        proxy = True
        verbose_name = 'Preferred Label'
        verbose_name_plural = 'Preferred Labels'
        
    @classmethod
    def create(cls, property_type='skos:prefLabel'):
        label = cls(property_type=property_type)
        return label
        
class AltLabelManager(models.Manager):
    def get_queryset(self):
        return super(AltLabelManager, self).get_queryset().filter(
            property_type='skos:altLabel'
        )
        
class AltLabel(Property):
    objects = AltLabelManager()
    
    class Meta:
        proxy = True
        verbose_name = 'Alternate Label'
        verbose_name_plural = 'Alternate Labels'
        
    @classmethod
    def create(cls, property_type='skos:altLabel'):
        label = cls(property_type=property_type)
        return label

class ConceptSchemeManager(models.Manager):
    def get_queryset(self):
        return super(ConceptSchemeManager, self).get_queryset().filter(
            resource_type='skos:ConceptScheme'
        )
        
class ConceptScheme(Resource):
    objects = ConceptSchemeManager()
    
    class Meta:
        proxy = True
        
    @classmethod
    def create(cls, resource_type='skos:ConceptScheme'):
        concept_scheme = cls(resource_type=resource_type)
        return concept_scheme
        
class CollectionManager(models.Manager):
    def get_queryset(self):
        return super(CollectionManager, self).get_queryset().filter(
            resource_type='skos:Collection'
        )
            
class Collection(Resource):
    objects = CollectionManager()
    
    class Meta:
        proxy = True
        
    @classmethod
    def create(cls, resource_type='skos:Collection'):
        collection = cls(resource_type=resource_type)
        return collection
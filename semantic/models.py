from django.db import models
from django.db.models import Q
from django.db.models.base import ObjectDoesNotExist
from django.conf import settings
from django.utils import translation
from django.core.urlresolvers import reverse

# Create your models here.
class Prefix(models.Model):
    name = models.CharField(max_length=200)
    uri = models.URLField()

    class Meta:
        verbose_name_plural = 'prefixes'

    def __unicode__(self):
        return self.name

    def turtle(self):
        return "@prefix " + self.name + ": <" + self.uri + "> ."

class OwlSuper(models.Model):
    OWL_TYPES = (
        ('owl:Class','Class'),
        ('owl:DatatypeProperty','DatatypeProperty'),
        ('owl:ObjectProperty','ObjectProperty'),
    )
    prefix = models.ForeignKey('Prefix')
    owl_type = models.CharField(max_length=200,choices=OWL_TYPES)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.prefix.__str__() + ':' + self.name

    def uri(self):
        return self.prefix.uri + '#' + self.name

class Resource(models.Model):
    uri = models.CharField(max_length=200)
    resource_type = models.ForeignKey('OwlSuper', limit_choices_to={'owl_type': 'owl:Class'})
    label_class = models.ForeignKey('OwlSuper', related_name='label_class', limit_choices_to=Q(name__icontains='label') | Q(name__icontains='title'))

    def pref_label(self):
        #Get the preferred label for whatever the current language is
        current_language = translation.get_language()
        try:
            label = Property.objects.get(Q(property_source=self) & Q(property_type=self.label_class) & Q(property_language=current_language))
        except Property.DoesNotExist:
            try:
                label = Property.objects.get(Q(property_source=self) & Q(property_type=self.label_class) & Q(property_language=settings.LANGUAGE_CODE))
            except Property.DoesNotExist:
                try:
                    label = Property.objects.get(Q(property_source=self) & Q(property_type=self.label_class))
                except Property.DoesNotExist:
                    return self.uri
                else:
                    return label.property_text
                #return self.uri
            else:
                return label.property_text
        else:
            return label.property_text
            
    def __unicode__(self):
        return self.pref_label()

    def get_absolute_url(self):
        return reverse('semantic.views.detail', kwargs={'uri': self.uri})

    def turtle(self):
        # only return the type declaration; properties and relationships can be done separately
        # a base uri prefix needs to be registered in Prefixes, aliased to _
        return "_:" + self.uri + " a " + self.resource_type.__unicode__()

class Relationship(models.Model):
    relationship_source = models.ForeignKey('Resource')
    relationship_type = models.ForeignKey('OwlSuper', limit_choices_to=Q(owl_type='owl:ObjectProperty') & ~Q(name__icontains='match'))
    relationship_target = models.ForeignKey('Resource', verbose_name='Target Resource', related_name='target_of')

    def __unicode__(self):
        return self.relationship_source.__str__() + ' ' + self.relationship_type.__str__() + ' ' + self.relationship_target.__str__()

    def turtle(self):
        return self.relationship_type.__unicode__() + " _:" + self.relationship_target.uri

class Property(models.Model):
    property_source = models.ForeignKey('Resource')
    property_text = models.TextField()
    property_language = models.CharField(max_length=2,choices=settings.LANGUAGES)
    property_type = models.ForeignKey('OwlSuper', limit_choices_to={'owl_type': 'owl:DatatypeProperty'})

    class Meta:
        verbose_name_plural = 'properties'
        ordering = ['property_type','property_language','property_text']

    def __unicode__(self):
        return_string = self.property_type.__str__() + ' "' + self.property_text + '"'
        
        if self.property_language:
            return_string += '@' + self.property_language
            
        return return_string

    def turtle(self):
        return self.__unicode__()

class Match(models.Model):
    match_source = models.ForeignKey('Resource')
    match_type = models.ForeignKey('OwlSuper', limit_choices_to=Q(owl_type='owl:ObjectProperty') & Q(name__icontains='match'))
    match_target = models.URLField(null=True, blank=True)
    match_internal_model = models.CharField(max_length=200, null=True, blank=True)
    match_internal_view = models.CharField(max_length=200, null=True, blank=True)
    match_internal_uri = models.CharField(max_length=200, null=True, blank=True)
    resolve_label = models.BooleanField()

    class Meta:
        verbose_name_plural = 'matches'

    def __unicode__(self):
        return self.match_source + ' ' + self.match_type + ' ' + self.match_target

    def internal_scope(self):
        return self.match_internal_model + ':' + self.match_internal_view
    #to do: create a general purpose label resolver that takes in a match target URI and attempts to return an appropriate label
    # This might be better achieved outside the program, however...

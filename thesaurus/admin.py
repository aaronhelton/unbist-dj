from django.contrib import admin

# Register your models here.
#Base models
from .models import Resource
from .models import Relationship
from .models import Property
from .models import Match

#Proxy models
from .models import Concept
from .models import PrefLabel
from .models import AltLabel
from .models import Collection
from .models import ConceptScheme

class RelationshipInline(admin.TabularInline):
    model = Relationship
    fk_name = 'relationship_source'
    extra = 1
    
class MatchInline(admin.TabularInline):
    model = Match
    fk_name = 'match_source'
    extra = 0
    
class PropertyInline(admin.TabularInline):
    model = Property
    fk_name = 'property_source'
    extra = 6

class ResourceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['uri', 'resource_type']})
    ]
    inlines = [PropertyInline,RelationshipInline,MatchInline]

class PrefLabelInline(admin.TabularInline):
    model = PrefLabel
    fk_name = 'property_source'
    extra = 6
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'property_type':
            kwargs['initial'] = 'skos:prefLabel'
            return db_field.formfield(**kwargs)
            
        return super(PrefLabelInline, self).formfield_for_dbfield(db_field, **kwargs)
        
class AltLabelInline(admin.TabularInline):
    model = AltLabel
    fk_name = 'property_source'
    extra = 0
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'property_type':
            kwargs['initial'] = 'skos:altLabel'
            return db_field.formfield(**kwargs)
            
        return super(AltLabelInline, self).formfield_for_dbfield(db_field, **kwargs)

class TopConceptInline(admin.TabularInline):
    model = Relationship
    fk_name = 'relationship_source'
    extra = 0
    
class ConceptAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['uri', 'resource_type']})
    ]
    inlines = [PrefLabelInline,AltLabelInline,RelationshipInline,MatchInline]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'resource_type':
            kwargs['initial'] = 'skos:Concept'
            return db_field.formfield(**kwargs)
            
        return super(ConceptAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        
class ConceptSchemeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['uri', 'resource_type']})
    ]
    inlines = [PrefLabelInline,AltLabelInline,TopConceptInline]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'resource_type':
            kwargs['initial'] = 'skos:ConceptScheme'
            return db_field.formfield(**kwargs)
            
        return super(ConceptSchemeAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        
    

admin.site.register(Resource,ResourceAdmin)
admin.site.register(Relationship)
admin.site.register(Property)
admin.site.register(Match)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(ConceptScheme, ConceptSchemeAdmin)

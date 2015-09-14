from django.contrib import admin

# Register your models here.
from .models import Concept, Collection, ConceptScheme, PreferredLabel, AlternateLabel, ScopeNote
from semantic.models import Relationship, Match, OwlSuper, Prefix
from semantic.admin import RelationshipInline, MatchInline

class PrefLabelInline(admin.TabularInline):
    model = PreferredLabel
    fk_name = 'property_source'
    extra = 1
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'property_type':
            kwargs['initial'] = OwlSuper.objects.get(name='prefLabel').id
#            return db_field.formfield(**kwargs)
            
        return super(PrefLabelInline, self).formfield_for_dbfield(db_field, **kwargs)
        
class AltLabelInline(admin.TabularInline):
    model = AlternateLabel
    fk_name = 'property_source'
    extra = 0
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'property_type':
            kwargs['initial'] = OwlSuper.objects.get(name='altLabel').id
#            return db_field.formfield(**kwargs)
            
        return super(AltLabelInline, self).formfield_for_dbfield(db_field, **kwargs)

class ScopeNoteInline(admin.TabularInline):
    model = ScopeNote
    fk_name = 'property_source'
    extra = 0
    
    def  formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'property_type':
            kwargs['initial'] = OwlSuper.objects.get(name='scopeNote').id
#            return db_field.formfield(**kwargs)

        return super(ScopeNoteInline, self).formfield_for_dbfield(db_field, **kwargs)

class ConceptAdmin(admin.ModelAdmin):
    view_on_site = True
    fieldsets = [
        (None,  {'fields': ['uri', 'resource_type', 'label_class']})
    ]
    inlines = [
        PrefLabelInline,
        AltLabelInline,
        ScopeNoteInline,
        RelationshipInline,
        MatchInline,
    ]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'resource_type':
            kwargs['initial'] = OwlSuper.objects.get(name='Concept').id
            #return db_field.formfield(**kwargs)
            
        return super(ConceptAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Concept, ConceptAdmin)
#admin.site.register(ConceptScheme, ConceptSchemeAdmin)

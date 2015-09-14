from django.contrib import admin

# Register your models here.
from .models import Resource, Relationship, Property, Match, OwlSuper, Prefix

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

admin.site.register(Resource,ResourceAdmin)
admin.site.register(Relationship)
admin.site.register(Property)
admin.site.register(Match)
admin.site.register(OwlSuper)
admin.site.register(Prefix)

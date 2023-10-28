from django.contrib import admin

from .models import Snippet, Tags,  subgoals

class tagInline(admin.TabularInline):
    model = Tags
    extra= 1


class subGoalsInline(admin.TabularInline):
    model = subgoals
    
    extra= 1


""" class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'description', 'on_hold', 'completed','not_started', 'progress' ]}) ]
    inlines = [tagInline, subGoalsInline]

admin.site.register(Snippet, SnippetAdmin)

class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'description', 'on_hold', 'completed','not_started', 'progress' ]}) ]
    inlines = [tagInline, subGoalsInline]

admin.site.register(Snippet, SnippetAdmin) """


class SnippetAdmin(admin.ModelAdmin):
  
    inlines = [tagInline, subGoalsInline]


admin.site.register(Snippet, SnippetAdmin)

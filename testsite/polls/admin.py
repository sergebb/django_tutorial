from django.contrib import admin

# Register your models here.
from polls.models import Poll,Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_yesterday')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll,PollAdmin)
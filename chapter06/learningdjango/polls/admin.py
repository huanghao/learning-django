from django.contrib import admin

from polls.models import Poll, Choice

#
# fields, fieldsets
#

class PollAdmin1(admin.ModelAdmin):

    fields = ['pub_date', 'question']

class PollAdmin2(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['question']}),

        ('Date information', {
                'fields': ['pub_date'],
                'classes': ['collapse']
                }),
        ]


#
# inlines
#

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class PollAdmin3(admin.ModelAdmin):

    inlines = [ChoiceInline]

class ChoiceInline2(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin4(admin.ModelAdmin):

    inlines = [ChoiceInline2]


#
# list_display, list_filter, search_fields
#

class PollAdmin5(admin.ModelAdmin):

    list_display = ['question', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question']



admin.site.register(Poll, PollAdmin5)

admin.site.register(Choice)


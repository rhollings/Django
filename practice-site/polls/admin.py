from django.contrib import admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline): 
    #With that TabularInline (instead of StackedInline), the related objects are displayed in a more compact, table-based format
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collaspe']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


'''
https://docs.djangoproject.com/en/3.2/intro/tutorial07/ 
Explanation to admin 
'''
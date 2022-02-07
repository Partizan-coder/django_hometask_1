from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Tag, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') == True:
                count += 1
        if count < 1:
            raise ValidationError('Укажите один основной раздел')
        elif count > 1:
            raise ValidationError('У статьи может быть только один основной раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormset
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['title']
    inlines = [ArticleScopeInline,]
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

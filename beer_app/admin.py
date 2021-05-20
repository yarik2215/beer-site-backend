from django.contrib import admin
from .models import Beer, UserComment


class UserCommentInline(admin.StackedInline):
    model = UserComment
    # fields = ('owner__email', 'test')
    extra = 0


@admin.register(Beer)
class PostAdmin(admin.ModelAdmin):
    list_filter = (
        'mark',
        'price',
        'updated_at',
    )
    list_display = (
        'name',
        'mark',
        'price',
        'updated_at'
    )
    search_fields = ('name',)
    date_hierarchy = 'updated_at'
    inlines = [UserCommentInline]

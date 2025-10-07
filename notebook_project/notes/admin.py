from django.contrib import admin

from .models import Category, Note, Status, User, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    ordering = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birth_date')
    search_fields = ('user__name', 'user__email')
    ordering = ('user__name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_final')
    search_fields = ('name',)
    list_filter = ('is_final',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_preview', 'author', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('text', 'author__name', 'category__title')
    date_hierarchy = 'created_at'

    @admin.display(description='Текст')
    def text_preview(self, obj):
        return obj.text[:30] + '...' if len(obj.text) > 30 else obj.text

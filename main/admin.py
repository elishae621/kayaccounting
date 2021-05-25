from django.contrib import admin
from django.contrib.auth.models import Group, User 
from .models import ContactMessage     


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'status',)
    list_filter = ('status',)
    readonly_fields = ('date',)
    fieldsets = (
        ('Details', {
            'classes': ('wide',),
            'fields': ('name', 'phone', 'email', 'status', 'date', 'content',),
        }),
    )
    search_fields = ('name', 'content',)
    ordering = ('-date',)


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = 'Kay Admin'
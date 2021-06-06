from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import ContactMessage, Instance, Mail, Subscriber


# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone', 'status',)
#     list_filter = ('status',)
#     readonly_fields = ('date',)
#     fieldsets = (
#         ('Details', {
#             'classes': ('wide',),
#             'fields': ('name', 'phone', 'email', 'status', 'date', 'content',),
#         }),
#     )
#     search_fields = ('name', 'content',)
#     ordering = ('-date',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    fieldsets = (
        (None, {
            "fields": (
                'email',
            ),
        }),
    )
        


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'address',)
    fieldsets = (
        ('Details', {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'address', 'facebook', 'instagram', 'linkedin', 'twitter',),
        }),
    )


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'date_sent',)
    list_filter = ('email',)
    fieldsets = (
        (None, {
            "fields": (
                'email', 'subject', 'content', 'date_sent',
            ),
        }),
    )
    search_filters = ('email', 'subject', 'content',)
    ordering = ('-date_sent',)



admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = 'Kay Admin'
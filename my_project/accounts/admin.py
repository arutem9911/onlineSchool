from django.contrib import admin
from accounts.models import User, UserGroup, StudyGroup


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'photo', 'role', 'birth_date', 'phone', 'city']
    list_filter = ['email', 'photo', 'role', 'birth_date']
    search_fields = ['email', 'birth_date', 'phone']
    fields = ['email', 'photo', 'role', 'birth_date', 'phone', 'city']


#
# class ImageAttachmentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order', 'image']
#     list_filter = ['order']
#     search_fields = ['order']
#     fields = ['order', 'image']
#
#
# class FileAttachmentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'order', 'document']
#     list_filter = ['order']
#     search_fields = ['order']
#     fields = ['order', 'document']
#
#
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     search_fields = ['title']
#     fields = ['title']
#
#
# admin.site.register(Order, OrderAdmin)
# admin.site.register(FileAttachment, FileAttachmentAdmin)
# admin.site.register(ImageAttachment, ImageAttachmentAdmin)
admin.site.register(User, UserAdmin)

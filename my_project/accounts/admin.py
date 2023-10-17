from django.contrib import admin
from accounts.models import User, UserGroup, StudyGroup


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'photo', 'role', 'birth_date', 'phone', 'city', 'first_name', 'last_name']
    list_filter = ['email', 'photo', 'role', 'birth_date']
    search_fields = ['email', 'birth_date', 'phone', 'first_name', 'last_name']
    fields = ['email', 'username', 'photo', 'role', 'birth_date', 'phone', 'city', 'first_name', 'last_name', 'password']


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'lesson']
    fields = ['title', 'start_date', 'end_date', 'lesson']


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'group']
    fields = ['user', 'group']


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
admin.site.register(StudyGroup, StudyGroupAdmin)
admin.site.register(UserGroup, UserGroupAdmin)

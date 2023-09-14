from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User



class UserInline(admin.StackedInline):
    model = UserMoc
    can_delete = False
    verbose_name_plural = "usermoc"

class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]

class GroupInline(admin.StackedInline):
    model = GroupMoc
    can_delete = False
    verbose_name_plural = "groupmoc"

class GroupAdmin(BaseGroupAdmin):
    inlines = [GroupInline]


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Image)
admin.site.register(Memorando)
admin.site.register(MemorandoCircular)
admin.site.register(Oficio)


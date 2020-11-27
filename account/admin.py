from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import license
# Register your models here.
@admin.register(license)
class licensesAdmin(admin.ModelAdmin):
	list_display  = ('user', 'started_at', 'expired_at', 'used', 'total', 'type', 'unlimited', 'lifetime', 'status')
	list_filter = ('expired_at', 'type', 'unlimited', 'lifetime', 'status')
	search_fields = ['user']
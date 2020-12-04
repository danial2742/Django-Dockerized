from django.contrib import admin
from account.models import License


@admin.register(License)
class LicensesAdmin(admin.ModelAdmin):
	list_display = ('user', 'started_at', 'expired_at', 'used', 'total', 'type', 'unlimited', 'lifetime', 'status')
	list_filter = ('expired_at', 'type', 'unlimited', 'lifetime', 'status')
	search_fields = ['user']
	actions = ['activate_selected_licenses', 'reset_selected_licenses']
	autocomplete_fields = ['user']

	def activate_selected_licenses(self, request, queryset):
		rows_updated = queryset.update(status=True)
		if rows_updated == 1:
			message_bit = "1 license was"
		else:
			message_bit = "%s licenses were" % rows_updated
		self.message_user(request, "%s successfully marked as deactivated." % message_bit)

	def reset_selected_licenses(self, request, queryset):
		rows_updated = queryset.update(used=0)
		if rows_updated == 1:
			message_bit = "1 license was"
		else:
			message_bit = "%s licenses were" % rows_updated
		self.message_user(request, "%s successfully reseted." % message_bit)

	def delete_queryset(self, request, queryset):
		rows_updated = queryset.update(status=False)
		if rows_updated == 1:
			message_bit = "1 license was"
		else:
			message_bit = "%s licenses were" % rows_updated
		self.message_user(request, "%s successfully marked as deactivated." % message_bit)

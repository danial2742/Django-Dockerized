from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class LicenseManager(models.Manager):
	def valid_license(self, user, license_type):
		now = timezone.now()
		count_criteria = models.Q(unlimited=True) | models.Q(used__lt=models.F('total'))
		time_criteria = models.Q(lifetime=True) | (models.Q(started_at__lt=now) & models.Q(expired_at__gt=now))
		return self.filter(user=user, type=license_type, status=True).filter(time_criteria).filter(count_criteria)

	def add_used_count(self, user, license_type, count):
		return self.filter(user=user, type=license_type, status=True).update(used=models.F('used') + count)


class License(models.Model):
	TYPE_API = 'api'
	TYPE_BLUE = 'blue'

	TYPE_CHOICES = (
		(TYPE_API, 'API'),
		(TYPE_BLUE, 'BLUE'),
	)

	user = models.ForeignKey(User, on_delete=models.PROTECT)
	started_at = models.DateTimeField()
	expired_at = models.DateTimeField()
	total = models.IntegerField(default=0)
	used = models.IntegerField(default=0)
	type = models.CharField(max_length=25, choices=TYPE_CHOICES, default='api')
	unlimited = models.BooleanField(default=False)
	lifetime = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=False)

	objects = LicenseManager()

	def delete(self):
		self.status = False
		self.save()

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['user', 'type'], name='Unique License For User')
		]

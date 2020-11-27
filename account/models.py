from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class LicenseManager(models.Manager):
	def valid_license(self, user):
		now = timezone.now()
		countCriteria = models.Q(unlimited=True) | models.Q(used__lt=models.F('total'))
		timeCriteria = models.Q(lifetime=True) | (models.Q(started_at__lt=now) & models.Q(expired_at__gt=now))
		return self.filter(user=user, type=license.TYPE_API, status=True).filter(timeCriteria).filter(countCriteria)

class license(models.Model):
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


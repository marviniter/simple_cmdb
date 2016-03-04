from django.db import models

class simple_cmdb(models.Model):
	manufacturer = models.CharField(max_length=50)
	serial_number = models.CharField(max_length=60)
	os = models.CharField(max_length=50)
	os_version = models.CharField(max_length=50)
	machine = models.CharField(max_length=50)
	hostname = models.CharField(max_length=50)
	ipaddr = models.CharField(max_length=50)
	hwaddr = models.CharField(max_length=50)
		
	def __unicode__(self):
		return self.hostname








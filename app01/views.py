from django.shortcuts import render
from django.http import HttpResponse
from app01.models import simple_cmdb

def collect(req):
	simple_cmdb.objects.create(
		manufacturer = req.POST.get('Manufacturer'),
		serial_number = req.POST.get('Serial Number'),	
		os = req.POST.get('os'),
		os_version = req.POST.get('os_version'),
		machine = req.POST.get('machine'),			
		hostname = req.POST.get('hostname'),
		ipaddr = req.POST.get('ipaddr'),
		hwaddr = req.POST.get('hwaddr'),
	)	

	return HttpResponse("ok")


	






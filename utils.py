#!/usr/bin/env python
#coding:utf-8
'''
	在client端收集数据，格式化成字典，以post方式发送到server端
	该脚本部署在client端

'''

from subprocess import Popen,PIPE
import re
import urllib
import urllib2

def get_ifconfig():
	p = Popen('ifconfig',stdout=PIPE,shell=True)
	out = p.communicate()[0]
	return out

def parse_ifconfig(out=None):
	if not None:
		out = get_ifconfig()
	#正则表达式的模板
	p =  r".*?(?P<ifname>eth\d+).*?HWaddr (?P<hwaddr>[0-9A-F:]{17}).*?inet addr:(?P<ipaddr>[0-9\.]{7,15})"
	#re.DOTALL为匹配点号
	ret = re.match(p,out,re.DOTALL)
	#以字典方式返回值,没有匹配内容会报错
	return ret.groupdict()

def get_dmidecode():
	p = Popen('dmidecode',stdout=PIPE,shell=True)
	out = p.communicate()[0]
	return out

def parse_dmidecode(out=None):
	if not None:
		out = get_dmidecode()
	p = r"System Information(.*?)\n\n"
	ret = re.findall(p,out,re.DOTALL)[0]
	ret = ret.split('\n\t')[1:]
	ret = [ i.split(': ') for i in ret]
	ret = dict(ret)
	return ret

def parse_os():
	p = Popen('uname -s',stdout=PIPE,shell=True)
	out = p.communicate()[0].strip()
	return {'os':out}

def parse_os_version():
	p = Popen('cat /etc/issue',stdout=PIPE,shell=True)
	out = p.communicate()[0]
	p = r'(\d+\.\d+)'
	out = re.findall(p,out)[0]
	return {'os_version':out}

def parse_machine_type():
	p = Popen('uname -m',stdout=PIPE,shell=True)
	out = p.communicate()[0]
	return {'machine':out.strip()}

def parse_hostname():
	p = Popen('hostname',stdout=PIPE,shell=True)
	out = p.communicate()[0]
	return {'hostname':out.strip()}

def main():
	data = {}
	data.update(parse_os())
	data.update(parse_os_version())
	data.update(parse_machine_type())
	data.update(parse_hostname())
	data.update(parse_ifconfig())
	data.update(parse_dmidecode())
	return data
	
if __name__ == '__main__':
	data = main()
	#将data字典发送到服务器端
	request = urllib2.Request('http://127.0.0.1:8000/api/collect/',urllib.urlencode(data))
	response = urllib2.urlopen(request)
	print response.read()

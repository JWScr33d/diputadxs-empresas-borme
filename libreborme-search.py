#!/usr/bin/env python
#-*- coding:utf-8 -*-

#AUTHOR: JORGE WEBSEC
import urllib2, json, time

count = 0
count_win = 0

def main():
	f = open("diputados.txt", "r")
	lines = f.readlines()
	for l in lines:
		print "--------------------------------"
		print "[!] Diputadx: " + l
		data = l.replace(" ", "+")
		data = l.replace("\n", "")
		url = "https://libreborme.net/borme/api/v1/persona/search/?q=" + data + "&page=1"
		html = urllib2.urlopen(url).read()
		j = json.loads(html)
		try:
			target = j["objects"][0]["resource_uri"]
			web = "https://libreborme.net/" + target
			html = urllib2.urlopen(web).read()
			datas = json.loads(html)
			print "Empresas:"
			for companies in datas["in_companies"]:
				print "[-]    " + str(companies)
			#print datas["in_companies"]
			print ""
			print "[INFORMACION][>]"
			print "[+]Cargos en empresas anteriores:"
			print datas["cargos_historial"]
			print "[+]Cargos en empresas actualmente:"
			print datas["cargos_actuales"]
			print ""

			if datas["cargos_actuales"]:
				count_win += 1

			count += 1
		except:
			print "No hay datos en el BORME"
		time.sleep(10)
	print "***************************************************"
	print "Diputadxs empresarixs: " + str(count)
	print "Diputadxs actualmente empresarixs: " + str(count_win)
	print "***************************************************"

main()

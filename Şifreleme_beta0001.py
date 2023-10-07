dongu_anahtarı = True

while dongu_anahtarı:
	sec_girdi = input("Şifrelemek için 1 şifre çözmek için 2 yazın\n")

	if sec_girdi == "1":
		
		kod = "000000000000 0aaaaaaaakkkkksssşhhhdşpğisffyyyxxyıççşşiiüğtcyas"
		kod2 = "yugtrdHJnvCHtumTRgsY Chdya00056"
		kod3 = "aatyibgyhcretau xnYIngThjOjYigdddddditYgygısrd7872392163"
		kod4 = "a676 llllaamany a28434ed H 5"
		sifreli_metin_yaz = input("Metin yaz: \n")

		sifrelendi2 =sifreli_metin_yaz.replace("e","210 342 1829")

		sifrelendi = kod3 + sifrelendi2[0:5] + kod +sifrelendi2[6:10] + kod2 + sifrelendi2 + kod4

		print(sifrelendi)

	elif sec_girdi == "2":
		coz_girdi = input("Şifrelenen metini yazın:\n")

		cozuldu = coz_girdi.replace("210 342 1829","e")
		print(f"{cozuldu[158:-28]}")

	else:
		print("hatalı giriş")

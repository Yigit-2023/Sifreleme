dongu_anahtarı = True


print("Şifreleme pro\nSürüm:   1.0\n")


while dongu_anahtarı:
	sec_girdi = input("Şifrelemek için 1 şifre çözmek için 2 yazın\n")

	if sec_girdi == "1":
		
		kod = "000000000000 0aaaaaaaakkkkksssşhhhdşpğisffyyyxxyıççşşiiüğtcyas"
		kod2 = "yugtrdHJn vCHtum TRgsY Chdya00056"
		kod3 = "aatyibgyhcretau xnYIngSelam ThjO jYigdddddditYgygısrd7872392163"
		kod4 = "a676 llllaamany a28434ed H 5"
		kod5 = "Ali Baass işte tamam asss fhhy ak rj asd tr alın "
		kod6 = "Bu merhaba slll slm sdfd asddsasdsdsa "
		kod7 = "sak sdds gffd saasdsa"
		kod8 = "1111111111111111pro0000000000 Yigit aaa cccxxx al sa da dsamiyee aa oldu kod 01pro"
		sifreli_metin_yaz = input("Metin yaz: \n")

		sifrelendi2 =sifreli_metin_yaz.replace("e","210 342 1829")

		sifrelendi = kod + kod8 + sifreli_metin_yaz[0:4] + kod5 + kod6 + sifreli_metin_yaz[0:6] + sifreli_metin_yaz[0:3] + kod8 + sifreli_metin_yaz[0:5] + kod7 + kod2 + sifreli_metin_yaz + kod3 +kod4


		print(f"{sifrelendi}")

	elif sec_girdi == "2":
		coz_girdi = input("Şifrelenen metini yazın:\n")

		cozuldu = coz_girdi.replace("210 342 1829","e")

		print(f"{cozuldu[385:-91]}")


	else:
		print("hatalı giriş")

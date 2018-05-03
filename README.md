# halozatok
ELTE IK számítógépes hálózatok tárgy -python

http://lakis.web.elte.hu/szhEA/Lecture_1.pdf   
http://lakis.web.elte.hu/szh201718II/gyak1/gyakorlat1.pdf   


http://vopraai.web.elte.hu/tananyag/halok1718t/Beadandok/1.beadando_bit_byte_beszuras.txt  --- > bemutatni -- bit byte beszúrás protokollja javítani.
http://vopraai.web.elte.hu/tananyag/halok1718t/Beadandok/2.beadando_CDMA.txt  -- > 04.17
 harmadik beadandó:
 BEADÁSI HATÁRIDŐ:
05.08

A Mikulás segítői a Manók szeretnének ajándékokat gyártani a jó gyerekeknek. Ehhez a elengedhetetlen, hogy az alkatrész-raktárból össze tudják szedni a darabokat.
A lehetséges elemek: kocka, kerék, hangszóró, elem, kijelző.

2-esért:
A raktárfelelős egy kezdő készlettel inicializálódik. Végtelen ciklusban fut: fogad egy kapcsolatot, megválaszolja a kérést és bontja a kapcsolatot.
A manó kliens elküldi a szükséges elemek listáját Pl.: {"kocka":1, "kerék": 2} a Raktárfelelősnek (szerver) TCP-n.
A szerver minden kérésére a saját adataiból megválaszolja, hogy rendelkezik-e mindennel amit a manó kért.
Ha igen akkor annyival csökkenti a készleteit, és azt válaszolja, hogy igen.
Ha bármi nem teljesíthető akkor nemmel válaszol, és nem csökken egyik alkatrész készlete sem.

	+--------+          +---------------+
	|        |    TCP   |               |
	|  Manó  +----------> Raktárfelelős |
	|        |          |               |
	+--------+          +---------------+


3-asért:
Több kliens csatlakozhat egyszerre, akit ki kell szolgálni. 
	+--------+
	|        |
	|  Manó  +-----+
	|        |     |                       
	+--------+     |                       
	               |                       
	+--------+     |    +---------------+
	|        |  TCP|    |               |
	|  Manó  +----------> Raktárfelelős |
	|        |     |    |               |
	+--------+     |    +---------------+
	               |                       
	+--------+     |                       
	|        |     |                       
	|  Manó  +-----+
	|        |
	+--------+


4-esért:
A rakárfelelős proxy-ként működik. A kapott kéréseket nem a saját adataiból válaszolja meg, hanem elküldi a kérést egy raktárnak UDP-n, és az adja meg a választ.
	+--------+
	|        |
	|  Manó  +-----+
	|        |     |                       
	+--------+     |                       
                   |                       
	+--------+     |    +---------------+        +----------+
	|        |  TCP|    |               |  UDP   |          |
	|  Manó  +----------> Raktárfelelős +-------->  Raktár  |
	|        |     |    |               |        |          |
	+--------+     |    +---------------+        +----------+
				   |                       
	+--------+     |                       
	|        |     |                       
	|  Manó  +-----+
	|        |
	+--------+
	
5-ösért:
Általad kitalált módon tervezz kontrollösszeget (checksum) a rendszerbe, amit a raktárfelelős számol a küldendő üzenetekhez, mikor a raktárral kommunikál. A Raktár ellenőrzi, hogy a kérés nem-e sérült-e meg, a checksum alapján. Ha sérült akkor azt válaszolja, hogy hiba, egyébként minden megy ugyanúgy, mint eddig. (A raktárnak visszaküldéskor nem kell checksumot adni a válaszához.)

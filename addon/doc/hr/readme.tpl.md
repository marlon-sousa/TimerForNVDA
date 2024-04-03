# Brojač za NVDA ${addon_version}
Donosi funkcije mjerača vremena i štoperice izravno u NVDA

## preuzimanje

Preuzmite [${addon_summary} ${addon_version} ] (${addon_url}/releases/download/${addon_version}/${addon_name}-${addon_version}.nvda-addon)

## Brojači i štoperice

Brojač broji određeno vrijeme do 0. Kada dosegne 0, završava i emitira se alarm.

Štoperica počinje brojati od 0 i nastavlja raditi dok ne dobije uputu za zaustavljanje. Kada se to dogodi, prikazuje proteklo vrijeme.

## Značajke

### Dijaloški okvir jednostavnih postavki

Brojač ili štoperica mogu se konfigurirati iz jednostavnog dijaloškog okvira postavki.

Iz istog dijaloškog okvira mogu se konfigurirati i različita izvješća o praćenju napretka.

#### Kako radi

Ili upotrijebite podizbornik "Brojač za NVDA postavke" ili pritisnite NVDA + Shift + T za otvaranje dijaloškog okvira postavki dodatka.
Podizbornik se nalazi u NVDA izborniku "Alati".

* Ako radi brojač ili štoperica, možete:
    * Pratiti napredak čitanjem statusne trake dijaloga postavki.
    * Pauzirati, nastaviti ili zaustaviti brojač ili štopericu.
* Ako su brojač ili štoperica zaustavljeni, možete:
    * Konfigurirati način rada (Brojač ili štoperica)
    * Konfigurirati vremensku jedinicu koja se koristi za početnu vrijednost vremena za brojač i također za izvješćivanje (sekundi, minuta ili sati)
    * Pokrenuti mjerač vremena ili štopericu.
* U bilo koje vrijeme možete:
    * Odabrati hoće li se napredak najavljivati govorom, zvučnim signalom, obojem ili ničim.

### Pokretanje NVDA naredbama

U bilo kojem trenutku je moguće pokrenuti, zaustaviti, pauzirati, nastaviti i dobiti izvješća o napretku iz brojača ili štoperice bez potrebe za korištenjem dijaloškog okvira postavki.

#### Kako radi

* Pritisnite NVDA + Control + Shift + S za pokretanje ili zaustavljanje brojača ili štoperice.
    * Ako ne radi nijedan brojač ili štoperica, jedan od njih će se pokrenuti, prema trenutnom načinu rada.
    * Ako jedan od njih radi, zaustavit će se. Proteklo vrijeme se najavljuje u slučaju da je štoperica radila
    * U slučaju da se brojač pokreće i nije konfigurirano prethodno početno vrijeme, emitira se upozorenje.
* pritisnite NVDA + Control + Shift + P za pauziranje ili nastavak brojača ili štoperice.
* Pritisnite NVDA + Control + Shift + R da provjerite napredak brojača ili štoperice. Ovo je posebno korisno ako su svi izvjestitelji o napretku isključeni i želite provjeriti napredak na zahtjev.

### unos vremena

U dijaloškom okviru postavki, početno vrijeme za brojač se unosi u HH: MM: SS formatu, gdje HH označava sate, MM minute i SS sekunde.

Nije potrebno upisivati ​​puni format, sustav će ga zaključiti:

* Ako se unese jednostavan broj, koristit će se odabrana vremenska jedinica.
* Ako su navedene podjedinice, one će se uzeti u obzir. Na primjer, 01:05 postaje jedna minuta i pet sekundi, ako je odabrana vremenska jedinica "minute".
Ako je odabrana vremenska jedinica "sati", 01:05 postaje jedan sat, pet minuta i nula sekundi.
* Podjedinice iznad "sekunde" su nevažeće. Ako je vremenska jedinica "minute", vrijednost 01:05:02 neće biti prihvaćena.

### Izvođenje brojača i štoperice

Istovremeno se može pokrenuti samo jedan brojač ili štoperica.
Napredak se može pratiti korištenjem nijednog, jednog ili više reportera, čitanjem statusne trake dijaloškog brojača ili izdavanjem naredbe statusa izvješća, NVDA + Control + Shift + R.
Na ovaj način je savršeno moguće pokrenuti sustav s isključenim svim izvješćima i pratiti napredak čitanjem statusne trake kada se dijaloški okvir otvori.

Naredbe za zaustavljanje, pokretanje, pauziranje, nastavak ili dobivanje izvješća o napretku na zahtjev mogu se koristiti čak i kada je dijaloški okvir postavki aktivan.

Može biti pokrenuta samo jedna instanca dijaloga postavki. Ako je dijaloški okvir postavki zatvoren, izvršavanja brojača ili štoperice u tijeku će nastaviti raditi.

Ako se dijaloški okvir postavki otvori dok radi brojač ili štoperica, on će u skladu s tim prikazati ažurirane informacije.

### Vremenska preciznost

Ovaj dodatak ne može računati vrijeme na iznimno precizan način.

To se događa zato što Python, jezik na kojem je NVDA napisan, ne može izvršiti više od jedne instrukcije u isto vrijeme, čak i ako postoji više od jednog procesora ili procesorske jezgre dostupne za korištenje.

Stoga, svaki put kada NVDA nešto govori, izračunava ili obrađuje, odbrojavanje vremena imat će malo kašnjenje.

Preciznost bi, međutim, trebala biti dobra u velikoj većini slučajeva, osim ako je milisekundna preciznost neophodna ili će u suprotnom na neki proces ozbiljno utjecati bilo kakvo kašnjenje.

Za bolju preciznost, izvješća bi trebala biti isključena i status bi se trebao zatražiti na zahtjev ili izdavanjem NVDA + Control + Shift + R ili čitanjem statusne trake dijaloškog okvira brojača.

### Reporteri

#### Zvučni reporter

Kada je aktiviran, ovaj reporter pušta zvučni signal svaki put kada brojač vremena ili štoperice dosegne zaokruženu vrijednost, u skladu s vremenskom jedinicom konfiguriranom u dijaloškom okviru postavki.

Ako ste, na primjer, konfigurirali brojač za 02:30 minute, zvučni signal će se čuti kada je odbrojavanje u 02:00 minuti, a drugi kada je u 01:00 minuti.

Točno brojanje možete dobiti čitanjem statusne trake dijaloškog okvira postavki ili izdavanjem naredbe statusa izvješća, NVDA + Control + Shift + R.

#### Govorni reporter

Kada je aktiviran, ovaj reporter izjavljuje trenutno brojanje vremena svaki put kada dosegne zaokruženu vrijednost, u skladu s vremenskom jedinicom konfiguriranom u dijaloškom okviru postavki.

Ako ste, na primjer, konfigurirali mjerač vremena za 02:30 minute, "2" će se izgovoriti kada je brojanje u 02:00 minuti, a "1" će se izgovoriti kada je u 01:00 minuti.

Točno brojanje možete dobiti čitanjem statusne trake dijaloškog okvira postavki ili izdavanjem naredbe statusa izvješća, ctrl + shift + NVDA + r.

### Izvješće o završetku brojača

Kada vrijeme koje se broji za timer dosegne 0, završilo je. To se signalizira, neovisno o aktivnom dijalogu postavki, diskretnim zvukom budilice. Ovaj zvuk ne ovisi o tome da su izvjestitelji o napretku aktivni.

### Izvješće o završetku štoperice

Kada je štoperica zaustavljena, izgovara se njeno proteklo vrijeme,neovisno o aktivnom dijalogu postavki.

Proteklo vrijeme posljednjeg izvršavanja štoperice može se provjeriti pregledom statusne trake dijaloga postavki ili pritiskom na NVDA + Control + Shift + R. Ove informacije se resetiraju kada se pokrene nova štoperica ili brojač.

### Izmijenite ulazne geste

Možete promijeniti zadane ulazne geste za ovaj dodatak tako da pristupite odjeljku "Brojač za NVDA" u NVDA izborniku / Postavke / Ulazne geste.

Zapamtite da, ako promijenite ulazne geste, morat ćete odabrati opcije koje ne koriste druge NVDA ili vanjske skripte dodataka kako biste izbjegli sukobe.

# Doprinos i prevođenje

Ako želite doprinijeti ili prevesti ovaj dodatak, pristupite [repozitoriju projekta] (${addon_url}) i pronađite upute na contributing.md u imeniku na vašem jeziku ili na engleskom jeziku.

## Suradnici

Posebno zahvaljujemo

* Marlon Brandão de Sousa - brazilski portugalski prijevod
* Ângelo Miguel Abrantes - portugalski prijevod
* Tarik Hadžirović - hrvatski prijevod
* Rémy Ruiz - francuski prijevod
* Rémy Ruiz - španjolski prijevod
* Umut KORKMAZ - turski prijevod
* Danil Kostenkov - ruski prijevod
* Heorhii - ukrajinski prijevod
* Brian Missao da Vera - NVDA 2022.1 kompatibilnost
* Edilberto Fonseca - NVDA 2024.1 kompatibilnost

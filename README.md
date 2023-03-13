<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Docs/Chema_Alonso%20(1).jpg" alt="Hacker roadmap" /><br>
</p>

Repositorio hau Ciber ikasturteko T3 Zabala Gailetena da

## Status

**Egiten**.

----

# Table of Contents

- [Ekoizpen gertakariak](#ekoizpen-gertakariak)
    - [Django Web](#django-web)
    - [Android App](#android-app)
- [Hacking](#hacking)
- [Docs](#Docs)
- [License](#license)


# Ekoizpen gertakariak

## Django Web
**Capturas** escribir tocho con capturas: [Wikipedia](https://en.wikipedia.org/wiki/Operations_security)

## Android App
**capturas** mas tocho

([Table of Contents](#table-of-contents))

# Hacking

### 0) Introdukzioa

Hasteko windows7 makina biktima esplotatzeko **CVE-2014-6332** vulnerabilitatea erabili dugu. Honek internet explorerren konponente baten failo batetaz baliatzen da. *Object Linking and Embedding* (OLE) da konponentea. Konponente hau windows aplikazioen artean datuak eta funtzionamedua konpartitzeko ahalbideratzen duen teknologia bat da.

Baina *"CreateObject"* funtzioak ez zituen OLE fitxategiak pasatzen zituen datuak balidatzen eta honek RCE bat gertatzeko aukera ematen zuen. Atake askok HTMLan javascript erabiliz OLE fitxategi maliziosoak gordetzen zituzten eta IE erabilita honek irakurri eta kodigoa automatikoki exekutatzen zen

### 1) Prestaketa
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/kaliSetup(1).PNG?raw=true">
</p>

Hasteko malwarea duen web horri bat prestatu (index izenarekin) eta pythonen **http.server** modulua erabilita ***``80``*** portuan zerbitzari bat sortu dugu. Web horrian reverse shell portaera bat sartu diogu kalira begira; beraz kalian ``nc -lvp 6969`` eginda *[netcat](https://eternallybored.org/misc/netcat/)* konexioak entzuten geldituko da eta horrela dena prest izango genuke.

### 2) Biktimaren POV-a 
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/internetExplorer(2).PNG">
</p>

*Biktimak ez daki ezer; bakarrik hentai ikustea nahi du.*

### 3) Biktimarekin konexioa
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/pwned(3).PNG">
</p>
Biktima web horrian sartu eta orain nire ordenagailu erasotzailearekin konektatu da.
****fijatzen bazarete serbitzari propio batean dago stage2.html rutan (payload a duen horria)****

### 4) Post esplotazio kutrea
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/hacked%20txt(4).PNG">
</p>
Orain biktimaren kontrol osoa dugu eta adibidez fitxategi bat sortu eta notepadekin zabaldu dezakegu honek biktimaren ordenagailuan notepada zabalduko du eta biktima oso kagatuta egongo da.

([Table of Contents](#table-of-contents))

# License

This repository is under MIT license.

([Table of Contents](#table-of-contents))

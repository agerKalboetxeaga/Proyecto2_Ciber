<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Docs/Chema_Alonso%20(1).jpg" alt="Hacker roadmap" /><br>
</p>

Repositorio hau Ciber ikasturteko T3 Zabala Gailetena da

## Status

**Egiten**.

----

# Table of Contents

- [Ekoizpen gertakariak](#)
    - [Django Web](https://github.com/agerKalboetxeaga/Proyecto2_Ciber/tree/main/django_vulnerable/Django_Web)
    - [Android App](https://github.com/agerKalboetxeaga/Proyecto2_Ciber/tree/main/Android_App/OWASP%20MASTG-Hacking-Playground%20master%20Android-MSTG-Android-Java-App)
- [Phishing](https://github.com/agerKalboetxeaga/Proyecto2_Ciber/tree/main/Phishing)
- [Hacking](#hacking)
- [Docs](https://github.com/agerKalboetxeaga/Proyecto2_Ciber/tree/main/Docs)
- [License](#license)

# Hacking

## Windows 7 Professional

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

## Windows Server 2008

### 0) Introdukzioa

Orain Windows Server 2008 baten momentua zen eta aurrerago analisitik datuengatik **CVE-2019-0708** vulnerabilitatea esplotatu dugu. Vulnerabilitate honek Remote desktopen protoko zerbitzuan (RPD) dagoen fallo batetaz baliatzen da:
    Atakante batek paketen bidez *buffer overflow* bat eragin dezake eta ostean sisteman kodigoa exekutatu. Vulnerabilitate hau hain famatua izan zen eta BlueKeep modura ere ezagutzen da.
    
### 1) Nmap analisia
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/1.-%20nmap%20result.PNG">
</p>

Irudian ikusten den bezala 3389 portua zabalik zuela ikusten da; eta makinan ikusita (konprobatzeko):
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/2.Escritorio%20remoto.PNG">
</p>

Efektibamente Remote desktopa habilitatua zegoen eta konfigurazioan begiratuta:
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/3.-%20Escritorio%20remoto.PNG">
</p>

Opzio ez seguruena markatuta zegoen; Bingo!
Interneten aztertu ondoren fallo bat zuela ikusi genuen; lehenago esandako CVE a. 

### 2) Explotazioa
Exploitak begiratzen ibili ginen eta erraztasunagatik metasploit framework a erabili genuen ****exploit/windows/rdp/cve_2019_0708_bluekeep_rce****
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/4.-%20exploit%20configuration.PNG">
</p>

Exploita konfiguratu genuen eta ostean exekutatu:
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/5.-%20Exploited.PNG">
</p>

Ostean dena ondo urten zela bermatzeko proba batzuk egin genituen:
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/6.-%20Bacilating%20part%201.PNG">
</p>
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/winserver/6.-%20Bacilating%20part%202.PNG">
</p>

## Ubuntu server
Azkenik ubuntu server bat genuen (ez dugu argazkirik). 

Zerbitzaria analizatuta (nmapekin) SMB zerbitzua gaituta duela ikusi dugu hain zuzen 4.1.6 bertsioa eta ikusi ostean SMBCry (CVE-2020-0796) exploitarekin
topatu ginen. Baina arazo batzuk izan genituen exploita exekutatzeko: Python bertsioak. exploitak python 2an idatziak zeuden eta Python2 zuen Virtual enviroment bat sortutzerakoan erroreak ematen zituen: modulo bat ya ez zen existitzen beraz entornoa geizki sortzen zen :( 

Beraz beste ideia bat izan genuen. Makinak smb zerbitzuaren gain Mysql eta Http zerbitzuak ere martxan zituen. Web horrian ea PHPMyAdmin horria bistan zuela konprobatu genuen eta Bingo, hor zegoen login horria. Default kredentzialak probatzea okurritu zitzaigun (root:) eta barrura sartu ginen. Vamosss. Ostean sql bidez php orri berri bat sortu genuen non sistema komandoak exekutatzen baliatzen zuen. Nire zerbitzaritik reverse shell bat deskargatu nuen eta makinan exekutatu, eta horrela makinaren kontrola lortu genuen.

([Table of Contents](#table-of-contents))

# License

This repository is under MIT license.

([Table of Contents](#table-of-contents))

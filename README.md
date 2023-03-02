<p align="center">
    <img src="https://i.imgur.com/VeEYEkT.png" alt="Hacker roadmap" /><br>
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


## Want to become a penetration tester?

Knowing about risks on the internet and how they can be prevented is very useful, especially as a developer. Web hacking and penetration testing is the v2.0 of self-defense! But is knowing about tools and how to use them really all you need to become a pen tester? Surely not. A real penetration tester must be able to proceed rigorously and detect the weaknesses of an application. They must be able to identify the technology behind and test every single door that might be open to hackers.

This repository aims first to establish a reflection method on penetration testing and explain how to proceed to secure an application. And secondly, to regroup all kind of tools or resources pen testers need. **Be sure to know basics of programming languages and internet security before learning pen testing.**

Also, this is important to inform yourself about the law and what you are allowed to do or not. According to your country, the computer laws are not the same. First, check laws about privacy and surveillance: [Nine eyes countries](https://en.wikipedia.org/wiki/Five_Eyes#Other_international_cooperatives), [Five eyes](https://en.wikipedia.org/wiki/Five_Eyes) and Fourteen Eyes. Always check if what you're doing is legal. Even when it's not offensive, information gathering can also be illegal!

# Ekoizpen gertakariak

## Django Web
**Capturas** escribir tocho con capturas: [Wikipedia](https://en.wikipedia.org/wiki/Operations_security)

## Android App
**capturas** mas tocho

([Table of Contents](#table-of-contents))

# Hacking

### 0) Introdukzioa

Hasteko windows7 makina biktima esplotatzeko **CVE-2014-6332** vulnerabilitatea erabili dugu. Honek internet explorerren konponente baten failo batetaz baliatzen da. Object Linking and Embedding (OLE) da konponentea. Konponente hau windows aplikazioen artean datuak eta funtzionamedua konpartitzeko ahalbideratzen duen teknologia bat da.

Baina "CreateObject" funtzioak ez zituen OLE fitxategiak pasatzen zituen datuak balidatzen eta honek RCE bat gertatzeko aukera ematen zuen. Atake askok HTMLan javascript erabiliz OLE fitxategi maliziosoak gordetzen zituzten eta IE erabilita honek irakurri eta kodigoa automatikoki exekutatzen zen

### 1) Prestaketa
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/kaliSetup(1).PNG?raw=true">
</p>

Hasteko malwarea duen web horri bat prestatu (index izenarekin) eta pythonen **http.server** modulua erabilita 80 portuan zerbitzari bat sortu dugu. Web horrian reverse shell portaera bat sartu diogu kalira begira; beraz kalian **nc -lvp 6969** eginda netcat konexioak entzuten geldituko da eta horrela dena prest izango genuke.

### 2) Biktimaren POV-a 
<p align="center">
    <img src="https://github.com/agerKalboetxeaga/Proyecto2_Ciber/blob/main/Hacking/Capturas/internetExplorer(2).PNG">
</p>

Biktimak ez daki ezer; bakarrik hentai ikustea nahi du 


### Scripting

- Bash
- Powershell

### Software & mobile apps

- Java
- Swift
- C / C++ / C#

### General purpose

- Python
- Ruby
- Perl
- PHP
- Go

([Table of Contents](#table-of-contents))

# Content Management Systems

- Wordpress
- Joomla
- Drupal
- SPIP

These are the most used Content Management Systems (CMS). See a complete list [here](https://en.wikipedia.org/wiki/List_of_content_management_systems).

([Table of Contents](#table-of-contents))

# Basic steps of pen testing

<p align="center">
    <img src="https://www.tutorialspoint.com/penetration_testing/images/penetration_testing_method.jpg">
</p>

*Source: [tutorialspoint](https://www.tutorialspoint.com/penetration_testing/index.htm)*

[Read more about pen testing methodology](https://www.tutorialspoint.com/penetration_testing/penetration_testing_method.htm)

([Table of Contents](#table-of-contents))

# Tools by category

A more complete list of tools can be found on [Kali Linux official website](https://tools.kali.org/tools-listing).

#### :male_detective: Information Gathering

Information Gathering tools allows you to collect host metadata about services and users. Check informations about a domain, IP address, phone number or an email address.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [theHarvester](https://github.com/laramies/theHarvester)      | **Python** | `Linux/Windows/macOS` | E-mails, subdomains and names Harvester. |
| [CTFR](https://github.com/UnaPibaGeek/ctfr)      | **Python** | `Linux/Windows/macOS` | Abusing Certificate Transparency logs for getting HTTPS websites subdomains. |
| [Sn1per](https://github.com/1N3/Sn1per)      | **bash** | `Linux/macOS` | Automated Pentest Recon Scanner. |
| [RED Hawk](https://github.com/Tuhinshubhra/RED_HAWK)      | **PHP** | `Linux/Windows/macOS` | All in one tool for Information Gathering, Vulnerability Scanning and Crawling. A must have tool for all penetration testers. |
| [Infoga](https://github.com/m4ll0k/Infoga)      | **Python** | `Linux/Windows/macOS` | Email Information Gathering. |
| [KnockMail](https://github.com/4w4k3/KnockMail)      | **Python** | `Linux/Windows/macOS` | Check if email address exists. |
| [a2sv](https://github.com/hahwul/a2sv)      | **Python** | `Linux/Windows/macOS` | Auto Scanning to SSL Vulnerability. |
| [Wfuzz](https://github.com/xmendez/wfuzz)      | **Python** | `Linux/Windows/macOS` | Web application fuzzer. |
| [Nmap](https://github.com/nmap/nmap)      | **C/C++** | `Linux/Windows/macOS` | A very common tool. Network host, vuln and port detector. |
| [PhoneInfoga](https://github.com/sundowndev/PhoneInfoga)      | **Go** | `Linux/macOS` | An OSINT framework for phone numbers. |

#### :lock: Password Attacks

Crack passwords and create wordlists.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [John the Ripper](https://github.com/magnumripper/JohnTheRipper)      | **C** | `Linux/Windows/macOS` | John the Ripper is a fast password cracker. |
| [hashcat](https://github.com/hashcat/hashcat)      | **C** | `Linux/Windows/macOS` | World's fastest and most advanced password recovery utility. |
| [Hydra](https://github.com/vanhauser-thc/thc-hydra)      | **C** | `Linux/Windows/macOS` | Parallelized login cracker which supports numerous protocols to attack. |
| [ophcrack](https://gitlab.com/objectifsecurite/ophcrack)      | **C++** | `Linux/Windows/macOS` | Windows password cracker based on rainbow tables. |
| [Ncrack](https://github.com/nmap/ncrack)      | **C** | `Linux/Windows/macOS` | High-speed network authentication cracking tool. |
| [WGen](https://github.com/agusmakmun/Python-Wordlist-Generator)      | **Python** | `Linux/Windows/macOS` | Create awesome wordlists with Python. |
| [SSH Auditor](https://github.com/ncsa/ssh-auditor)      | **Go** | `Linux/macOS` | The best way to scan for weak ssh passwords on your network. |

###### :memo: Wordlists

| Tool        | Description    |
| ----------- |----------------|
| [Probable Wordlist](https://github.com/berzerk0/Probable-Wordlists)      | Wordlists sorted by probability originally created for password generation and testing. |

#### :globe_with_meridians: Wireless Testing

Used for intrusion detection and wifi attacks.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [Aircrack](https://github.com/aircrack-ng/aircrack-ng)      | **C** | `Linux/Windows/macOS` | WiFi security auditing tools suite. |
| [bettercap](https://github.com/bettercap/bettercap)      | **Go** | `Linux/Windows/macOS/Android` | bettercap is the Swiss army knife for network attacks and monitoring. |
| [WiFi Pumpkin](https://github.com/P0cL4bs/WiFi-Pumpkin)      | **Python** | `Linux/Windows/macOS/Android` | Framework for Rogue Wi-Fi Access Point Attack. |
| [Airgeddon](https://github.com/v1s1t0r1sh3r3/airgeddon)      | **Shell** | `Linux/Windows/macOS` | This is a multi-use bash script for Linux systems to audit wireless networks. |
| [Airbash](https://github.com/tehw0lf/airbash)      | **C** | `Linux/Windows/macOS` | A POSIX-compliant, fully automated WPA PSK handshake capture script aimed at penetration testing. |

#### :wrench: Exploitation Tools

Acesss systems and data with service-oriented exploits.

| Tool                                                    | Language   | Support               | Description                                                  |
| ------------------------------------------------------- | ---------- | --------------------- | ------------------------------------------------------------ |
| [SQLmap](https://github.com/sqlmapproject/sqlmap)       | **Python** | `Linux/Windows/macOS` | Automatic SQL injection and database takeover tool.          |
| [XSStrike](https://github.com/UltimateHackers/XSStrike) | **Python** | `Linux/Windows/macOS` | Advanced XSS detection and exploitation suite.               |
| [Commix](https://github.com/commixproject/commix)       | **Python** | `Linux/Windows/macOS` | Automated All-in-One OS command injection and exploitation tool.￼ |
| [Nuclei](https://github.com/projectdiscovery/nuclei)    | **Go**     | `Linux/Windows/macOS` | Fast and customisable vulnerability scanner based on simple YAML based DSL. |

#### :busts_in_silhouette: Sniffing & Spoofing

Listen to network traffic or fake a network entity.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [Wireshark](https://www.wireshark.org)      | **C/C++** | `Linux/Windows/macOS` | Wireshark is a network protocol analyzer. |
| [WiFi Pumpkin](https://github.com/P0cL4bs/WiFi-Pumpkin)      | **Python** | `Linux/Windows/macOS/Android` | Framework for Rogue Wi-Fi Access Point Attack. |
| [Zarp](https://github.com/hatRiot/zarp)      | **Python** | `Linux/Windows/macOS` | A free network attack framework. |

#### :rocket: Web Hacking

Exploit popular CMSs that are hosted online.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [WPScan](https://github.com/wpscanteam/wpscan)      | **Ruby** | `Linux/Windows/macOS` | WPScan is a black box WordPress vulnerability scanner. |
| [Droopescan](https://github.com/droope/droopescan)      | **Python** | `Linux/Windows/macOS` | A plugin-based scanner to identify issues with several CMSs, mainly Drupal & Silverstripe. |
| [Joomscan](https://github.com/rezasp/joomscan)      | **Perl** | `Linux/Windows/macOS` | Joomla Vulnerability Scanner. |
| [Drupwn](https://github.com/immunIT/drupwn)      | **Python** | `Linux/Windows/macOS` | Drupal Security Scanner to perform enumerations on Drupal-based web applications. |
| [CMSeek](https://github.com/Tuhinshubhra/CMSeek)      | **Python** | `Linux/Windows/macOS` | CMS Detection and Exploitation suite - Scan WordPress, Joomla, Drupal and 130 other CMSs. |

#### :tada: Post Exploitation

Exploits for after you have already gained access.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [TheFatRat](https://github.com/Screetsec/TheFatRat)      | **C** | `Linux/Windows/macOS` | Easy tool to generate backdoor and easy tool to post exploitation attack like browser attack, dll. |

#### :package: Frameworks

Frameworks are packs of pen testing tools with custom shell navigation and documentation.

| Tool        | Language           | Support  | Description    |
| ----------- |-------------------------|----------|----------------|
| [Operative Framework](https://github.com/graniet/operative-framework)      | **Python** | `Linux/Windows/macOS` | Framework based on fingerprint action, this tool is used to get information on a website or a enterprise target with multiple modules. |
| [Metasploit](https://github.com/rapid7/metasploit-framework)      | **Ruby** | `Linux/Windows/macOS` | A penetration testing framework for ethical hackers. |
| [cSploit](https://github.com/cSploit/android)      | **Java** | `Android` | The most complete and advanced IT security professional toolkit on Android. |
| [radare2](https://github.com/radare/radare2)      | **C** | `Linux/Windows/macOS/Android` | Unix-like reverse engineering framework and commandline tools. |
| [Wifiphisher](https://github.com/wifiphisher/wifiphisher)      | **Python** | `Linux` | The Rogue Access Point Framework. |
| [Beef](https://github.com/beefproject/beef)      | **Javascript** | `Linux/Windows/macOS` | The Browser Exploitation Framework. It is a penetration testing tool that focuses on the web browser. |
| [Mobile Security Framework (MobSF)](https://github.com/MobSF/Mobile-Security-Framework-MobSF)      | **Python** | `Linux/Windows/macOS` | Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework capable of performing static and dynamic analysis. |
| [Burp Suite](https://portswigger.net/burp)      | **Java** | `Linux/Windows/macOS` | Burp Suite is a leading range of cybersecurity tools, brought to you by PortSwigger. **This tool is not free and open source** |

([Table of Contents](#table-of-contents))

# Additional resources

- [Devbreak on Twitter](https://twitter.com/DevbreakFR)
- [The Life of a Security Researcher](https://www.alienvault.com/blogs/security-essentials/the-life-of-a-security-researcher)
- [Find an awesome hacking spots in your country](https://github.com/diasdavid/awesome-hacking-spots)
- [Awesome-Hacking Lists](https://github.com/Hack-with-Github/Awesome-Hacking/blob/master/README.md)
- [Crack Station](http://crackstation.net/)
- [Exploit Database](http://www.exploit-db.com/)
- [Hackavision](http://www.hackavision.com/)
- [Hackmethod](https://www.hackmethod.com/)
- [Packet Storm Security](http://packetstormsecurity.org/)
- [SecLists](http://seclists.org/)
- [SecTools](http://sectools.org/)
- [Smash the Stack](http://smashthestack.org/)
- [Don't use VPN services](https://gist.github.com/joepie91/5a9909939e6ce7d09e29)
- [How to Avoid Becoming a Script Kiddie](https://www.wikihow.com/Avoid-Becoming-a-Script-Kiddie)
- [2017 Top 10 Application Security Risks](https://www.owasp.org/index.php/Top_10-2017_Top_10)
- [Starting in cybersecurity ?](https://blog.0day.rocks/starting-in-cybersecurity-5b02d827fb54)

## Books / Manuals

**Warning :** I haven't read them all so do not consider I am recommending as I liked them. They just seem to provide useful resources.

- [Penetration Testing: A Hands-On Introduction to Hacking](https://www.amazon.com/Penetration-Testing-Hands-Introduction-Hacking/dp/1593275641) (2014)
- [Kali Linux Revealed](https://www.amazon.com/Kali-Linux-Revealed-Penetration-Distribution/dp/0997615605) - [PDF](https://kali.training/downloads/Kali-Linux-Revealed-1st-edition.pdf) (2017)
- [Blue Team Field Manual (BTFM)](https://www.amazon.com/Blue-Team-Field-Manual-BTFM/dp/154101636X) (2017)
- [Cybersecurity - Attack and Defense Strategies](https://www.amazon.com/Cybersecurity-Defense-Strategies-Infrastructure-security/dp/1788475291) (2018)
- [NMAP Network Scanning : Official Discovery](https://www.amazon.com/Nmap-Network-Scanning-Official-Discovery/dp/0979958717) (2009)
- [Social Engineering : The Art of Human Hacking](https://www.amazon.com/Social-Engineering-Art-Human-Hacking/dp/0470639539) (2010)
- [Incognito Toolkit: Tools, Apps, and Creative Methods for Remaining Anonymous](https://www.amazon.com/Incognito-Toolkit-Communicating-Publishing-Researching/dp/0985049146) (2013)

## Discussions
- [Reddit/HowToHack](https://www.reddit.com/r/HowToHack/) Learn and ask about hacking, security and pen testing.
- [Reddit/hacking](https://www.reddit.com/r/hacking) Discuss about hacking and web security.
- [ax0nes](https://ax0nes.com/) Hacking, security, and software development forum.
- [0Day.rocks on discord](https://discord.gg/WmYzJfD) Discord server about the 0day.rocks blog for technical and general InfoSec/Cyber discussions & latest news.
- [Reddit/AskNetsec](https://www.reddit.com/r/AskNetsec/) Discuss about network security, ask professionals for advices about jobs and stuff.

## Security Advisories

- [CVE](http://cve.mitre.org/)
- [CWE](http://cwe.mitre.org/)
- [NVD](http://web.nvd.nist.gov/)

## Challenges

- [Vulnhub](https://www.vulnhub.com/) - Has a lot of VMs to play with. Some are beginner friendly, some aren't.
- [Itsecgames](http://www.itsecgames.com/) - bWAPP or buggy web app is a deliberately insecure web application.
- [Dvwa](http://www.dvwa.co.uk/) - Damn Vulnerable Web Application is another deliberately insecure web application to practice your skills on.
- [Hackthissite](https://www.hackthissite.org/) - A site which provides challenges, CTFs, and more to improve your hacking skills.
- [Defend the Web](https://defendtheweb.net/) - Defend the Web is an interactive security platform where you can learn and challenge your skills.
- [Root-me](https://www.root-me.org/) - Another website which hosts challenges to test your hacking skills.
- [HackTheBox](https://www.hackthebox.eu/) - An online platform to test and advance your skills in penetration testing and cyber security.
- [Overthewire](http://overthewire.org/wargames/) - Learn and practice security concepts in the form of fun-filled games.
- [Ctftime](https://ctftime.org/) - The de facto website for everything CTF related. 
- [TryHackMe](https://tryhackme.com/) - TryHackMe is a free online platform for learning cyber security, using hands-on exercises and labs.
- [PicoCTF](https://picoctf.org/) - Provides you with fun CTF challenges of varying levels of difficulty to practice on.

([Table of Contents](#table-of-contents))

# License

This repository is under MIT license.

([Table of Contents](#table-of-contents))

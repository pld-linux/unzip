Summary:	Unpacks .zip files such as those made by pkzip under DOS
Summary(de):	entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte) 
Summary(es):	Descompacta archivos con extensión .zip, como los que crea pkzip en DOS
Summary(fr):	décompresse les fichiers .zip créés par pkzip sous DOS
Summary(ja):	Zip¥Õ¥¡¥¤¥ë²òÅà¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡¼
Summary(pl):	Unzip rozpakowuje pliki skompresowane programem pkzip i zgodnymi
Summary(pt_BR):	Descompacta arquivos com extensão .zip, como os criados pelo pkzip no DOS
Summary(tr):	pkzip ve benzeri programlarýn ürettiði zip arþivlerini açar
Name:		unzip
Version:	5.42
Release:	2
License:	distributable
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://ftp.freesoftware.com/pub/infozip/src/%{name}542.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unzip will list, test, or extract files from a ZIP archive, commonly
found on MS-DOS systems. A companion program, zip, creates ZIP
archives; both programs are compatible with archives created by
PKWARE's PKZIP and PKUNZIP for MS-DOS, but in many cases the program
options or default behaviors differ.

%description -l de
unzip dient zum Auflisten, Testen und Extrahieren von Dateien aus
ZIP-Archiven, wie sie oft unter MS-DOS erstellt werden. Das
Partnerprogramm ZIP erstellt ZIP-Archive. Beide Programme sind
kompatibel zu Archiven, die mit PKWARE ZIP und PKUNZIP für MS-DOS
komprimiert wurden, doch viele der Optionen und Standardeinstellungen
sind anders.

%description -l es
Descompacta archivos con extensión .zip, como los que se crean por
pkzip en DOS

%description -l fr
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip crée
des archives ZIP ; les deux programmes sont compatibles avec les
archives créées avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les
options ou comportements par défaut diffèrent fréquemment

%description -l ja
unzip ¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ï¡¢zip ½ñ¸Ë¤Î¥Õ¥¡¥¤¥ëÉ½¼¨¡¢¥Æ¥¹¥È¡¢²òÅà¤ò¹Ô¤¦¤Î¤Ë
»ÈÍÑ¤·¤Þ¤¹¡£zip ½ñ¸Ë¤Ï MS-DOS ¥·¥¹¥Æ¥à¤Ç¼ç¤Ë¸«¤é¤ì¤Þ¤¹¡£ zip
¥æ¡¼¥Æ¥£¥ê¥Æ¥£¤Ï zip ½ñ¸Ë¤òºî¤ë zip ¥Ñ¥Ã¥±¡¼¥¸¤Ë´Þ¤Þ¤ì¤Þ¤¹¡£ zip ¤È
unzip ¤Ï¤É¤Á¤é¤â MS-DOS ¾å¤Î PKWARE(R) ¤Î PKZIP ¤Ë¤è¤Ã¤ÆºîÀ®¤µ¤ì¤¿
½ñ¸Ë¤È¸ß´¹À­¤¬¤¢¤ê¤Þ¤¹¤¬¡¢¥×¥í¥°¥é¥à¤Î¥ª¥×¥·¥ç¥ó¤È¥Ç¥Õ¥©¥ë¥È¤Î¿¶Éñ¤Ï
¤¤¤¯¤Ä¤«¤ÎÅÀ¤Ç°ã¤¤¤¬¤¢¤ê¤Þ¤¹¡£

zip ½ñ¸Ë¤Î¥Õ¥¡¥¤¥ëÉ½¼¨¡¢¥Æ¥¹¥È¡¢²òÅà¤ò¹Ô¤¦É¬Í×¤¬¤¢¤ë¤Ê¤é¡¢ unzip
¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤·¤Þ¤·¤ç¤¦¡£

%description -l pl
Unzip pozwala na odczytanie zawarto¶ci, przetestowanie i rozpakowanie
archiwum ZIP, czêsto spotykanego w systemach opartych o MS-DOS.
Komplementarny program, zip, potrafi tak¿e tworzyæ archiwa ZIP.

%description -l pt_BR
Descompacta arquivos com extensão .zip, como os criados pelo pkzip no
DOS

%description -l tr
unzip, MS-DOS sistemlerinde sýkça rastlanan ZIP arþivlerini listeler,
içeriklerini doðrular ve açar. Bu programa eþlik eden zip, ZIP
arþivleri oluþturmakta kullanýlýr. Her iki program da MS-DOS için
PKWARE'in PKZIP ve PKUNZIP uygulamalarý ile uyumludur ancak çoðu
durumda seçeneklerinin kullanýlýþý farklýdýr.

%prep
%setup -q
%patch -p1 
rm -f Makefile
ln -sf unix/Makefile Makefile

%build
%ifarch %{ix86}
CFLAGS="%{rpmcflags}" %{__make} linux
%else
CFLAGS="%{rpmcflags}" %{__make} linux_noasm
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf README BUGS

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(pl) %{_mandir}/pl/man1/*

Summary:	unpacks .zip files such as those made by pkzip under DOS
Summary(de):	entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte) 
Summary(fr):	décompresse les fichiers .zip créés par pkzip sous DOS
Summary(pl):	Unzip rozpakowuje pliki skompresowane programem pkzip i zgodnymi
Summary(tr):	pkzip ve benzeri programlarýn ürettiði zip arþivlerini açar
Name:		unzip
Version:	5.42
Release:	1
Copyright:	distributable
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://ftp.freesoftware.com/pub/infozip/src/%{name}542.tar.gz
Patch:		%{name}-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
unzip will list, test, or extract files from a ZIP archive, commonly
found on MS-DOS systems.  A companion program, zip, creates ZIP
archives; both programs are compatible with archives created by
PKWARE's PKZIP and PKUNZIP for MS-DOS, but in many cases the program
options or default behaviors differ.

%description -l de
unzip dient zum Auflisten, Testen und Extrahieren von Dateien aus 
ZIP-Archiven, wie sie oft unter MS-DOS erstellt werden. Das 
Partnerprogramm ZIP erstellt ZIP-Archive. Beide Programme sind kompatibel 
zu Archiven, die mit PKWARE ZIP und PKUNZIP für MS-DOS komprimiert 
wurden, doch viele der Optionen und Standardeinstellungen sind anders. 

%description -l fr
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip crée
des archives ZIP ; les deux programmes sont compatibles avec les archives
créées avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les options ou
comportements par défaut diffèrent fréquemment

%description -l pl
Unzip pozwala na odczytanie zawarto¶ci, przetestowanie i rozpakowanie
archiwum ZIP, czêsto spotykanego w systemach opartych o MS-DOS.
Komplementarny program, zip, potrafi tak¿e tworzyæ archiwa ZIP.

%description -l tr
unzip, MS-DOS sistemlerinde sýkça rastlanan ZIP arþivlerini listeler,
içeriklerini doðrular ve açar. Bu programa eþlik eden zip, ZIP arþivleri
oluþturmakta kullanýlýr. Her iki program da MS-DOS için PKWARE'in PKZIP
ve PKUNZIP uygulamalarý ile uyumludur ancak çoðu durumda seçeneklerinin
kullanýlýþý farklýdýr.

%prep
%setup -q

%patch -p1 
rm -f Makefile
ln -sf unix/Makefile Makefile

%build
%ifarch %{ix86}
CFLAGS="%{rpmcflags}" make linux
%else
CFLAGS="%{rpmcflags}" make linux_noasm
%endif

%install
rm -rf $RPM_BUILD_ROOT 

%{__make} \
	install \
	prefix=$RPM_BUILD_ROOT/%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT/%{_mandir}/man1

gzip -9nf README BUGS

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*

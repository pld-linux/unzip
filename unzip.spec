Summary:     unpacks .zip files such as those made by pkzip under DOS
Summary(de): entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte) 
Summary(fr): d�compresse les fichiers .zip cr��s par pkzip sous DOS
Summary(pl): Unzip rozpakowuje pliki skompresowane programem pkzip i zgodnymi
Summary(tr): pkzip ve benzeri programlar�n �retti�i zip ar�ivlerini a�ar
Name:        unzip
Version:     5.40
Release:     2
Copyright:   distributable
Group:       Utilities/Archiving
Group(pl):   Narz�dzia/Archiwizacja
Source:      ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}540.tar.gz
Patch:       %{name}-opt.patch
Buildroot:   /tmp/%{name}-%{version}-root

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
zu Archiven, die mit PKWARE ZIP und PKUNZIP f�r MS-DOS komprimiert 
wurden, doch viele der Optionen und Standardeinstellungen sind anders. 

%description -l fr
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip cr�e
des archives ZIP ; les deux programmes sont compatibles avec les archives
cr��es avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les options ou
comportements par d�faut diff�rent fr�quemment

%description -l pl
Unzip pozwala na odczytanie zawarto�ci, przetestowanie i rozpakowanie
archiwum ZIP, cz�sto spotykanego w systemach opartych o MS-DOS.
Komplementarny program, zip, potrafi tak�e tworzy� archiwa ZIP.

%description -l tr
unzip, MS-DOS sistemlerinde s�k�a rastlanan ZIP ar�ivlerini listeler,
i�eriklerini do�rular ve a�ar. Bu programa e�lik eden zip, ZIP ar�ivleri
olu�turmakta kullan�l�r. Her iki program da MS-DOS i�in PKWARE'in PKZIP
ve PKUNZIP uygulamalar� ile uyumludur ancak �o�u durumda se�eneklerinin
kullan�l��� farkl�d�r.

%prep
%setup -q 
%patch -p1 
ln -sf unix/Makefile Makefile

%build
%ifarch i386
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" make linux 
%else
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" make linux_noasm 
%endif

%install
rm -rf $RPM_BUILD_ROOT 
make prefix=$RPM_BUILD_ROOT/usr install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*
gzip -9nf README BUGS

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(644, root, root, 755)
%doc README.gz BUGS.gz
%attr(755, root, root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Feb 10 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [5.40-2]
- added Group(pl)
- added gzipping documentation
- fixed pl translation

* Fri Dec 11 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [5.40-1]
- removed -c %setup option,
- added gzipping man pages.

* Tue Oct 13 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [5.31-4]
- added pl translation,
- added using $RPM_OPT_FLAGS during compile,
- allow building from non root account,
- removed COPYING and INSTALL from docs.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- builds on non i386 platforms

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- updated the version

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

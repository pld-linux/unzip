Summary:	Unpacks .zip files such as those made by pkzip under DOS
Summary(de):	entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte)
Summary(es):	Descompacta archivos con extensiСn .zip, como los que crea pkzip en DOS
Summary(fr):	dИcompresse les fichiers .zip crИИs par pkzip sous DOS
Summary(ja):	Zip╔у╔║╔╓╔К╡РеЮ╔Ф║╪╔ф╔ё╔Й╔ф╔ё║╪
Summary(pl):	Unzip rozpakowuje pliki skompresowane programem pkzip i zgodnymi
Summary(pt_BR):	Descompacta arquivos com extensЦo .zip, como os criados pelo pkzip no DOS
Summary(ru):	Распаковщик файлов .zip
Summary(tr):	pkzip ve benzeri programlarЩn ЭrettiПi zip arЧivlerini aГar
Summary(uk):	Розпаковувач файл╕в .zip
Name:		unzip
Version:	5.51
Release:	2
License:	distributable
Group:		Applications/Archiving
#Source0:	ftp://ftp.info-zip.org/pub/infozip/src/%{name}551.tar.gz
Source0:	ftp://sunsite.icm.edu.pl/pub/unix/archiving/info-zip/src/%{name}551.tar.gz
# Source0-md5:	8a25712aac642430d87d21491f7c6bd1
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d7f8b0b09f6e8d89591b4dc25e335764
Patch0:		%{name}-opt.patch
URL:		http://www.info-zip.org/
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
kompatibel zu Archiven, die mit PKWARE ZIP und PKUNZIP fЭr MS-DOS
komprimiert wurden, doch viele der Optionen und Standardeinstellungen
sind anders.

%description -l es
Descompacta archivos con extensiСn .zip, como los que se crean por
pkzip en DOS

%description -l fr
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip crИe
des archives ZIP ; les deux programmes sont compatibles avec les
archives crИИes avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les
options ou comportements par dИfaut diffХrent frИquemment

%description -l ja
unzip ╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓о║╒zip ╫Я╦к╓н╔у╔║╔╓╔Ки╫╪╗║╒╔ф╔╧╔х║╒╡РеЮ╓Р╧т╓╕╓н╓к
╩хмя╓╥╓ч╓╧║ёzip ╫Я╦к╓о MS-DOS ╔╥╔╧╔ф╔Ю╓г╪Г╓к╦╚╓И╓Л╓ч╓╧║ё zip
╔Ф║╪╔ф╔ё╔Й╔ф╔ё╓о zip ╫Я╦к╓Р╨Н╓К zip ╔я╔ц╔╠║╪╔╦╓к╢ч╓ч╓Л╓ч╓╧║ё zip ╓х
unzip ╓о╓и╓а╓И╓Б MS-DOS ╬Е╓н PKWARE(R) ╓н PKZIP ╓к╓Х╓ц╓ф╨Ню╝╓╣╓Л╓©
╫Я╦к╓х╦ъ╢╧ю╜╓╛╓╒╓Й╓ч╓╧╓╛║╒╔в╔М╔╟╔И╔Ю╓н╔╙╔в╔╥╔Г╔С╓х╔г╔у╔╘╔К╔х╓н©╤иЯ╓о
╓╓╓╞╓д╓╚╓нею╓г╟Ц╓╓╓╛╓╒╓Й╓ч╓╧║ё

zip ╫Я╦к╓н╔у╔║╔╓╔Ки╫╪╗║╒╔ф╔╧╔х║╒╡РеЮ╓Р╧т╓╕и╛мв╓╛╓╒╓К╓й╓И║╒ unzip
╔я╔ц╔╠║╪╔╦╓Р╔╓╔С╔╧╔х║╪╔К╓╥╓ч╓╥╓Г╓╕║ё

%description -l pl
Unzip pozwala na odczytanie zawarto╤ci, przetestowanie i rozpakowanie
archiwum ZIP, czЙsto spotykanego w systemach opartych o MS-DOS.
Komplementarny program, zip, potrafi tak©e tworzyФ archiwa ZIP.

%description -l pt_BR
Descompacta arquivos com extensЦo .zip, como os criados pelo pkzip no
DOS

%description -l ru
Unzip выдает список, проверяет целостность и извлекает файлы из
архивов ZIP, довольно широко распространенных в мире DOS.
Сопутствующая программа, zip, создает архивы ZIP. Обе программы
совместимы с архивами созданными PKZIP и PKUNZIP от PKWARE для MS-DOS,
но во многих случаях опции или умолчания отличаются.

%description -l tr
unzip, MS-DOS sistemlerinde sЩkГa rastlanan ZIP arЧivlerini listeler,
iГeriklerini doПrular ve aГar. Bu programa eЧlik eden zip, ZIP
arЧivleri oluЧturmakta kullanЩlЩr. Her iki program da MS-DOS iГin
PKWARE'in PKZIP ve PKUNZIP uygulamalarЩ ile uyumludur ancak ГoПu
durumda seГeneklerinin kullanЩlЩЧЩ farklЩdЩr.

%description -l uk
Unzip вида╓ перел╕к, перев╕ря╓ ц╕л╕сн╕сть та видобува╓ файли з арх╕в╕в
ZIP, досить широко розповсюджених у св╕т╕ DOS. В╕дпов╕дна програма,
zip, створю╓ арх╕ви ZIP. Обидв╕ програми сум╕сн╕ з арх╕вами створеними
PKZIP та PKUNZIP в╕д PKWARE для MS-DOS, але в багатьох випадках опц╕╖
або умовчання в╕др╕зняються.

%prep
%setup -q
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README BUGS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(pl) %{_mandir}/pl/man1/*

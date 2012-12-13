#
# TODO:		bzip2 support
#
Summary:	Unpacks .zip files such as those made by pkzip under DOS
Summary(de.UTF-8):	entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte)
Summary(es.UTF-8):	Descompacta archivos con extensión .zip, como los que crea pkzip en DOS
Summary(fr.UTF-8):	décompresse les fichiers .zip créés par pkzip sous DOS
Summary(ja.UTF-8):	Zipファイル解凍ユーティリティー
Summary(pl.UTF-8):	Unzip rozpakowuje pliki skompresowane programem pkzip i zgodnymi
Summary(pt_BR.UTF-8):	Descompacta arquivos com extensão .zip, como os criados pelo pkzip no DOS
Summary(ru.UTF-8):	Распаковщик файлов .zip
Summary(tr.UTF-8):	pkzip ve benzeri programların ürettiği zip arşivlerini açar
Summary(uk.UTF-8):	Розпаковувач файлів .zip
Name:		unzip
Version:	6.00
Release:	2
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://ftp.info-zip.org/pub/infozip/src/%{name}60.tgz
# Source0-md5:	62b490407489521db863b523a7f86375
#Source0:	ftp://sunsite.icm.edu.pl/pub/unix/archiving/info-zip/src/%{name}552.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d7f8b0b09f6e8d89591b4dc25e335764
Patch0:		%{name}-opt.patch
Patch2:		%{name}-cve-2005-4667.patch
Patch3:		%{name}-method99_hint.patch
URL:		http://www.info-zip.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		Werror_cflags	%{nil}

%description
unzip will list, test, or extract files from a ZIP archive, commonly
found on MS-DOS systems. A companion program, zip, creates ZIP
archives; both programs are compatible with archives created by
PKWARE's PKZIP and PKUNZIP for MS-DOS, but in many cases the program
options or default behaviors differ.

%description -l de.UTF-8
unzip dient zum Auflisten, Testen und Extrahieren von Dateien aus
ZIP-Archiven, wie sie oft unter MS-DOS erstellt werden. Das
Partnerprogramm ZIP erstellt ZIP-Archive. Beide Programme sind
kompatibel zu Archiven, die mit PKWARE ZIP und PKUNZIP für MS-DOS
komprimiert wurden, doch viele der Optionen und Standardeinstellungen
sind anders.

%description -l es.UTF-8
Descompacta archivos con extensión .zip, como los que se crean por
pkzip en DOS

%description -l fr.UTF-8
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip crée
des archives ZIP ; les deux programmes sont compatibles avec les
archives créées avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les
options ou comportements par défaut diffèrent fréquemment

%description -l ja.UTF-8
unzip ユーティリティは、zip 書庫のファイル表示、テスト、解凍を行うのに
使用します。zip 書庫は MS-DOS システムで主に見られます。 zip
ユーティリティは zip 書庫を作る zip パッケージに含まれます。 zip と
unzip はどちらも MS-DOS 上の PKWARE(R) の PKZIP によって作成された
書庫と互換性がありますが、プログラムのオプションとデフォルトの振舞は
いくつかの点で違いがあります。

zip 書庫のファイル表示、テスト、解凍を行う必要があるなら、 unzip
パッケージをインストールしましょう。

%description -l pl.UTF-8
Unzip pozwala na odczytanie zawartości, przetestowanie i rozpakowanie
archiwum ZIP, często spotykanego w systemach opartych o MS-DOS.
Komplementarny program, zip, potrafi także tworzyć archiwa ZIP.

%description -l pt_BR.UTF-8
Descompacta arquivos com extensão .zip, como os criados pelo pkzip no
DOS

%description -l ru.UTF-8
Unzip выдает список, проверяет целостность и извлекает файлы из
архивов ZIP, довольно широко распространенных в мире DOS.
Сопутствующая программа, zip, создает архивы ZIP. Обе программы
совместимы с архивами созданными PKZIP и PKUNZIP от PKWARE для MS-DOS,
но во многих случаях опции или умолчания отличаются.

%description -l tr.UTF-8
unzip, MS-DOS sistemlerinde sıkça rastlanan ZIP arşivlerini listeler,
içeriklerini doğrular ve açar. Bu programa eşlik eden zip, ZIP
arşivleri oluşturmakta kullanılır. Her iki program da MS-DOS için
PKWARE'in PKZIP ve PKUNZIP uygulamaları ile uyumludur ancak çoğu
durumda seçeneklerinin kullanılışı farklıdır.

%description -l uk.UTF-8
Unzip видає перелік, перевіряє цілісність та видобуває файли з архівів
ZIP, досить широко розповсюджених у світі DOS. Відповідна програма,
zip, створює архіви ZIP. Обидві програми сумісні з архівами створеними
PKZIP та PKUNZIP від PKWARE для MS-DOS, але в багатьох випадках опції
або умовчання відрізняються.

%prep
%setup -q -n %{name}60
%patch0 -p1
%patch2 -p1
%patch3 -p1

ln -sf unix/Makefile Makefile

%build
# NOTE: unix/configure creates flags file with guessed values
%{__make} unzips \
	CC="%{__cc}" \
	AS="%{__cc}" \
%ifarch %{ix86}
	CF="%{rpmcflags} -I. -Wall -DASM_CRC -DLARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT -DUNICODE_WCHAR -DUNICODE_SUPPORT -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DHAVE_DIRENT_H -DHAVE_TERMIOS_H -D_MBCS" \
	AF="-Di386 %{rpmldflags}" \
	CRCA_O="crc_gcc.o" \
	LD="%{__cc} %{rpmcflags} -I. -Wall -DASM_CRC -DLARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT -DUNICODE_WCHAR -DUNICODE_SUPPORT -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DHAVE_DIRENT_H -DHAVE_TERMIOS_H -D_MBCS"
%else
	CF="%{rpmcflags} -I. -Wall" \
	LD="%{__cc} %{rpmcflags} -I. -Wall"
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/README.unzip-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COPYING.OLD History.600 LICENSE README ToDo WHERE file_id.diz *.txt proginfo
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(pl) %{_mandir}/pl/man1/*

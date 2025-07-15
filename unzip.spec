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
Release:	6
License:	distributable
Group:		Applications/Archiving
Source0:	ftp://ftp.info-zip.org/pub/infozip/src/%{name}60.tgz
# Source0-md5:	62b490407489521db863b523a7f86375
#Source0:	ftp://sunsite.icm.edu.pl/pub/unix/archiving/info-zip/src/%{name}552.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d7f8b0b09f6e8d89591b4dc25e335764
Patch100:	unzip-opt.patch
# Not sent to upstream.
Patch1: unzip-6.0-bzip2-configure.patch
# Upstream plans to do this in zip (hopefully also in unzip).
Patch2: unzip-6.0-exec-shield.patch
# Upstream plans to do similar thing.
Patch3: unzip-6.0-close.patch
# Details in rhbz#532380.
# Reported to upstream: http://www.info-zip.org/board/board.pl?m-1259575993/
Patch4: unzip-6.0-attribs-overflow.patch
# Not sent to upstream, as it's Fedora/RHEL specific.
# Modify the configure script to accept var LFLAGS2 so linking can be configurable
# from the spec file. In addition '-s' is still removed as before
Patch5: unzip-6.0-configure.patch
Patch6: unzip-6.0-manpage-fix.patch
# Update match.c with recmatch() from zip 3.0's util.c
# This also resolves the license issue in that old function.
# Original came from here: https://projects.parabolagnulinux.org/abslibre.git/plain/libre/unzip-libre/match.patch
Patch7: unzip-6.0-fix-recmatch.patch
# Update process.c
Patch8: unzip-6.0-symlink.patch
# change using of macro "case_map" by "to_up"
Patch9: unzip-6.0-caseinsensitive.patch
# downstream fix for "-Werror=format-security"
# upstream doesn't want hear about this option again
Patch10: unzip-6.0-format-secure.patch

Patch11: unzip-6.0-valgrind.patch
Patch12: unzip-6.0-x-option.patch
Patch13: unzip-6.0-overflow.patch
Patch14: unzip-6.0-cve-2014-8139.patch
Patch15: unzip-6.0-cve-2014-8140.patch
Patch16: unzip-6.0-cve-2014-8141.patch
Patch17: unzip-6.0-overflow-long-fsize.patch

# Fix heap overflow and infinite loop when invalid input is given (#1260947)
Patch18: unzip-6.0-heap-overflow-infloop.patch

# support non-{latin,unicode} encoding
Patch19: unzip-6.0-alt-iconv-utf8.patch
Patch20: unzip-6.0-alt-iconv-utf8-print.patch
Patch21: 0001-Fix-CVE-2016-9844-rhbz-1404283.patch

# restore unix timestamp accurately
Patch22: unzip-6.0-timestamp.patch

# fix possible heap based stack overflow in passwd protected files
Patch23: unzip-6.0-cve-2018-1000035-heap-based-overflow.patch

Patch24: unzip-6.0-cve-2018-18384.patch

# covscan issues
Patch25: unzip-6.0-COVSCAN-fix-unterminated-string.patch

Patch26: unzip-zipbomb-part1.patch
Patch27: unzip-zipbomb-part2.patch
Patch28: unzip-zipbomb-part3.patch
Patch29: unzip-zipbomb-manpage.patch
Patch30: unzip-zipbomb-part4.patch
Patch31: unzip-zipbomb-part5.patch
Patch32: unzip-zipbomb-part6.patch
Patch33: unzip-zipbomb-switch.patch
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
%patch -P100 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1
%patch -P21 -p1
%patch -P22 -p1
%patch -P23 -p1
%patch -P24 -p1
%patch -P25 -p1

%patch -P26 -p1
%patch -P27 -p1
%patch -P28 -p1
%patch -P29 -p1
%patch -P30 -p1
%patch -P31 -p1
%patch -P32 -p1
%patch -P33 -p1

%build
# IZ_HAVE_UXUIDGID is needed for right functionality of unzip -X
# NOMEMCPY solve problem with memory overlapping - decomression is slowly,
# but successfull.
#
# NOTE: unix/configure creates flags file with guessed values
X86_OPT1=""
X86_OPT2=""
%ifarch %{ix86}
X86_OPT1="-Di386"
X86_OPT2="-DASM_CRC"
%endif

%{__make} -f unix/Makefile generic \
	CC="%{__cc}" \
	AS="%{__cc}" \
	CF_NOOPT="%{rpmcppflags} %{rpmcflags} -I. -Wall ${X86_OPT2} -DLARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT -DUNICODE_WCHAR -DUNICODE_SUPPORT -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DHAVE_DIRENT_H -DHAVE_TERMIOS_H -D_MBCS -DNOMEMCPY -DIZ_HAVE_UXUIDGID" \
	AF="${X86_OPT} %{rpmldflags}" \
%ifarch %{ix86}
	CRCA_O="crc_gcc.o" \
%endif
	LFLAGS2="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f unix/Makefile install \
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

Summary:	Unpacks .zip files such as those made by pkzip under DOS
Summary(de):	entpackt .zip-Dateien (etwa mit pkzip unter DOS erstellte)
Summary(es):	Descompacta archivos con extensi�n .zip, como los que crea pkzip en DOS
Summary(fr):	d�compresse les fichiers .zip cr��s par pkzip sous DOS
Summary(ja):	Zip�ե��������桼�ƥ���ƥ���
Summary(pl):	Unzip rozpakowuje pliki skompresowane programem pkzip i zgodnymi
Summary(pt_BR):	Descompacta arquivos com extens�o .zip, como os criados pelo pkzip no DOS
Summary(ru):	����������� ������ .zip
Summary(tr):	pkzip ve benzeri programlar�n �retti�i zip ar�ivlerini a�ar
Summary(uk):	������������ ���̦� .zip
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
kompatibel zu Archiven, die mit PKWARE ZIP und PKUNZIP f�r MS-DOS
komprimiert wurden, doch viele der Optionen und Standardeinstellungen
sind anders.

%description -l es
Descompacta archivos con extensi�n .zip, como los que se crean por
pkzip en DOS

%description -l fr
unzip liste, teste ou extrait des fichiers d'une archive ZIP. zip cr�e
des archives ZIP ; les deux programmes sont compatibles avec les
archives cr��es avec PKZIP et PKUNZIP de PKWARE pour MS-DOS, mais les
options ou comportements par d�faut diff�rent fr�quemment

%description -l ja
unzip �桼�ƥ���ƥ��ϡ�zip ��ˤΥե�����ɽ�����ƥ��ȡ������Ԥ��Τ�
���Ѥ��ޤ���zip ��ˤ� MS-DOS �����ƥ�Ǽ�˸����ޤ��� zip
�桼�ƥ���ƥ��� zip ��ˤ��� zip �ѥå������˴ޤޤ�ޤ��� zip ��
unzip �Ϥɤ���� MS-DOS ��� PKWARE(R) �� PKZIP �ˤ�äƺ������줿
��ˤȸߴ���������ޤ������ץ����Υ��ץ����ȥǥե���Ȥο����
�����Ĥ������ǰ㤤������ޤ���

zip ��ˤΥե�����ɽ�����ƥ��ȡ������Ԥ�ɬ�פ�����ʤ顢 unzip
�ѥå������򥤥󥹥ȡ��뤷�ޤ��礦��

%description -l pl
Unzip pozwala na odczytanie zawarto�ci, przetestowanie i rozpakowanie
archiwum ZIP, cz�sto spotykanego w systemach opartych o MS-DOS.
Komplementarny program, zip, potrafi tak�e tworzy� archiwa ZIP.

%description -l pt_BR
Descompacta arquivos com extens�o .zip, como os criados pelo pkzip no
DOS

%description -l ru
Unzip ������ ������, ��������� ����������� � ��������� ����� ��
������� ZIP, �������� ������ ���������������� � ���� DOS.
������������� ���������, zip, ������� ������ ZIP. ��� ���������
���������� � �������� ���������� PKZIP � PKUNZIP �� PKWARE ��� MS-DOS,
�� �� ������ ������� ����� ��� ��������� ����������.

%description -l tr
unzip, MS-DOS sistemlerinde s�k�a rastlanan ZIP ar�ivlerini listeler,
i�eriklerini do�rular ve a�ar. Bu programa e�lik eden zip, ZIP
ar�ivleri olu�turmakta kullan�l�r. Her iki program da MS-DOS i�in
PKWARE'in PKZIP ve PKUNZIP uygulamalar� ile uyumludur ancak �o�u
durumda se�eneklerinin kullan�l��� farkl�d�r.

%description -l uk
Unzip ����� ����̦�, ����צ�Ѥ æ̦�Φ��� �� ��������� ����� � ��Ȧצ�
ZIP, ������ ������ �������������� � �צԦ DOS. �����צ��� ��������,
zip, ������� ��Ȧ�� ZIP. ����צ �������� ��ͦ�Φ � ��Ȧ���� ����������
PKZIP �� PKUNZIP צ� PKWARE ��� MS-DOS, ��� � �������� �������� ��æ�
��� ��������� צ�Ҧ��������.

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

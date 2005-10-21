Summary:	Software for programming Atmel AVR Microcontrollers
Summary(pl):	Oprogramowanie do programowania mikrokontrolerów Atmel AVR
Name:		avrdude
Version:	4.4.0
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avrdude/%{name}-%{version}.tar.gz
# Source0-md5:	e9aec3dfaa022d5c6878aa355d69c83d
Patch0:		%{name}-info.patch
URL:		http://savannah.nongnu.org/projects/avrdude/
BuildRequires:	automake
BuildRequires:	readline-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts-latex
BuildRequires:	tetex-format-pdftex
BuildRequires:	tetex-format-plain
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description -l pl
AVRDUDE to oprogramowanie do programowania mikrokontrolerów Atmel AVR.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README doc/avrdude-html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/avr*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf

Summary:	Software for programming Atmel AVR Microcontrollers
Summary(pl.UTF-8):	Oprogramowanie do programowania mikrokontrolerów Atmel AVR
Name:		avrdude
Version:	5.3.1
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avrdude/%{name}-%{version}.tar.gz
# Source0-md5:	58c2be9f7a864b930ed9e6f1858f5cc7
Patch0:		%{name}-info.patch
Patch1:		%{name}-doc.patch
Patch2:		%{name}-configure.patch
URL:		http://savannah.nongnu.org/projects/avrdude/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libusb-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	bison
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description -l pl.UTF-8
AVRDUDE to oprogramowanie do programowania mikrokontrolerów Atmel AVR.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ac_cv_lib_termcap_tputs=no \
	--enable-doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README 
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/*
%{_infodir}/avrdude.info*

Summary:	software for programming Atmel AVR Microcontrollers
Name:		avrdude
Version:	4.2.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://jubal.westnet.com/AVR/%{name}-%{version}.tar.gz
# Source0-md5:	dd8027d4fd238f47a61651867c9c8d10
URL:		http://savannah.nongnu.org/projects/avrdude/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%prep
%setup -q

%build
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
%config(noreplace) %verify(not md5 size mtime) /etc/%{name}.conf

Summary:	Software for programming Atmel AVR Microcontrollers
Summary(pl):	Oprogramowanie do programowania mikrokontrolerów Atmel AVR
Name:		avrdude
Version:	5.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://savannah.nongnu.org/download/avrdude/%{name}-%{version}.tar.gz
# Source0-md5:	ac21da160853f7cf7f3f0578c756a52c
URL:		http://savannah.nongnu.org/projects/avrdude/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description -l pl
AVRDUDE to oprogramowanie do programowania mikrokontrolerów Atmel AVR.

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}.conf

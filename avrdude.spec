# TODO: shared library
#       package python gui demonstrator, requires swig, python and Qt5 or Qt6
Summary:	Software for programming Atmel AVR Microcontrollers
Summary(pl.UTF-8):	Oprogramowanie do programowania mikrokontrolerów Atmel AVR
Name:		avrdude
Version:	8.0
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	https://github.com/avrdudes/avrdude/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f62d33439f6c5b2239467372864c5e41
Patch0:		%{name}-info.patch
Patch1:		%{name}-doc.patch
Patch2:		shebang.patch
URL:		https://github.com/avrdudes/avrdude
BuildRequires:	bison
BuildRequires:	cmake >= 3.14
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	hidapi-devel
BuildRequires:	libusb-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVRDUDE is software for programming Atmel AVR Microcontrollers.

%description -l pl.UTF-8
AVRDUDE to oprogramowanie do programowania mikrokontrolerów Atmel AVR.

%package devel
Summary:	AVRDUDE static library and development includes
Summary(pl.UTF-8):	Biblioteka stayczna i pliki nagłówkowe AVRDUDE
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
AVRDUDE static library and development includes

%description devel -l pl.UTF-8
Biblioteka stayczna i pliki nagłówkowe AVRDUDE

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build
install -d build
cd build
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF \
	-DBUILD_DOC=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/avrdude
%attr(755,root,root) %{_bindir}/elf2tag
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man?/*
%{_infodir}/avrdude.info*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libavrdude.a
%{_includedir}/libavrdude.h
%{_includedir}/libavrdude-avrintel.h

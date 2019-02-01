%define major	8
%define akaimajor 0
%define tarballname libgig
%define libname %mklibname %{name} %{major}
%define libakai %mklibname %{name}-akai %{akaimajor}
%define devname %mklibname %{name} -d
%define devakai %mklibname %{name}-akai -d

Name:		gig
Version:	4.1.0
Release:	1
Summary:	C++ library for loading Gigasampler files and DLS Level 1/2 files
License:	GPLv2 and LGPL
# Note akai library is LGPL
Group:		Sound/Utilities
Source0:	http://download.linuxsampler.org/packages/libgig-%{version}.tar.bz2
URL:		http://www.linuxsampler.org/libgig/

BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	doxygen
Requires:	%{libname} = %{version}-%{release}

%description
C++ library for accessing Gigasampler/GigaStudio, DLS,
SoundFont and KORG sound files.

%package -n %{libname}
Summary:	C++ library for loading Gigasampler files and DLS Level 1/2 files
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
C++ library for loading Gigasampler files and DLS Level 1/2 files.

%package -n %{devname}
Summary:	Header files for developers
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Requires:	%{_lib}uuid-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{tarballname}-devel = %{version}-%{release}

%description -n %{devname}
Header files for developers.

%package -n %{libakai}
Summary:	C++ library for accessing AKAI disk images
Group:		System/Libraries
License:	LGPL

%description -n %{libakai}
Akai lib

%package -n %{devakai}
Summary:	Header files for developers
Group:		System/Libraries
License:	LGPL
Requires:	%{libakai} = %{version}-%{release}
Provides:	%{name}-akai-devel = %{version}-%{release}

%description -n %{devakai}
Header files for developers.

%prep
%setup -q -n lib%{name}-%{version}

%build
%configure
%make_build
make docs

%install
%make_install
find %{buildroot} -name "*.la" -delete

mv %{buildroot}/%{_libdir}/libgig/* %{buildroot}/%{_libdir}/
rm -rf %{buildroot}/%{_libdir}/libgig

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/html
%{_mandir}/man1/*
%{_bindir}/*

%files  -n %{libname}
%{_libdir}/libgig.so.%{major}
%{_libdir}/libgig.so.%{major}.*

%files  -n %{devname}
%{_includedir}/*
#{_libdir}/libgig.a
%{_libdir}/libgig.so
%{_libdir}/pkgconfig/gig.pc

%files -n %{libakai}
%{_libdir}/libakai.so.%{akaimajor}
%{_libdir}/libakai.so.%{akaimajor}.*

%files  -n %{devakai}
#{_libdir}/libakai.a
%{_libdir}/libakai.so
%{_libdir}/pkgconfig/akai.pc




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.0-2mdv2011.0
+ Revision: 618471
- the mass rebuild of 2010.0 packages

* Thu Aug 27 2009 Emmanuel Andry <eandry@mandriva.org> 3.3.0-1mdv2010.0
+ Revision: 421759
- New version 3.3.0

* Sun Sep 07 2008 Emmanuel Andry <eandry@mandriva.org> 3.2.1-3mdv2009.0
+ Revision: 282392
- apply devel policy
- add gcc43 patch from gentoo
- use configure2_5x

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 14 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.2.1-1mdv2008.1
+ Revision: 120265
- Fix BuildRequires
- import gig



%define	major	6
%define	libname	%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d
%define oname  libgig

Name:          gig
Summary:       C++ library for loading Gigasampler files
Version:       3.2.1
Release:       %mkrel 3
License:       GPLv2+
Group:	       System/Libraries 
Source0:       %{oname}-%{version}.tar.bz2
Patch0:		libgig-gcc-4.3.patch
URL: 	       http://www.linuxsampler.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libsndfile-devel

%description
C++ library for loading Gigasampler files and DLS Level 1/2 files.

%files 
%defattr(-,root,root)
%{_bindir}/dlsdump
%{_bindir}/gigdump
%{_bindir}/gigextract
%{_bindir}/rifftree
%{_mandir}/man1/dlsdump.1.*
%{_mandir}/man1/gigdump.1.*
%{_mandir}/man1/gigextract.1.*
%{_mandir}/man1/rifftree.1.*

#--------------------------------------------------------------------

%package -n	%libname
Group: 		System/Libraries
Summary: 	Libraries for %name
Provides: 	lib%name = %version-%release

%description -n %libname 
C++ library for loading Gigasampler files and DLS Level 1/2 files

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libgig.so.%{major}*

#--------------------------------------------------------------------

%package -n	%develname
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%libname = %version-%release
Provides:	lib%name-devel = %version-%release
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}%{name}6-devel

%description -n	%develname
Development libraries from %oname

%files -n %develname
%defattr (-,root,root)
%{_includedir}/DLS.h
%{_includedir}/RIFF.h
%{_includedir}/gig.h
%{_libdir}/libgig.a
%{_libdir}/libgig.la
%{_libdir}/libgig.so
%{_libdir}/pkgconfig/gig.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %oname-%version
%patch0

%build
make -f Makefile.cvs
%configure2_5x
make

%install
make DESTDIR=%buildroot  install

%clean


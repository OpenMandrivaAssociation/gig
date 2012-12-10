%define	major	6
%define	libname	%mklibname %{name} %{major}
%define	develname	%mklibname %{name} -d
%define oname  libgig

Name:          gig
Summary:       C++ library for loading Gigasampler files
Version:       3.3.0
Release:       3
License:       GPLv2+
Group:	       System/Libraries 
Source0:       %{oname}-%{version}.tar.bz2
Patch0:		libgig-gcc-4.3.patch
URL: 	       http://www.linuxsampler.org/
BuildRequires: pkgconfig(sndfile)

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
%{_libdir}/libgig.so
%{_libdir}/pkgconfig/gig.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %oname-%version
%patch0

%build
#make -f Makefile.cvs
%configure2_5x
make

%install
make DESTDIR=%buildroot  install

%clean



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



%define	major	12
%define	akaimajor 0
%define	tarballname libgig
%define	libname %mklibname %{name} %{major}
%define	libakai %mklibname %{name}-akai %{akaimajor}
%define	devname %mklibname %{name} -d
%define	devakai %mklibname %{name}-akai -d

Summary:	C++ library for loading Gigasampler files and DLS Level 1/2 files
Name:	gig
Version:	4.5.0
Release:	1
# Note: akai library is LGPL
License:	GPLv2 and LGPL
Group:	Sound/Utilities
Url:		https://www.linuxsampler.org/libgig/
Source0:	https://download.linuxsampler.org/packages/libgig-%{version}.tar.bz2
# We want the library files in %%_libdir, not in %%_libdir/libgig
Patch0:	libgig-4.5.0-fix-libdir.patch
BuildRequires:	doxygen
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(uuid)
Requires:	%{libname} = %{version}-%{release}

%description
C++ library for accessing Gigasampler/GigaStudio, DLS, SoundFont and KORG
sound files.

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/html
%{_bindir}/*
%{_mandir}/man1/*

#-----------------------------------------------------------------------------


%package -n %{libname}
Summary:	C++ library for loading Gigasampler files and DLS Level 1/2 files
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
C++ library for loading Gigasampler files and DLS Level 1/2 files.

%files  -n %{libname}
%{_libdir}/libgig.so.%{major}
%{_libdir}/libgig.so.%{major}.*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files for developers
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(uuid)
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{tarballname}-devel = %{version}-%{release}

%description -n %{devname}
Header files for developers using %{libname}.

%files  -n %{devname}
%{_includedir}/libgig/*.h
%{_libdir}/libgig.so
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%package -n %{libakai}
Summary:	C++ library for accessing AKAI disk images
Group:	System/Libraries
License:	LGPLv2

%description -n %{libakai}
Akai library for accessing AKAI disk images.

%files -n %{libakai}
%{_libdir}/libakai.so.%{akaimajor}
%{_libdir}/libakai.so.%{akaimajor}.*

#-----------------------------------------------------------------------------

%package -n %{devakai}
Summary:	Header files for developers
Group:	Development/C++
License:	LGPLv2
Requires:	%{libakai} = %{version}-%{release}
Provides:	%{name}-akai-devel = %{version}-%{release}

%description -n %{devakai}
Header files for developers using akai library.

%files  -n %{devakai}
%{_libdir}/libakai.so
%{_libdir}/pkgconfig/akai.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{tarballname}-%{version}


%build
autoreconf -vfi
%configure
%make_build

doxygen -u
make docs


%install
%make_install

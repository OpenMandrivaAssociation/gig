%define	oname libgig
%define	major	14
%define	akaimajor 0
%define	libname %mklibname %{name} %{major}
%define	libakai %mklibname %{name}-akai %{akaimajor}
%define	devname %mklibname %{name} -d
%define	devakai %mklibname %{name}-akai -d

Summary:	C++ library for loading Gigasampler files and DLS Level 1/2 files
Name:	gig
Version:	4.6.0
Release:	2
# Note: akai library is LGPL
License:	GPLv2 and LGPL-2.0
Group:	Sound/Utilities
Url:		https://www.linuxsampler.org/libgig/
Source0:	https://download.linuxsampler.org/packages/%{oname}-%{version}.tar.bz2
# We want the libraries in %%{_libdir}, not %%{_libdir}/%%{name},
# otherwise linuxsampler cannot find them at build time...
# Need to be rediffed when updating the package
Patch0:	libgig-4-6.0-fix-libdir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	libtool-base
BuildRequires:	make
#BuildRequires:	slibtool
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(uuid)
Requires:	%{libname} = %{version}-%{release}

%description
C++ library for accessing Gigasampler/GigaStudio, DLS, SoundFont and KORG
sound files.

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO doc/html
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
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{devname}
Header files for developers using %{libname}.

%files  -n %{devname}
%{_includedir}/%{oname}/*.h
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
%autosetup -p1 -n %{oname}-%{version}

# Fix FSF address
sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/31 Milk Street, # 960789, Boston, MA 02196, USA/g' COPYING
sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/31 Milk Street, # 960789, Boston, MA 02196, USA/g' src/Akai.h


%build
# Slibtool won't work with libgig
ln -sf %{_bindir}/libtoolize slibtoolize
export PATH=$PWD:$PATH
export LIBTOOLIZE=%{_bindir}/libtoolize
export LIBTOOL=%{_bindir}/libtool
autoreconf -vfi
%configure
%make_build

doxygen -u
make docs


%install
%make_install

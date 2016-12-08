%define oname bZRTP
%define lname %(echo %oname | tr [:upper:] [:lower:])

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	An opensource implementation of ZRTP keys exchange protocol
Name:		%{lname}
Version:	1.0.4
Release:	0
License:	GPLv2+
Group:		Communications
URL:		https://www.linphone.org/technical-corner/%{name}
#Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	http://download-mirror.savannah.gnu.org/releases/linphone/%{name}/%{name}-%{version}.tar.gz
Source1:	http://download-mirror.savannah.gnu.org/releases/linphone/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:		%{name}-1.0.4-pkgconfig.patch

BuildRequires:	cmake
BuildRequires:	cmake(BcToolbox)
BuildRequires:	pkgconfig(libxml-2.0)

%description
%{oname} is an opensource implementation of ZRTP keys exchange protocol. 
The library written in C 89 is fully portable and can be executed on
many platforms including both ARM processor and x86. 

#--------------------------------------------------------------------

%package -n	%{libname}
Summary:	An opensource implementation of ZRTP keys exchange protocol
Group:		System/Libraries

%description -n	%{libname}
%{oname} is an opensource implementation of ZRTP keys exchange protocol. 
The library written in C 89 is fully portable and can be executed on
many platforms including both ARM processor and x86.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%doc COPYING

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers, libraries and docs for the bZRTP library
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains header files and development libraries needed to
develop programs using the %{oname} library.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_datadir}/%{name}/cmake/
%doc README
%doc NEWS
%doc AUTHORS
#doc ChangeLog
#doc INSTALL
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b.orig

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DENABLE_SHARED:BOOL=ON \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_TESTS:BOOL=OFF
%make

%install
%makeinstall_std -C build


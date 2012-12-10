%define _disable_ld_no_undefined 1

%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Free HDL simulator
Name:		freehdl
Version:	0.0.7
Release:	3
License:	GPL
Group:		Sciences/Other
URL:		http://freehdl.seul.org/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool

%description
A project to develop a free, open source, GPL'ed VHDL simulator for Linux.

%files
%doc AUTHORS COPYING HACKING INSTALL NEWS README README.AIRE README.gen-nodes README.libraries README.v2cc README.vaul
%{_bindir}/freehdl-gennodes
%{_bindir}/freehdl-v2cc
%{_bindir}/gvhdl
%{_datadir}/%{name}
%{_infodir}/fire.info.*
%{_mandir}/man?/*

#----------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared libraries for %{name}.

%files -n %{libname}
%{_libdir}/freehdl/libieee.so.%{major}*
%{_libdir}/libfreehdl-cdfggen.so.%{major}*
%{_libdir}/libfreehdl-fire.so.%{major}*
%{_libdir}/libfreehdl-kernel.so.%{major}*
%{_libdir}/libfreehdl-std.so.%{major}*
%{_libdir}/libfreehdl-vaul.so.%{major}*

#----------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_bindir}/freehdl-config
%{_includedir}/%{name}
%{_libdir}/freehdl/libieee.so
%{_libdir}/libfreehdl-cdfggen.so
%{_libdir}/libfreehdl-fire.so
%{_libdir}/libfreehdl-kernel.so
%{_libdir}/libfreehdl-std.so
%{_libdir}/libfreehdl-vaul.so
%{_libdir}/freehdl/libieee.a
%{_libdir}/libfreehdl-cdfggen.a
%{_libdir}/libfreehdl-fire.a
%{_libdir}/libfreehdl-kernel.a
%{_libdir}/libfreehdl-std.a
%{_libdir}/libfreehdl-vaul.a
%{_libdir}/pkgconfig/%{name}.pc

#----------------------------------------------------------------

%prep
%setup -q
autoreconf -fi

%build
%configure --with-gnu-ld --with-pic
%make

%install
%makeinstall_std



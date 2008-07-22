%define name 	freehdl
%define version 0.0.6
%define release 1

Summary: 	Free HDL simulator
Name: 		%{name}
Version: 	%{version}
Release: 	%mkrel %{release}
License: 	GPL
Group: 		Sciences/Other
URL: 		http://freehdl.seul.org/
Source0: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	bison, flex, libtool

%description
A project to develop a free, open source, GPL'ed VHDL simulator for Linux.

%prep
%setup -q

%build
%configure --with-gnu-ld --with-pic
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING HACKING INSTALL NEWS README README.AIRE README.gen-nodes README.libraries README.v2cc README.vaul
%{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/*
%{_datadir}/%{name}
%{_infodir}/fire.info.lzma
%{_mandir}/man?/*

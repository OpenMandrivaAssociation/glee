%define major 0d1
%define libname %mklibname glee %major
%define libname_devel %mklibname -d glee

Name:          glee
Version:       5.4.0
Release:       1
Summary:       GL Easy Extension library
Group:         System/X11
License:       BSD
Url:           http://elf-stone.com/glee.php
Source0:       http://elf-stone.com/downloads/GLee/GLee-%{version}-src.tar.gz
# includedir point to /usr/include instead of /usr/include/GL (default location)
# from Debian
Source1:       glee-%{version}.pc
Patch0:        glee-5.4.0-Makefile_in.patch
Patch1:        glee-5.4.0-GLXContextID.patch
BuildRequires: pkgconfig(gl)

%description
GLee (GL Easy Extension library) is a 
free cross-platform extension 
loading library for OpenGL. It
provides seamless support for 
OpenGL functions up to version 
3.0 and 398 extensions.

Features:

 * Core functions up to OpenGL 3.0
 * 398 extensions
 * Lazy loading for extension functions, 
 so no initialisation code is required
 * Forced extension loading, 
 though the GLeeForceLink function.

%package -n %libname
Summary:          Library files for %{name}
Group:            System/X11
Provides:         %{name} = %{version}

%description -n %libname
GLee (GL Easy Extension library) is a free cross-platform extension loading library for OpenGL.

%package -n %libname_devel
Group:         Development/C++
Summary:       Devel package for %{name}
Requires:      %libname = %{version}-%{release}
Provides:      %{name}-devel = %{version}

%description -n %libname_devel
GLee (GL Easy Extension library) is a free cross-platform extension loading library for OpenGL.

This package contains static libraries and header files need for development.

%prep
%setup -q -c
%patch0 -p0
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

chmod 755 %{buildroot}%{_libdir}/*.so*

mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -pm 644 %SOURCE1 %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%files -n %libname
%{_libdir}/lib%{name}.so.*
%doc readme.txt

%files -n %libname_devel
%{_includedir}/GLee.h
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%doc extensionList.txt




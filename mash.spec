Summary:	A library for using real 3D models within a Clutter scene
Name:		mash
Version:	0.2.0
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://github.com/downloads/clutter-project/mash/%{name}-%{version}.tar.xz
# Source0-md5:	9eda552784291707e667be4d55917794
URL:		http://wiki.clutter-project.org/wiki/Mash
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel
BuildRequires:	cogl-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package devel
Summary:	Header files for mash library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for mash library.

%package apidocs
Summary:	mash API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API and internal documentation for mash library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libmash-0.2.so.0
%attr(755,root,root) %{_libdir}/libmash-0.2.so.*.*.*
%{_libdir}/girepository-1.0/Mash-0.2.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmash-0.2.so
%{_datadir}/gir-1.0/Mash-0.2.gir
%{_includedir}/mash-0.2
%{_pkgconfigdir}/mash-0.2.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/mash


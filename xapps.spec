%define major           1
%define girmajor        1.0
%define libname         %mklibname xapp %{major}
%define develname       %mklibname xapp -d
%define girname         %mklibname xapp-gir %{girmajor}

Name:           xapps
Version:        1.6.1
Release:        1
Summary:        Common files for XApp desktop apps

License:        LGPLv2+
URL:            https://github.com/linuxmint/xapps/
Source0:        https://github.com/linuxmint/xapps/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %url/flags/archive/1.0.2.tar.gz
Group:          Development/Other

BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  libgnomekbd-devel
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	vala-devel
BuildRequires:	meson
BuildRequires:	python-gi
BuildRequires:	python2-gi
Requires:       python-gi
Requires:       inxi
Requires:       xdg-utils
Requires:       fpaste

%description
This package includes files that are shared between several XApp
apps (i18n files and configuration schemas).

%package -n %{libname}
Group:          System/Libraries
Summary:        JavaScript bindings based on %{name}
Obsoletes:      %{_lib}xapps0 < 1.0.2-2

%description -n %{libname}
This package contains JavaScript bindings based on %{name}.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       %{girname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes:      %{_lib}xapps-devel < 1.0.2-2

%description -n %{develname}
Files for development with %{name}.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}
Obsoletes:      %{_lib}xapps-gir1.0 < 1.0.2-2

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q

%autopatch -p1

tar -xf %{SOURCE1} -C files/usr/share --strip 3

rm files/usr/share/format

%build
%meson

%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%find_lang xapp

%files -f xapp.lang
%doc README.md COPYING
%{_bindir}/pastebin
%{_bindir}/upload-system-info
%{_bindir}/xfce4-set-wallpaper
%{_datadir}/iso-flag-png/
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{python3_sitearch}/gi/overrides/XApp.py*
%{python2_sitearch}/gi/overrides/XApp.py*
%{python3_sitearch}/gi/overrides/__pycache__
%{_libexecdir}/xapps/mate-panel/*
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet

%files -n %{libname}
%{_libdir}/libxapp.so.%{major}
%{_libdir}/libxapp.so.%{major}.*

%files -n %{girname}
%{_libdir}/girepository-1.0/XApp-1.0.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libxapp.so
%{_libdir}/pkgconfig/xapp.pc
%{_datadir}/gir-1.0/XApp-1.0.gir
%{_datadir}/glade/catalogs/xapp-glade-catalog.xml
%{_datadir}/vala/vapi/xapp.vapi
%{_datadir}/vala/vapi/xapp.deps

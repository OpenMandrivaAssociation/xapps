%define oname           xapp
%define major           1
%define girmajor        3.2
%define libname         %mklibname xapp
%define oldlibname      %mklibname xapp 1
%define develname       %mklibname xapp -d
%define girname         %mklibname xapp-gir %{girmajor}

Name:           %{oname}
Version:        3.2.2
Release:        1
Summary:        Common files for XApp desktop apps
Group:          Development/Other
License:        LGPLv2+
URL:            https://github.com/linuxmint/xapps/
Source0:        https://github.com/linuxmint/xapps/archive/%{version}/%{oname}-%{version}.tar.gz

BuildSystem:    meson

BuildRequires:	gnome-common
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	intltool
BuildRequires:	gobject-introspection-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	libgnomekbd-devel
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	vala-devel
BuildRequires:	mold
BuildRequires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(pygobject)
Requires:	python-gobject3
Requires:	inxi
Requires:	xdg-utils
Requires:	fpaste
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

Obsoletes:      xapps < %{EVRD}

%description
This package includes files that are shared between several XApp
apps (i18n files and configuration schemas).

%package -n %{libname}
Group:          System/Libraries
Summary:        JavaScript bindings based on %{name}
Requires:       %{name} = %{version}-%{release}
Obsoletes:      %{_lib}xapps0 < %{EVRD}
Obsoletes:      %{_lib}xapps0 < %{EVRD}
Obsoletes:      %{_lib}xapp1 < %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
This package contains JavaScript bindings based on %{name}.

%package -n %{develname}
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       %{girname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes:      %{_lib}xapps-devel < %{EVRD}

%description -n %{develname}
Files for development with %{name}.

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries

Obsoletes:      %{_lib}xapps-gir1.0 < %{EVRD}
Obsoletes:      %{_lib}xapp-gir2.6 < %{EVRD}
Obsoletes:      %{_lib}xapp-gir2.8 < %{EVRD}

%description -n %{girname}
GObject Introspection interface description for %{name}.


%conf -p
%global optflags %{optflags} -fuse-ld=mold
export CC=gcc
export CXX=g++


%install -a
find %{buildroot} -name '*.la' -delete

%find_lang xapp

%files -f xapp.lang
%doc README.md COPYING
%{_bindir}/pastebin
%{_bindir}/upload-system-info
%{_bindir}/xfce4-set-wallpaper
%{_bindir}/xapp-gpu-offload
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{python3_sitearch}/gi/overrides/XApp.py*
%{_libexecdir}/xapps/mate-xapp-status-applet.py
%{_libexecdir}/xapps/applet_constants.py
#{_libexecdir}/xapps/sn-watcher/xapp-sn-watcher
%{_sysconfdir}/xdg/autostart/xapp-sn-watcher.desktop
%{_sysconfdir}/X11/xinit/xinitrc.d/80xapp-gtk3-module.sh
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet
%{_datadir}/dbus-1/services/org.x.StatusNotifierWatcher.service

%files -n %{libname}
%{_libdir}/libxapp.so.%{major}
%{_libdir}/libxapp.so.%{girmajor}*
%{_libdir}/xapps/xapp-sn-watcher

%files -n %{girname}
%{_libdir}/girepository-1.0/XApp-1.0.typelib

%files -n %{develname}
%{_includedir}/*
%{_libdir}/libxapp.so
%{_libdir}/gtk-3.0/modules/libxapp-gtk3-module.so
%{_libdir}/pkgconfig/xapp.pc
%{_datadir}/gir-1.0/XApp-1.0.gir
%{_datadir}/glade/catalogs/xapp-glade-catalog.xml
%{_datadir}/vala/vapi/xapp.vapi
%{_datadir}/vala/vapi/xapp.deps

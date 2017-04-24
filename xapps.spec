%define major           1
%define girmajor        1.0
%define libname         %mklibname xapp %{major}
%define develname       %mklibname xapp -d
%define girname         %mklibname xapp-gir %{girmajor}

Name:           xapps
Version:        1.0.2
Release:        1
Summary:        Common files for XApp desktop apps

License:        LGPLv2+
URL:            https://github.com/linuxmint
Source0:        %url/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %url/flags/archive/1.0.1.tar.gz#/flags-1.0.1.tar.gz
Group:          Development/Other

BuildRequires:  gnome-common
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  libgnomekbd-devel
Requires:       python-gobject
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

%apply_patches

tar -xf %{SOURCE1} -C files/usr/share --strip 3

rm files/usr/share/format

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make V=1


%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%files
%doc README.md COPYING
%{_bindir}/pastebin
%{_bindir}/upload-system-info
%{_bindir}/xfce4-set-wallpaper
%{_datadir}/iso-flag-png/
%{_datadir}/glib-2.0/schemas/org.x.apps.*.xml
%{_datadir}/icons/hicolor/scalable/actions/xapp-*-symbolic.svg

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


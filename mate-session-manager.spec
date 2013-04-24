Summary:	The mate desktop programs for the MATE GUI desktop environment
Name:		mate-session-manager
Version:	1.4.0
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{lua: print (string.match(rpm.expand("%{version}"),"%d+.%d+"))}/%{name}-%{version}.tar.xz
Source1:	startmate
Source2:	materc

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mateconf-sanity-check
BuildRequires:	mate-conf
BuildRequires:	xmlto
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	x11-xtrans-devel

Requires:	desktop-common-data
Requires:	mateconf-sanity-check
Requires:	mate-conf
#Requires:	mate-user-docs
Requires:	mate-settings-daemon
Requires:	%{name}-bin >= %{EVRD}

%description
MATE (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.

The MATE Session Manager restores a set session (group of applications)
when you log into MATE.

%package bin
Group: %{group}
Summary: %{summary}

%description bin
This package contains the binaries for the MATE Session Manager, but 
no startup scripts. It is meant for applications such as GDM that use 
mate-session internally.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/doc/mate-session/dbus/mate-session.html

# wmsession session file
mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat << EOF > %{buildroot}%{_sysconfdir}/X11/wmsession.d/05MATE
NAME=MATE
ICON=mate
DESC=MATE Environment
EXEC=%{_bindir}/startmate
SCRIPT:
exec %{_bindir}/startmate
EOF

install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/startmate
install -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/materc

%find_lang %{name}



%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/mate-session-properties
%{_bindir}/mate-session-save
%{_bindir}/mate-wm
%{_datadir}/applications/*
%{_datadir}/xsessions/mate.desktop
%{_mandir}/man1/mate-session-properties.*
%{_mandir}/man1/mate-session-save.1.xz
%{_mandir}/man1/mate-wm.1.xz
%config %{_sysconfdir}/X11/wmsession.d/*

%files bin
%{_sysconfdir}/mateconf/schemas/mate-session.schemas
%{_sysconfdir}/materc
%{_bindir}/mate-session
%{_bindir}/startmate
%{_datadir}/mate-session
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/mate-session.*



%changelog
* Sat Jun 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.2.0-3
+ Revision: 804161
- add wmsession file

* Thu Jun 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-2
+ Revision: 803180
- rebuild dropping non-existent mate-user-docs

* Sat Jun 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802055
- imported package mate-session-manager


%define major 17
%define libname %mklibname %{name} %{major}
%define libgui %mklibname %{name}gui %{major}
%define _disable_lto 1

Summary:	A sound editor for KDE
Name:		kwave
Version:	17.08.0
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Sound
Url:		http://kwave.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kwave/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5WidgetsAddons)
Buildrequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	id3lib-devel
BuildRequires:	librsvg
Requires:	lame
Suggests:	twolame

%description
Kwave is a sound editor designed for the KDE Desktop Environment.

With Kwave you can edit many sorts of wav-files including multi-channel
files. You are able to alter and play back each channel on its own.
Kwave also includes many plugins (most are still under development) to
transform the wave-file in several ways and presents a graphical view
with a complete zoom- and scroll capability.

%files -f %{name}.lang
%doc CHANGES README TODO
%{_bindir}/%{name}
%{_iconsdir}/*/*/*/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/org.kde.kwave.desktop
%{_libdir}/qt5/plugins/kwave
%{_datadir}/kservicetypes5/kwave-plugin.desktop
%{_datadir}/metainfo/org.kde.kwave.appdata.xml

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries needed by %{name}
Group:		System/Libraries

%description -n %{libname}
Libraries needed for %{name}.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libgui}
Summary:	Libraries needed by %{name}
Group:		System/Libraries
Conflicts:	%{_lib}kwave0 < 0.8.10

%description -n %{libgui}
Libraries needed for %{name}.

%files -n %{libgui}
%{_libdir}/lib%{name}gui.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q
# FIXME workaround for clang 5.0-305643 compile time error
# causes an undefined reference to a template variable
export CXX=g++
%cmake_kde5 -DWITH_MP3=ON

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

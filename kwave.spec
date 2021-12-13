%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	A sound editor for KDE
Name:		kwave
Version:	21.12.0
Release:	1
License:	GPLv2+
Group:		Sound
Url:		http://kwave.sourceforge.net/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kwave-19.07.80-compile.patch
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
BuildRequires:	pkgconfig(zlib)
BuildRequires:	id3lib-devel >= 3.8.1
BuildRequires:	librsvg
Requires:	lame
Suggests:	twolame
Obsoletes:	%mklibname %{name} 17
Obsoletes:	%mklibname %{name}gui 17
Obsoletes:	%mklibname %{name} 18
Obsoletes:	%mklibname %{name}gui 18
Obsoletes:	%mklibname %{name} 19
Obsoletes:	%mklibname %{name}gui 19

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
# Those are really internal libraries that can't be used by anything else.
# They also aren't optional. There's no point in splitting them into lib
# packages.
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}gui.so.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5 -DWITH_MP3=ON

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

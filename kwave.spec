%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%ifarch znver1
# Workaround for crash on startup with default flags
%global optflags -O3 -march=znver1 -mtune=znver1 -mmmx -msse -msse2 -mssse3 -msse4a -msse4.1 -msse4.2 -mavx -mavx2 -msha -maes -mclflushopt -mfsgsbase -mrdrnd -mfma -mrdseed -mpopcnt -madx -mbmi -mbmi2 -mfxsr -mxsave -mxsaveopt -mxsavec -mxsaves -mmwaitx -mclzero -mfpmath=sse -g3 -gdwarf-4 -flto
%endif

Summary:	A sound editor for KDE
Name:		kwave
Version:	24.12.0
Release:	2
License:	GPLv2+
Group:		Sound
Url:		https://kwave.sourceforge.net/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
#Patch0:		kwave-19.07.80-compile.patch
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
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
BuildRequires:	pkgconfig(alsa)
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
# For converting icons
BuildRequires:	imagemagick
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
%doc CHANGES TODO
%{_bindir}/%{name}
%{_iconsdir}/*/*/*/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/org.kde.kwave.desktop
%{_libdir}/qt5/plugins/kwave
%{_datadir}/metainfo/org.kde.kwave.appdata.xml
# Those are really internal libraries that can't be used by anything else.
# They also aren't optional. There's no point in splitting them into lib
# packages.
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}gui.so.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
# As of 22.03.80/90 an error occur on aarch64 during compilation when converting images.
# With disabled imagemagick and only enabled librsvg converting success on x86_64 but on aarch64 filing at configure time
# with error:  "Found rsvg but conversion failed, falling back to convert from ImageMagick" and using imagemagick on aarch64 cause convert failure.
# Let's disable for now building documentation on aarch64.
%cmake_kde5 \
%ifarch aarch64
            -DWITH_DOC=OFF \
%endif            
            -DWITH_MP3=ON

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

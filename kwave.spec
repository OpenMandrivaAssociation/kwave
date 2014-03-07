%define major 0
%define libname %mklibname %{name} %{major}

Summary:	A sound editor for KDE
Name:		kwave
Version:	0.8.10
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Sound
Url:		http://kwave.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/kwave/%{name}-%{version}-1.tar.bz2
BuildRequires:	imagemagick
BuildRequires:	kdelibs4-devel
Buildrequires:	libid3-devel
Buildrequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(audiofile)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(flac++)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(samplerate) >= 0.1.3
BuildRequires:	pkgconfig(vorbis)

%description
Kwave is a sound editor designed for the KDE Desktop Environment.

With Kwave you can edit many sorts of wav-files including multi-channel
files. You are able to alter and play back each channel on its own.
Kwave also includes many plugins (most are still under development) to
transform the wave-file in several ways and presents a graphical view
with a complete zoom- and scroll capability.

%files -f %{name}.lang
%doc CHANGES README TODO
%{_kde_bindir}/%{name}
%{_kde_iconsdir}/*/*/apps/%{name}.*
%{_kde_iconsdir}/*/*/actions/%{name}*
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_datadir}/apps/%{name}
%{_kde_libdir}/kde4/plugins/%{name}

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries needed by %{name}
Group:		System/Libraries

%description -n %{libname}
Libraries needed for %{name}

%files -n %{libname}
%{_kde_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DWITH_GSL=OFF -DWITH_MP3=ON -DWITH_DOC=OFF
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html


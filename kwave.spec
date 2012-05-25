%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	A sound editor for KDE
Name:		kwave
Version: 	0.8.8
Release: 	%mkrel 1
Epoch:		1
Source0: 	http://prdownloads.sourceforge.net/kwave/%name-%version-1.tar.bz2
Group:  	Sound
License:	GPLv2+
URL:		http://kwave.sourceforge.net/
BuildRequires:	kdelibs4-devel
Buildrequires:	libalsa-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	libflac++-devel
BuildRequires:	audiofile-devel
Buildrequires:	libid3-devel
BuildRequires:	mad-devel
BuildRequires:	libsamplerate-devel >= 0.1.3
BuildRequires:	imagemagick
BuildRequires:	kdesdk4-po2xml
BuildRequires:	fftw3-devel
Obsoletes:	%{name}-devel < 0.8.3

%description
Kwave is a sound editor designed for the KDE Desktop Environment.

With Kwave you can edit many sorts of wav-files including multi-channel
files. You are able to alter and play back each channel on its own.
Kwave also includes many plugins (most are still under development) to
transform the wave-file in several ways and presents a graphical view
with a complete zoom- and scroll capability.

%package -n	%{libname}
Summary:	Libraries needed by %{name}
Group:		System/Libraries

%description -n	%{libname}
Libraries needed for %{name}

%prep
%setup -q

%build
%if 0
#emuse: fix ambiguous int to QString conversions
perl -i -e "s/QString(0)/QString(\"\")/g" plugins/sonogram/SonogramDialog.cpp
perl -i -e "s/_group(0)/_group(\"\")/g" libgui/KwaveFileDialog.cpp libgui/MenuItem.cpp 
perl -i -e "s/last_url \= 0/last_url \= \"\"/g" libgui/KwaveFileDialog.h 
perl -i -e "s/last_ext \= 0/last_ext \= \"\"/g" libgui/KwaveFileDialog.h 
#fwang: gsl disabled due to license incompatible
#emuse: disable broken documentation
%endif
%cmake_kde4 -DWITH_GSL=OFF -DWITH_MP3=ON -DWITH_DOC=OFF
%make

%install
%makeinstall_std -C build
%find_lang %{name} --with-html

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES README TODO
%{_kde_bindir}/%{name}
%{_kde_iconsdir}/*/*/apps/%{name}.*
%{_kde_iconsdir}/*/*/actions/%{name}*
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_datadir}/apps/%{name}
%{_kde_libdir}/kde4/plugins/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_kde_libdir}/lib*.so.%{major}*

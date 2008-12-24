%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	A sound editor for KDE
Name:		kwave
Version: 	0.8.1
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
BuildRequires:	imagemagick
BuildRequires:	kdesdk4-po2xml
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A sound editor for KDE.

%package -n	%{libname}
Summary:	Libraries needed by %{name}
Group:		System/Libraries

%description -n	%{libname}
Libraries needed for %{name}

%package -n	%{develname}
Summary:	Development files provdied by %{name}
Group:		Development/KDE and Qt
Obsoletes:	%libname-devel
Provides:	%{name}-devel = %epoch:%version-%release
Requires:	%libname = %epoch:%version-%release
Conflicts:	%libname < 1:0.7.10-2mdk

%description -n %{develname}
This package contains development files provided by %{name}.

%prep
%setup -q

%build
#fwang: gsl disabled due to license incompatible
%cmake_kde4 -DWITH_GSL=OFF -DWITH_MP3=ON
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%find_lang %{name} --with-html

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES README TODO
%{_kde_bindir}/%{name}
%{_kde_iconsdir}/*/*/apps/%{name}.png
%{_kde_datadir}/applications/kde4/%{name}.desktop
%{_kde_datadir}/apps/%{name}
%{_kde_libdir}/kde4/plugins/%{name}

%files -n %{libname}
%defattr(-,root,root)
%{_kde_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_kde_libdir}/*.so

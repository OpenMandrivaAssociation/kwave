%define	major	0
%define	libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	A sound editor for KDE
Name:		kwave
Version: 	0.7.11
Release: 	%mkrel 1
Epoch:		1
Source0: 	http://ovh.dl.sourceforge.net/sourceforge/kwave/%{name}-%{version}.tar.gz
Patch0:		kwave-0.7.10-remove-fr-comment.patch
Patch1:		kwave-0.7.11-fix-desktop-entry.patch
Group:  	Sound
License:	GPLv2+
URL:		http://kwave.sourceforge.net/
BuildRequires:	kdelibs-devel oggvorbis-devel mad-devel
BuildRequires:	imagemagick gettext cmake
BuildRequires:	libflac++-devel jackit-devel gsl-devel libid3_3.8-devel
BuildRequires:	esound-devel recode arts-devel kdesdk-po2xml kdemultimedia-arts-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A sound editor for KDE3.

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
%patch0 -p0
%patch1 -p0

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
cd build
%makeinstall_std
cd -

%find_lang %{name} --with-html

install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

desktop-file-install	--vendor="" --delete-original \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications \
			--add-category="Qt" \
			--add-category="KDE" \
			--add-category="Audio" \
			%{buildroot}%{_datadir}/applnk/Multimedia/%{name}.desktop

rm -fr %{buildroot}%{_datadir}/doc/%{name}*

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
%doc %{_docdir}/HTML/en/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/audio/*.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so

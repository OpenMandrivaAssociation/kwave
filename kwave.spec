%define	name	kwave
%define	version	0.7.9

%define	major	0
%define	libname	%mklibname %{name} %{major}

Summary:	A sound editor for KDE
Name:		%{name}
Version: 	%{version}
Release: 	%mkrel 1
Source0: 	http://ovh.dl.sourceforge.net/sourceforge/kwave/%{name}-%{version}.tar.gz
Group:  	Sound
License:	GPL
URL:		http://kwave.sourceforge.net/
BuildRequires:	kdelibs-devel oggvorbis-devel mad-devel
BuildRequires:	imagemagick gettext
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

%package -n	%{libname}-devel
Summary:	Development tools for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libname}-devel
This package contains the development libraries
for development with %{name}.

%prep
%setup -q

%build
# fwang: it doesn't build against latest flac.
# The author suggest remove it at the time.
# See: http://sourceforge.net/tracker/index.php?func=detail&aid=1713655&group_id=6478&atid=106478
rm -fr plugins/codec_flac
CONFIGURE_OPTS="--with-install-root=$RPM_BUILD_ROOT ${CONFIGURE_OPTS}"
make -f Makefile.dist
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

desktop-file-install	--vendor="" \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications \
			--add-category="Qt" \
			--add-category="KDE" \
			--add-category="Audio" \
			--add-category="X-MandrivaLinux-Multimedia-Sound" \
			%{buildroot}%{_datadir}/applnk/Multimedia/%{name}.desktop

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES README TODO
%doc %{_docdir}/HTML/en/%{name}
%lang(fr) %doc %{_docdir}/HTML/fr/%{name}
%lang(de) %doc %{_docdir}/HTML/de/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/mimelnk/audio/*.desktop
%{_datadir}/applnk/Multimedia/%{name}.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/apps/%{name}
%dir %{_libdir}/kde3/plugins/%{name}
%{_libdir}/kde3/plugins/%{name}/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.la
%{_libdir}/lib*.so


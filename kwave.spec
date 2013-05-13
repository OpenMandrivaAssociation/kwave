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
BuildRequires:	pkgconfig(samplerate) >= 0.1.3
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


%changelog
* Fri May 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1:0.8.8-1mdv2012.0
+ Revision: 800732
- fix file list
- spec cleanup

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 0.8.8

  + Funda Wang <fwang@mandriva.org>
    - new version 0.8.7

* Wed Mar 09 2011 Funda Wang <fwang@mandriva.org> 1:0.8.6-1
+ Revision: 642983
- New version 0.8.6

* Mon Dec 20 2010 Frank Kober <emuse@mandriva.org> 1:0.8.5-3mdv2011.0
+ Revision: 623298
- bump release
- fix ambiguous int to Qstring conversions

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Thu Dec 24 2009 Funda Wang <fwang@mandriva.org> 1:0.8.5-1mdv2010.1
+ Revision: 482068
- new version 0.8.5

* Mon Sep 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:0.8.4-2mdv2010.0
+ Revision: 450734
- rebuild for missing binaries

* Sun Sep 27 2009 Funda Wang <fwang@mandriva.org> 1:0.8.4-1mdv2010.0
+ Revision: 449957
- BR samplerate
- new version 0.8.4

* Sat Jul 04 2009 Funda Wang <fwang@mandriva.org> 1:0.8.3-2mdv2010.0
+ Revision: 392270
- New version 0.8.3-2

* Tue Jun 30 2009 Funda Wang <fwang@mandriva.org> 1:0.8.3-1mdv2010.0
+ Revision: 390782
- no more devel files
- New version 0.8.3

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1:0.8.2-1mdv2010.0
+ Revision: 369386
- New versio 0.8.2
- update description

* Wed Dec 24 2008 Funda Wang <fwang@mandriva.org> 1:0.8.1-1mdv2009.1
+ Revision: 318219
- fix file list
- BR fftw3
- new version 0.8.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Oct 02 2008 Funda Wang <fwang@mandriva.org> 1:0.8.0-1mdv2009.1
+ Revision: 290731
- enable mp3 decoder support
- New version 0.8.0 (kde4 version)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 26 2008 Funda Wang <fwang@mandriva.org> 1:0.7.11-1mdv2008.1
+ Revision: 158425
- fix desktop entry
- New version 0.7.11

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 1:0.7.10-4mdv2008.0
+ Revision: 77316
- another fix for fr comment

* Sat Sep 01 2007 Funda Wang <fwang@mandriva.org> 1:0.7.10-3mdv2008.0
+ Revision: 77298
- remove invalid fr comment of mimelnk

* Thu Aug 23 2007 Funda Wang <fwang@mandriva.org> 1:0.7.10-2mdv2008.0
+ Revision: 69955
- bring back devel packages

* Thu Aug 23 2007 Funda Wang <fwang@mandriva.org> 1:0.7.10-1mdv2008.0
+ Revision: 69902
- New version 0.7.10

* Sun Jun 17 2007 Funda Wang <fwang@mandriva.org> 0.8.0-0.2008.1mdv2008.0
+ Revision: 40506
- New svn snapshot
- Remove wrong doc files
- drop old patch
  svn snapshot
  use cmake
- Fix x86-64 libdir
- buildrequires imagemagick gettext
- Fix file list
- Fix build requires
- New version


* Tue Aug 22 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.6-1mdv2007.0
- 0.7.6
- xdg menu

* Tue Sep 20 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.3-3mdk
- fix build on older releases (only apply on P0 on new releases)

* Tue Sep 20 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.3-2mdk
- fix buildrequires

* Tue Sep 20 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.7.3-1mdk
- initial release (club request)


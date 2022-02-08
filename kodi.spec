%define _legacy_common_support 1

%global         PYTHON %{__python3}
%global		LIBDVDCSS_VERSION 1.4.2-Leia-Beta-5
%global		LIBDVDREAD_VERSION 6.0.0-Leia-Alpha-3
%global		LIBDVDNAV_VERSION 6.0.0-Leia-Alpha-3

# Tips thanks to:
# https://www.archlinux.org/packages/community/x86_64/kodi/
# https://gitweb.gentoo.org/repo/gentoo.git/tree/media-tv/kodi
%global  _firewalldpath   /usr/lib/firewalld/services

%global debug_package %{nil} 

%global _fmt_version 6.1.2

# Commit for kodi
%global commit0 49a04cd6a7f49ea9a0f05c492b11a3ba7c542a99
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: kodi
Version: 19.3
Release: 8%{dist}
Epoch: 1
Summary: Media center

License: GPLv2+ and GPLv3+ and LGPLv2+ and BSD and MIT
# Main binary and all supporting files are GPLv2+/GPLv3+
# Some supporting libraries use the LGPL / BSD / MIT license
Group: Applications/Multimedia
URL: https://www.kodi.tv/
Source0: https://github.com/xbmc/xbmc/archive/%{commit0}.zip#/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/xbmc/FFmpeg/archive/refs/tags/4.3.2-Matrix-19.2.tar.gz
Source2: kodi-snapshot
Source3: http://mirrors.kodi.tv/build-deps/sources/fmt-%{_fmt_version}.tar.gz
Source4: tv.kodi.kodi.metainfo.xml 
Source5: https://github.com/xbmc/libdvdcss/archive/%{LIBDVDCSS_VERSION}.tar.gz#/libdvdcss-%{LIBDVDCSS_VERSION}.tar.gz
Source6: https://github.com/xbmc/libdvdread/archive/%{LIBDVDREAD_VERSION}.tar.gz#/libdvdread-%{LIBDVDREAD_VERSION}.tar.gz
Source7: https://github.com/xbmc/libdvdnav/archive/%{LIBDVDNAV_VERSION}.tar.gz#/libdvdnav-%{LIBDVDNAV_VERSION}.tar.gz
Patch: smb_fix.patch
#Patch1: 17300.patch
Patch4: cheat-sse-build.patch


%global _with_libbluray 1
%global _with_cwiid 1
%global _with_libssh 1
%global _with_libcec 1
%global _with_internal_ffmpeg 0
%global _with_internal_fmt 0
%global _with_wayland 0


%ifarch x86_64 i686
%global _with_crystalhd 1
%endif

# Upstream does not support ppc64
ExcludeArch: ppc64

BuildRequires: git
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconfig(xrandr)
BuildRequires: SDL2-devel
BuildRequires: SDL2_image-devel
BuildRequires: a52dec-devel
BuildRequires: afpfs-ng-devel
BuildRequires: avahi-devel
BuildRequires: bluez-libs-devel
BuildRequires: boost-devel
BuildRequires: bzip2-devel
BuildRequires: cmake
BuildRequires: crossguid-devel
%if 0%{?_with_cwiid}
BuildRequires: cwiid-devel >= 3.0.0
%endif
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: e2fsprogs-devel
BuildRequires: enca-devel
BuildRequires: expat-devel
BuildRequires: faad2-devel
%if 0%{?_with_internal_ffmpeg}
BuildRequires: ffmpeg-devel >= 5.0
%endif
BuildRequires: libdrm-devel
BuildRequires: flac-devel
BuildRequires: flex
BuildRequires: fontconfig-devel
BuildRequires: fontpackages-devel
BuildRequires: freetype-devel
BuildRequires: fribidi-devel
%if 0%{?el6}
BuildRequires: gettext-devel
%else
BuildRequires: gettext-autopoint
%endif
BuildRequires: glew-devel
BuildRequires: glib2-devel
BuildRequires: gperf
BuildRequires: jasper-devel
%if 0%{?fedora} <= 32
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: java-11-openjdk-devel
%else
BuildRequires: java-devel 
%endif
BuildRequires: lame-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXtst-devel
BuildRequires: libass-devel >= 0.9.7
%if 0%{?_with_libbluray}
BuildRequires: libbluray-devel
%endif
BuildRequires: libcap-devel
BuildRequires: libcdio-devel
%if 0%{?fedora} >= 24
BuildRequires: libcec-devel >= 4.0.0
%endif
%if 0%{?_with_crystalhd}
BuildRequires: libcrystalhd-devel
%endif
BuildRequires: libcurl-devel
BuildRequires: libdca-devel
BuildRequires: libdvdread-devel
%if 0%{?el6}
BuildRequires: libjpeg-devel
%else
BuildRequires: libjpeg-turbo-devel
%endif
BuildRequires: libmad-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libmms-devel
BuildRequires: libmodplug-devel
BuildRequires: libmpcdec-devel
BuildRequires: libmpeg2-devel
BuildRequires: libnfs-devel
BuildRequires: libogg-devel
# for AirPlay support
BuildRequires: shairplay-devel
BuildRequires: libplist-devel
BuildRequires: libpng-devel
BuildRequires: librtmp-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsmbclient-devel
%if 0%{?_with_libssh}
BuildRequires: libssh-devel
%endif
BuildRequires: libtiff-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
%ifnarch %{arm}
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
%endif
BuildRequires: libunistring-devel
BuildRequires: libvorbis-devel
%if 0%{?_with_wayland}
BuildRequires: libwayland-client-devel waylandpp-devel Xkbcommon
BuildRequires: pkgconfig(wayland-protocols)
%endif
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: lzo-devel
BuildRequires: mariadb-devel
# ARM uses GLES
%ifarch %{arm}
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
%endif
BuildRequires: nasm
BuildRequires: pcre-devel
BuildRequires: pixman-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: python3-devel
BuildRequires: python3-pillow 

BuildRequires: sqlite-devel
BuildRequires: swig
BuildRequires: systemd-devel
BuildRequires: taglib-devel >= 1.8
BuildRequires: tinyxml-devel
BuildRequires: tre-devel
BuildRequires: trousers-devel
BuildRequires: wavpack-devel
%if 0%{?_with_wayland}
BuildRequires: weston-devel
%endif
BuildRequires: yajl-devel
BuildRequires: zlib-devel
# texture packer
BuildRequires: giflib-devel

# new buildrequires
# Why the internal fmt needs a configuration file installed? bug detected!
BuildRequires: fmt-devel 
BuildRequires: rapidjson-devel
BuildRequires: afpfs-ng-devel
BuildRequires: nss-mdns
BuildRequires: alsa-lib-devel
BuildRequires: libidn2-devel
#
BuildRequires: flatbuffers-devel
BuildRequires: fstrcmp-devel
BuildRequires: lcms2-devel
BuildRequires: lirc-devel
BuildRequires: pkgconfig(libupnp)
BuildRequires: rapidjson-devel  
BuildRequires: libdvdcss-devel
BuildRequires: spdlog-devel
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libinput)
BuildRequires: libudfread-devel 
BuildRequires: libdav1d-devel
BuildRequires: gtest-devel doxygen
BuildRequires: ninja-build
# Wayland
BuildRequires: wayland-devel
BuildRequires: waylandpp-devel
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)

Requires: google-roboto-fonts
# need explicit requires for these packages
# as they are dynamically loaded via XBMC's arcane
# pseudo-DLL loading scheme (sigh)
%if 0%{?_with_libbluray}
Requires: libbluray%{?_isa}
%endif
%if 0%{?fedora} >= 24
Requires: libcec%{?_isa} >= 4.0.0
%endif
%if 0%{?_with_crystalhd}
Requires: libcrystalhd%{?_isa}
%endif
Requires: libmad%{?_isa}
Requires: librtmp%{?_isa}
Requires: shairplay-libs%{?_isa}

# needed when doing a minimal install, see
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=1844
Requires: glx-utils
Requires: xorg-x11-utils

# This is just symlinked to, but needed both at build-time
# and for installation
Requires: python3-pillow%{?_isa}
Provides: %{name} = %{epoch}:%{version}-%{release}
Provides: %{name}%{?_isa} = %{version}-%{release}

%description
Kodi is a free cross-platform media-player jukebox and entertainment hub.
Kodi can play a spectrum of of multimedia formats, and featuring playlist,
audio visualizations, slideshow, and weather forecast functions, together
third-party plugins.


%package tools-texturepacker
Summary: Kodi Texturepacker tool
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools-texturepacker
Kodi uses a tool named TexturePacker to compile all images used in a skin into 
a single file. The benefit of it is that images inside the Textures.


%package devel
Summary: Development files needed to compile C programs against kodi
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: xbmc-devel < 14.0
Provides: xbmc-devel = %{version}
Provides: %{name}-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-devel%{?_isa} = %{version}-%{release}
Recommends: %{name}-tools-texturepacker = %{version}-%{release}

%description devel
Kodi is a free cross-platform media-player jukebox and entertainment hub.
If you want to develop programs which use Kodi's libraries, you need to
install this package.


%package eventclients
Summary: Media center event client remotes
Obsoletes: xbmc-eventclients < 14.0
Provides: xbmc-eventclients = %{version}
Provides: %{name}-eventclients = %{epoch}:%{version}-%{release}
Provides: %{name}-eventclients%{?_isa} = %{version}-%{release}

%description eventclients
This package contains support for using Kodi with the PS3 Remote, the Wii
Remote, a J2ME based remote and the command line xbmc-send utility.

%package eventclients-devel
Summary: Media center event client remotes development files
Requires:	%{name}-eventclients%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes: xbmc-eventclients-devel < 14.0
Provides:  xbmc-eventclients-devel = %{version}
Provides: %{name}-eventclients-devel = %{epoch}:%{version}-%{release}
Provides: %{name}-eventclients-devel%{?_isa} = %{version}-%{release}

%description eventclients-devel
This package contains the development header files for the eventclients
library.

%package firewalld
Summary: FirewallD metadata files for Kodi
Requires: firewalld-filesystem

%description firewalld
This package contains FirewallD files for Kodi.

%prep

%autosetup -n xbmc-%{commit0} -p1  

# fmt external fix
%if 0%{?_with_internal_fmt}
echo "internal fmt"
%else
sed -i 's|-DCMAKE_INSTALL_LIBDIR=lib"|-DCMAKE_INSTALL_LIBDIR=%{_lib}|g' cmake/modules/FindFmt.cmake
%endif

# avoid long delays when powerkit isn't running 
	sed -i \
		-e '/dbus_connection_send_with_reply_and_block/s:-1:3000:' \
		xbmc/platform/linux/*.cpp
		
	# Prevent autoreconf rerun
	sed -e 's/autoreconf -vif/echo "autoreconf already done in src_prepare()"/' -i \
		$PWD/tools/depends/native/TexturePacker/src/autogen.sh \
		$PWD/tools/depends/native/JsonSchemaBuilder/src/autogen.sh 

%build
cp -f %{S:5} %{S:6} %{S:7} $PWD/

#export PATH="$PATH:/usr/lib/jvm/java-1.8.0/bin/"
#export JAVA_HOME="/usr/lib/jvm/java-1.8.0/"

cmake -DCMAKE_INSTALL_PREFIX=/usr \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_AR=%{_bindir}/gcc-ar \
       -DCMAKE_RANLIB=%{_bindir}/gcc-ranlib \
       -DCMAKE_NM=%{_bindir}/gcc-nm \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
       -DENABLE_EVENTCLIENTS=ON \
       -DENABLE_INTERNAL_CROSSGUID=ON \
       -DPYTHON_EXECUTABLE=%{__python3} \
%if 0%{?_with_internal_ffmpeg}
       -DENABLE_INTERNAL_FFMPEG=OFF \
%else
       -DFFMPEG_URL=%{S:1} \
       -DENABLE_INTERNAL_FFMPEG=ON \
%endif
       -DVERBOSE=0 \
%if 0%{?_with_internal_fmt}
       -DENABLE_INTERNAL_FMT=ON \
%endif
       -DENABLE_XSLT=ON \
       -DAPP_RENDER_SYSTEM=gl \
       -DENABLE_MDNS=OFF \
       -DENABLE_SNDIO=OFF \
       -DENABLE_INTERNAL_FLATBUFFERS=OFF \
       -Dlibdvdnav_URL=libdvdnav-%{LIBDVDNAV_VERSION}.tar.gz \
       -Dlibdvdread_URL=libdvdread-%{LIBDVDREAD_VERSION}.tar.gz \
       -Dlibdvdcss_URL=libdvdcss-%{LIBDVDCSS_VERSION}.tar.gz \
       %if 0%{?fedora} <= 31
       -DENABLE_INTERNAL_SPDLOG=ON \
       %endif
       -GNinja \
       -Wno-dev .

#       
%ninja_build
echo 'DONE Ninja build'

%install
%ninja_install

# Move man-pages into system dir
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/
mv docs/manpages ${RPM_BUILD_ROOT}%{_mandir}/man1/

# Metainfo
install -Dm 0644 %{S:4} %{buildroot}/%{_metainfodir}/tv.kodi.kodi.metainfo.xml

# Mangling fix

sed -i 's|/bin/sh|/usr/bin/sh|g' %{buildroot}/usr/bin/kodi
sed -i 's|/bin/sh|/usr/bin/sh|g' %{buildroot}/usr/bin/kodi-standalone

sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/bt/__init__.py
sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/bt/bt.py
sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/bt/hid.py
sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/ps3/__init__.py
sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/ps3/keymaps.py
sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/__init__.py
sed -i '1 i\#!/usr/bin/python3'  %{buildroot}/%{python3_sitelib}/kodi/defs.py

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(755, root, root)
%license LICENSES/GPL-2.0-or-later LICENSES/LGPL-2.1-or-later LICENSES/BSD-3-Clause LICENSES/BSD-4-Clause LICENSES/MIT LICENSE.md
%doc docs
%{_bindir}/kodi
%{_bindir}/kodi-standalone
%{_bindir}/JsonSchemaBuilder
%{_libdir}/kodi
%{_datadir}/kodi
%{_datadir}/xsessions/kodi.desktop
%{_datadir}/applications/kodi.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_mandir}/man1/kodi.1.gz
%{_mandir}/man1/kodi.bin.1.gz
%{_mandir}/man1/kodi-standalone.1.gz
%{_mandir}/man1/TexturePacker.1.gz
%{_docdir}/kodi/LICENSE.md
%{_docdir}/kodi/README.Linux.md
%{_docdir}/kodi/version.txt
%{_metainfodir}/*.xml


%files tools-texturepacker
%{_bindir}/TexturePacker


%files devel
%{_includedir}/kodi


%files eventclients
%license LICENSES/GPL-2.0-or-later LICENSES/LGPL-2.1-or-later LICENSES/BSD-3-Clause LICENSES/BSD-4-Clause LICENSES/MIT LICENSE.md
%{python3_sitelib}/kodi
%dir %{_datadir}/pixmaps/kodi
%{_datadir}/pixmaps/kodi/*.png
%{_bindir}/kodi-ps3remote
%{_bindir}/kodi-send
%{_bindir}/kodi-wiiremote
%{_mandir}/man1/kodi-ps3remote.1.gz
%{_mandir}/man1/kodi-send.1.gz
%{_mandir}/man1/kodi-wiiremote.1.gz


%files eventclients-devel
%{_includedir}/kodi/xbmcclient.h
%{_docdir}/kodi/kodi-eventclients-dev/examples/


%files firewalld
%license LICENSES/GPL-2.0-or-later LICENSES/LGPL-2.1-or-later LICENSES/BSD-3-Clause LICENSES/BSD-4-Clause LICENSES/MIT LICENSE.md
%{_firewalldpath}/kodi-eventserver.xml
%{_firewalldpath}/kodi-http.xml
%{_firewalldpath}/kodi-jsonrpc.xml


%changelog

* Wed Feb 02 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.3-8
- Rebuilt for ffmpeg

* Fri Nov 12 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.3-7
- Updated to 19.3

* Fri Oct 22 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.2-7
- Updated to 19.2

* Tue May 11 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.1-7
- Updated to 19.1

* Fri Feb 19 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 19.0-7
- Updated to 19.0

* Sun Oct 25 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.9-7
- Updated to 18.9

* Mon Oct 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.8-9
- Rebuilt

* Mon Oct 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.8-9
- Rebuilt

* Tue Jul 28 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.8-7
- Updated to 18.8

* Tue Jun 23 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.7.1-8
- Rebuilt for ffmpeg

* Sun May 31 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.7.1-7
- Updated to 18.7.1

* Thu May 21 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.7-7
- Updated to 18.7

* Mon May 18 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.6-8
- Added metainfo

* Sat Feb 29 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.6-7
- Updated to 18.6

* Fri Nov 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.5-7
- Updated to 18.5

* Fri Aug 30 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.4-7
- Updated to 18.4

* Tue Jun 25 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.3-7
- Updated to 18.3

* Sat Jun 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.2-5
- Rebuilt for x265

* Mon Jun 10 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.2-4
- Release fix

* Sun Jun 09 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.2-3
- Rebuilt for cwiid

* Mon Apr 22 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.2-2.gitf264356
- Updated to 18.2-2.gitf264356

* Mon Feb 18 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.1-2.git8cfdc89
- Updated to 18.1-2.git8cfdc89

* Fri Feb 15 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-2.gitd81c34c
- Automatic rebuilt

* Wed Feb 06 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-1.gitd81c34c
- Updated to stable

* Mon Dec 10 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.42.git828cdae
- Updated to RC3

* Wed Dec 05 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.41.git812855d 
- Rebuilt for fmt, enabled conditional for compatibility

* Mon Dec 03 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.40.git812855d 
- Updated to RC2

* Tue Nov 13 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.39.gite759ef6  
- Updated to current commit
- Added patch to fix SMB crash

* Tue Nov 06 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.38.git5c29180  
- Updated to RC1

* Fri Oct 12 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.37.gitc2e1b31  
- Updated to current commit

* Tue Sep 04 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.35.git5d7e1db  
- Updated to current commit 18 v2

* Wed Jun 27 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.33.git4c0a23e  
- Updated to current commit Alpha-3

* Thu Apr 26 2018 Unitedrpms Project <unitedrpms AT protonmail DOT com> 18.0-0.31.git6dbb6cf  
- Automatic Mass Rebuild

* Mon Apr 23 2018 David Vásquez <davidva AT tutanota DOT com> - 18.0-0.3.git6dbb6cf
- Updated to current commit
- Compatibility with ffmpeg 4

* Wed Mar 21 2018 David Vásquez <davidva AT tutanota DOT com> - 18.0-0.2.gitbb8b89e
- Updated to 18.0-0.2.gitbb8b89e

* Tue Jan 16 2018 David Vásquez <davidva AT tutanota DOT com> - 17.6-2.git816d15e
- Updated to current commit in Krypton

* Wed Nov 15 2017 David Vásquez <davidva AT tutanota DOT com> - 17.6-1.gita9a7a20
- Updated to 17.6-1.gita9a7a20

* Sat Nov 11 2017 David Vásquez <davidva AT tutanota DOT com> - 17.5-4.git5bd45ab
- libdvd FIX

* Sat Oct 28 2017 David Vásquez <davidva AT tutanota DOT com> - 17.5-3.git5bd45ab
- Changed to internal ffmpeg 3.1 for incompatibility with ffmpeg 3.4

* Sun Oct 22 2017 David Vásquez <davidva AT tutanota DOT com> - 17.5-1.git5bd45ab
- Updated to 17.5-1.git5bd45ab

* Fri Oct 20 2017 David Vásquez <davidva AT tutanota DOT com> - 17.4-4.gite3c608f
- Automatic Mass Rebuild

* Wed Aug 30 2017 David Vásquez <davidva AT tutanota DOT com> - 17.4-3.gite3c608f
- First round with cmake

* Tue Aug 29 2017 David Vásquez <davidva AT tutanota DOT com> - 17.4-2.gite3c608f
- Updated to current commit

* Wed Aug 23 2017 David Vásquez <davidva AT tutanota DOT com> - 17.4-1.git7fc6da0
- Updated to 17.4-1.git7fc6da0

* Thu May 25 2017 David Vásquez <davidva AT tutanota DOT com> - 17.3-1.git147cec4
- Updated to 17.3-1.git147cec4

* Wed May 24 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 17.2-1.git4f53fb5  
- Updated to 17.2-1.git4f53fb5

* Wed Apr 19 2017 Unitedrpms Project <unitedrpms AT protonmail DOT com> 17.1-2.gitfc1619b1 
- Automatic Mass Rebuild

* Fri Mar 24 2017 David Vásquez <davidva AT tutanota DOT com> - 17.1-1.gitfc1619b
- Updated to 17.1-1.gitfc1619b

* Sat Mar 18 2017 David Vásquez <davidva AT tutanota DOT com> - 17.0-4.gita10c504
- Rebuilt for libbluray

* Thu Mar 09 2017 David Vásquez <davidva AT tutanota DOT com> - 17.0-4.gita10c504
- Rebuilt for ffmpeg

* Sun Feb 05 2017 David Vásquez <davidva AT tutanota DOT com> - 17.0-3.gita10c504
- Updated to 17.0-3.gita10c504

* Fri Jan 27 2017 David Vásquez <davidva AT tutanota DOT com> - 17.0rc4-2.gite80803a
- Updated to 17.0rc4-2.gite80803a

* Thu Jan 26 2017 David Vásquez <davidva AT tutanota DOT com> - 17.0rc3-2.git4d93228
- Updated to 17.0rc3-2.git4d93228

* Thu Jan 05 2017 David Vásquez <davidva AT tutanota DOT com> - 17.0rc2-2.git5c40b5c
- Enabled libcec for F24

* Sat Dec 31 2016 David Vásquez <davidva AT tutanota DOT com> - 17.0rc2-1.git5c40b5c
- Updated to 17.0rc2-1.git5c40b5c

* Tue Nov 01 2016 David Vásquez <davidva AT tutanota DOT com> - 17.0b5-1.gite92818a
- Updated to 17.0b5-1.gite92818a

* Tue Sep 27 2016 David Vásquez <davidva AT tutanota DOT com> - 17.0b2-1.gitaa5d1e5
- Updated to 17.0b2-1.gitaa5d1e5

* Thu Aug 25 2016 David Vásquez <davidva AT tutanota DOT com> - 17.0b1-1.git81d5d26
- Updated to beta release 17.0b1-1.git81d5d26

* Wed Aug 03 2016 David Vásquez <davidva AT tutanota DOT com> - 17.0a3-1.gitfc46cf2
- Updated to alpha release 17.0a3-1.gitfc46cf2

* Sat Jul 23 2016 David Vásquez <davidva AT tutanota DOT com> 16.1-5
- Reverting to external ffmpeg, patch thanks to Nathan Grennan

* Wed Jul 20 2016 David Vásquez <davidva AT tutanota DOT com> 16.1-4
- Enabled internal ffmpeg for compatibility

* Fri Jul 08 2016 David Vásquez <davidva AT tutanota DOT com> 16.1-3
- Rebuilt for FFmpeg 3.1

* Sun Jun 26 2016 The UnitedRPMs Project (Key for UnitedRPMs infrastructure) <unitedrpms@protonmail.com> - 16.1-2
- Rebuild with new ffmpeg

* Mon Apr 25 2016 Michael Cronenworth <mike@cchtml.com> - 16.1-1
- Kodi 16.1 final
- Add patch to build with gcc6 
- Add patch to build with ffmpeg3
- Add patch to support xselection pasting

* Sat Feb 20 2016 Michael Cronenworth <mike@cchtml.com> - 16.0-1
- Kodi 16.0 final

* Fri Jan 22 2016 Michael Cronenworth <mike@cchtml.com> - 16.0-0.2
- Kodi 16.0 RC1

* Sun Dec 06 2015 Michael Cronenworth <mike@cchtml.com> - 16.0-0.1
- Kodi 16.0 beta 3
- Drop libhdhomerun support (dropped by Kodi)

* Wed Nov 25 2015 Michael Cronenworth <mike@cchtml.com> - 15.2-3
- Enable AirPlay support (shairplay library)

* Sat Oct 24 2015 Michael Cronenworth <mike@cchtml.com> - 15.2-2
- Enable NFS client support

* Thu Oct 22 2015 Michael Cronenworth <mike@cchtml.com> - 15.2-1
- Kodi 15.2 final

* Sun Aug 16 2015 Michael Cronenworth <mike@cchtml.com> - 15.1-1
- Kodi 15.1 final

* Wed Jul 22 2015 Michael Cronenworth <mike@cchtml.com> - 15.0-1
- Kodi 15.0 final

* Tue Jun 16 2015 Michael Cronenworth <mike@cchtml.com> - 15.0-0.1
- Kodi 15.0 beta 2

* Fri May 22 2015 Michael Cronenworth <mike@cchtml.com> - 14.2-2
- GCC5 fixes

* Sun Mar 29 2015 Michael Cronenworth <mike@cchtml.com> - 14.2-1
- Update to 14.2 final
- Build with SDL2 to enable joystick support

* Fri Jan 30 2015 Michael Cronenworth <mike@cchtml.com> - 14.1-1
- Update to 14.1 final
- Fix Obsoletes for -devel

* Mon Jan 05 2015 Michael Cronenworth <mike@cchtml.com> - 14.0-2
- Fix xbmc upgrade path

* Sun Dec 28 2014 Michael Cronenworth <mike@cchtml.com> - 14.0-1
- Update to 14.0 final

* Tue Dec 09 2014 Michael Cronenworth <mike@cchtml.com> - 14.0-0.4.rc3
- Update to 14.0 RC3

* Sun Nov 09 2014 Michael Cronenworth <mike@cchtml.com> - 14.0-0.3.beta2
- Update to 14.0 beta 2

* Tue Sep 02 2014 Michael Cronenworth <mike@cchtml.com> - 14.0-0.2.alpha3
- Update to 14.0 alpha 3

* Sun Aug 24 2014 Michael Cronenworth <mike@cchtml.com> - 14.0-0.1.alpha2
- Update to 14.0 alpha 2
- Renamed XBMC to Kodi

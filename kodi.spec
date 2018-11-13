# Tips thanks to:
# https://www.archlinux.org/packages/community/x86_64/kodi/
# https://gitweb.gentoo.org/repo/gentoo.git/tree/media-tv/kodi
%global  _firewalldpath   /usr/lib/firewalld/services
%global commit0 e759ef620c108270753348ca409c76d19d2878fd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%global debug_package %{nil}

Name: kodi
Version: 18.0
Release: 0.39%{?gver}%{dist}
Epoch: 1
Summary: Media center

License: GPLv2+ and GPLv3+ and LGPLv2+ and BSD and MIT
# Main binary and all supporting files are GPLv2+/GPLv3+
# Some supporting libraries use the LGPL / BSD / MIT license
Group: Applications/Multimedia
URL: http://www.kodi.tv/
Source0: https://github.com/xbmc/xbmc/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/xbmc/FFmpeg/archive/4.0.3-Leia-Beta5.tar.gz
Source2: kodi-snapshot
Patch: smb_fix.patch

%global _with_libbluray 1
%global _with_cwiid 1
%global _with_libssh 1
%if 0%{?fedora} >= 24
%global _with_libcec 1
%endif
%global _with_external_ffmpeg 0
%global _with_wayland 0


%ifarch x86_64 i686
%global _with_crystalhd 1
%endif

# Upstream does not support ppc64
ExcludeArch: ppc64

BuildRequires: git
BuildRequires: cmake
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
BuildRequires: cwiid-devel
%endif
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: e2fsprogs-devel
BuildRequires: enca-devel
BuildRequires: expat-devel
BuildRequires: faad2-devel
%if 0%{?_with_external_ffmpeg}
BuildRequires: ffmpeg-devel >= 4.0
%endif
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
BuildRequires: java-devel
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
BuildRequires: libvorbis-devel
%if 0%{?_with_wayland}
BuildRequires: libwayland-client-devel
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
BuildRequires: python2-devel
BuildRequires: python2-pillow
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
Requires: python2-pillow%{?_isa}
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

# Our trick; the tarball doesn't download completely the source code; kodi needs some data from .git
# the script makes it for us.

%{S:2} -c %{commit0}

%autosetup -T -D -n kodi-%{shortcommit0} -p1

# Python fix
sed -i 's|PYTHON_LIB_PATH|%{python2_sitelib}|g' cmake/scripts/linux/Install.cmake

# python2 fix
mkdir -p "$HOME/bin/"
ln -sfn /usr/bin/python2.7 $HOME/bin/python
export PATH="$HOME/bin/:$PATH"

%build

# python2 fix
export PATH="$HOME/bin/:$PATH"

# https://bugs.gentoo.org/show_bug.cgi?id=606124
cmake  -DCMAKE_INSTALL_PREFIX=/usr \
       -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
       -DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
       -DCMAKE_RULE_MESSAGES:BOOL=OFF \
       -DENABLE_EVENTCLIENTS=ON \
       -DENABLE_LDGOLD=OFF \
       -DENABLE_ALSA=ON \
       -DENABLE_AIRTUNES=ON \
       -DENABLE_AVAHI=ON \
       -DENABLE_BLUETOOTH=ON \
       -DENABLE_BLURAY=ON \
       -DENABLE_CCACHE=OFF \
       -DENABLE_CEC=ON \
       -DENABLE_DBUS=ON \
       -DENABLE_DVDCSS=ON \
       -DENABLE_INTERNAL_CROSSGUID=OFF \
       -DENABLE_CAP=ON \
       -DENABLE_LIRC=ON \
       -DENABLE_MICROHTTPD=ON \
       -DENABLE_MYSQLCLIENT=ON \
       -DENABLE_NFS=ON \
       -DENABLE_NONFREE=ON \
       -DENABLE_OPENGLES=ON \
       -DENABLE_OPENGL=ON \
       -DENABLE_OPENSSL=ON \
       -DENABLE_OPTICAL=ON \
       -DENABLE_PLIST=ON \
       -DENABLE_PULSEAUDIO=ON \
       -DENABLE_SMBCLIENT=ON \
       -DENABLE_SSH=ON \
       -DENABLE_UDEV=ON \
       -DENABLE_UPNP=ON \
       -DENABLE_VAAPI=ON \
       -DENABLE_VDPAU=ON \
       -DENABLE_X11=ON \
%if 0%{?_with_external_ffmpeg}
       -DWITH_FFMPEG="yes" \
       -DENABLE_INTERNAL_FFMPEG="no" \
%else
       -DFFMPEG_URL=%{S:1} \
       -DENABLE_INTERNAL_FFMPEG="yes" \
%endif
       -DVERBOSE=0 \
       -DENABLE_XSLT=ON .

make %{?_smp_mflags} VERBOSE=0
echo 'DONE MAKE'
 
make preinstall VERBOSE=0
echo 'DONE MAKE PREINSTALL'

%install
make install DESTDIR=%{buildroot} 


# Move man-pages into system dir
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/
mv docs/manpages ${RPM_BUILD_ROOT}%{_mandir}/man1/

# Mangling fix
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/bin/kodi-ps3remote
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/bin/kodi-send
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/share/doc/kodi/kodi-eventclients-dev/examples/python/example_button2.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/share/doc/kodi/kodi-eventclients-dev/examples/python/example_notification.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/share/doc/kodi/kodi-eventclients-dev/examples/python/example_mouse.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/share/doc/kodi/kodi-eventclients-dev/examples/python/example_action.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/share/doc/kodi/kodi-eventclients-dev/examples/python/example_button1.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/usr/share/doc/kodi/kodi-eventclients-dev/examples/python/example_simple.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/ps3/sixpair.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/ps3/sixaxis.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/ps3/sixwatch.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/xbmcclient.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/zeroconf.py
sed -i 's|usr/bin/python|usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/ps3_remote.py
sed -i 's|/usr/bin/env python|/usr/bin/python2|g' %{buildroot}/%{python2_sitelib}/kodi/zeroconf.py

sed -i 's|/bin/sh|/usr/bin/sh|g' %{buildroot}/usr/bin/kodi
sed -i 's|/bin/sh|/usr/bin/sh|g' %{buildroot}/usr/bin/kodi-standalone

sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/bt/__init__.py
sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/bt/bt.py
sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/bt/hid.py
sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/ps3/__init__.py
sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/ps3/keymaps.py
sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/__init__.py
sed -i '1 i\#!/usr/bin/python2'  %{buildroot}/%{python2_sitelib}/kodi/defs.py

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
%{_libdir}/kodi
%{_datadir}/kodi
%{_datadir}/xsessions/kodi.desktop
%{_datadir}/applications/kodi.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_mandir}/man1/kodi.1.gz
%{_mandir}/man1/kodi.bin.1.gz
%{_mandir}/man1/kodi-standalone.1.gz
%{_docdir}/kodi/LICENSE.md
%{_docdir}/kodi/README.Linux.md
%{_docdir}/kodi/version.txt


%files tools-texturepacker
%{_bindir}/TexturePacker


%files devel
%{_includedir}/kodi


%files eventclients
%license LICENSES/GPL-2.0-or-later LICENSES/LGPL-2.1-or-later LICENSES/BSD-3-Clause LICENSES/BSD-4-Clause LICENSES/MIT LICENSE.md
%{python2_sitelib}/kodi
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

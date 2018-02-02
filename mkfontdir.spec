#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkfontdir
Version  : 1.0.7
Release  : 10
URL      : http://ftp.x.org/pub/individual/app/mkfontdir-1.0.7.tar.bz2
Source0  : http://ftp.x.org/pub/individual/app/mkfontdir-1.0.7.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mkfontdir-bin
Requires: mkfontdir-doc
BuildRequires : pkgconfig(xorg-macros)

%description
mkfontdir creates the fonts.dir files needed by the legacy X server
core font system.   The current implementation is a simple wrapper script
around the mkfontscale program, which must be built and installed first.

%package bin
Summary: bin components for the mkfontdir package.
Group: Binaries

%description bin
bin components for the mkfontdir package.


%package doc
Summary: doc components for the mkfontdir package.
Group: Documentation

%description doc
doc components for the mkfontdir package.


%prep
%setup -q -n mkfontdir-1.0.7

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkfontdir

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

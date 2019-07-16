#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-slip
Version  : 0.6.5
Release  : 1
URL      : https://github.com/nphilipp/python-slip/releases/download/python-slip-0.6.5/python-slip-0.6.5.tar.bz2
Source0  : https://github.com/nphilipp/python-slip/releases/download/python-slip-0.6.5/python-slip-0.6.5.tar.bz2
Summary  : Convenience, extension and workaround code for Python 2.x
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: python-slip-license = %{version}-%{release}
Requires: python-slip-python = %{version}-%{release}
Requires: python-slip-python3 = %{version}-%{release}

%description
The Simple Library for Python 2.x packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package license
Summary: license components for the python-slip package.
Group: Default

%description license
license components for the python-slip package.


%package python
Summary: python components for the python-slip package.
Group: Default
Requires: python-slip-python3 = %{version}-%{release}

%description python
python components for the python-slip package.


%package python3
Summary: python3 components for the python-slip package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-slip package.


%prep
%setup -q -n python-slip-0.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563317696
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1563317696
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-slip
cp COPYING %{buildroot}/usr/share/package-licenses/python-slip/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-slip/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

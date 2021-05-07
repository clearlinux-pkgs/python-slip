#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-slip
Version  : 0.6.5
Release  : 13
URL      : https://github.com/nphilipp/python-slip/releases/download/python-slip-0.6.5/python-slip-0.6.5.tar.bz2
Source0  : https://github.com/nphilipp/python-slip/releases/download/python-slip-0.6.5/python-slip-0.6.5.tar.bz2
Summary  : Convenience, extension and workaround code for Python and some Python modules
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: python-slip-license = %{version}-%{release}
Requires: python-slip-python = %{version}-%{release}
Requires: python-slip-python3 = %{version}-%{release}
Requires: decorator
Requires: six
BuildRequires : decorator
BuildRequires : six

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
cd %{_builddir}/python-slip-0.6.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583214861
# -Werror is for werrorists
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
export SOURCE_DATE_EPOCH=1583214861
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-slip
cp %{_builddir}/python-slip-0.6.5/COPYING %{buildroot}/usr/share/package-licenses/python-slip/4a5b0415695c09bc33ed154339a3d50d4ee1275c
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-slip/4a5b0415695c09bc33ed154339a3d50d4ee1275c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

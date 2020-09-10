#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isort
Version  : 5.5.2
Release  : 75
URL      : https://files.pythonhosted.org/packages/49/af/6dc35623937fe93a6bccfd95a7b6fc295b34aca75c0d676a765ddb026dc1/isort-5.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/49/af/6dc35623937fe93a6bccfd95a7b6fc295b34aca75c0d676a765ddb026dc1/isort-5.5.2.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: isort-bin = %{version}-%{release}
Requires: isort-license = %{version}-%{release}
Requires: isort-python = %{version}-%{release}
Requires: isort-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![isort - isort your imports, so you don't have to.](https://raw.githubusercontent.com/pycqa/isort/develop/art/logo_large.png)](https://pycqa.github.io/isort/)

%package bin
Summary: bin components for the isort package.
Group: Binaries
Requires: isort-license = %{version}-%{release}

%description bin
bin components for the isort package.


%package license
Summary: license components for the isort package.
Group: Default

%description license
license components for the isort package.


%package python
Summary: python components for the isort package.
Group: Default
Requires: isort-python3 = %{version}-%{release}

%description python
python components for the isort package.


%package python3
Summary: python3 components for the isort package.
Group: Default
Requires: python3-core
Provides: pypi(isort)

%description python3
python3 components for the isort package.


%prep
%setup -q -n isort-5.5.2
cd %{_builddir}/isort-5.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599762787
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/isort
cp %{_builddir}/isort-5.5.2/LICENSE %{buildroot}/usr/share/package-licenses/isort/00afc6bf25b2c1776f00c130bbf4397210ce7766
cp %{_builddir}/isort-5.5.2/isort/_vendored/toml/LICENSE %{buildroot}/usr/share/package-licenses/isort/5e02fc6e946419e35c2f97512cee7fd1a2fe1952
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
rm -rf %{buildroot}/usr/lib/python3*/site-packages/tests
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isort

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/isort/00afc6bf25b2c1776f00c130bbf4397210ce7766
/usr/share/package-licenses/isort/5e02fc6e946419e35c2f97512cee7fd1a2fe1952

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

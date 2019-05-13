#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isort
Version  : 4.3.19
Release  : 45
URL      : https://files.pythonhosted.org/packages/ed/f7/27e8e8a5c24fcb519f5417c6360ab2da33e7236cc45f3e333b828cc19ac0/isort-4.3.19.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/f7/27e8e8a5c24fcb519f5417c6360ab2da33e7236cc45f3e333b828cc19ac0/isort-4.3.19.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: isort-bin = %{version}-%{release}
Requires: isort-license = %{version}-%{release}
Requires: isort-python = %{version}-%{release}
Requires: isort-python3 = %{version}-%{release}
Requires: appdirs
Requires: futures
Requires: pipreqs
Requires: toml
BuildRequires : appdirs
BuildRequires : buildreq-distutils3
BuildRequires : futures
BuildRequires : pipreqs
BuildRequires : toml

%description
.. image:: https://raw.github.com/timothycrosley/isort/master/logo.png
:alt: isort

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

%description python3
python3 components for the isort package.


%prep
%setup -q -n isort-4.3.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557758016
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/isort
cp LICENSE %{buildroot}/usr/share/package-licenses/isort/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isort

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/isort/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

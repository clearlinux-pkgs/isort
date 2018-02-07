#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isort
Version  : 4.3.3
Release  : 16
URL      : https://pypi.debian.net/isort/isort-4.3.3.tar.gz
Source0  : https://pypi.debian.net/isort/isort-4.3.3.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: isort-bin
Requires: isort-legacypython
Requires: isort-python3
Requires: isort-python
Requires: futures
BuildRequires : futures
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://raw.github.com/timothycrosley/isort/master/logo.png
:alt: isort

%package bin
Summary: bin components for the isort package.
Group: Binaries

%description bin
bin components for the isort package.


%package legacypython
Summary: legacypython components for the isort package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the isort package.


%package python
Summary: python components for the isort package.
Group: Default
Requires: isort-python3

%description python
python components for the isort package.


%package python3
Summary: python3 components for the isort package.
Group: Default
Requires: python3-core

%description python3
python3 components for the isort package.


%prep
%setup -q -n isort-4.3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517924909
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1517924909
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isort

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

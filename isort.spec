#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isort
Version  : 4.2.14
Release  : 5
URL      : https://pypi.debian.net/isort/isort-4.2.14.tar.gz
Source0  : https://pypi.debian.net/isort/isort-4.2.14.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: isort-bin
Requires: isort-python
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


%package python
Summary: python components for the isort package.
Group: Default

%description python
python components for the isort package.


%prep
%setup -q -n isort-4.2.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496839304
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1496839304
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

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*

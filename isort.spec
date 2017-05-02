#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isort
Version  : 4.2.5
Release  : 3
URL      : https://pypi.python.org/packages/70/65/49f66364f4ac551ec414e88537b02be439d1d9ea7e1fdd6d526fb8796bf9/isort-4.2.5.tar.gz
Source0  : https://pypi.python.org/packages/70/65/49f66364f4ac551ec414e88537b02be439d1d9ea7e1fdd6d526fb8796bf9/isort-4.2.5.tar.gz
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
%setup -q -n isort-4.2.5

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488044693
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488044693
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/isort

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*

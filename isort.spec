#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isort
Version  : 4.3.13
Release  : 36
URL      : https://files.pythonhosted.org/packages/fa/d3/7542bd894dc661124b37e046abeda5a4d977bcf4fe218f6be3d1a2a5d156/isort-4.3.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/fa/d3/7542bd894dc661124b37e046abeda5a4d977bcf4fe218f6be3d1a2a5d156/isort-4.3.13.tar.gz
Summary  : A Python utility / library to sort Python imports.
Group    : Development/Tools
License  : MIT
Requires: isort-bin = %{version}-%{release}
Requires: isort-license = %{version}-%{release}
Requires: isort-python = %{version}-%{release}
Requires: isort-python3 = %{version}-%{release}
Requires: appdirs
Requires: futures
Requires: pip
Requires: pipreqs
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : futures

%description
.. image:: https://raw.github.com/timothycrosley/isort/master/logo.png
:alt: isort

%package bin
Summary: bin components for the isort package.
Group: Binaries
Requires: isort-license = %{version}-%{release}

%description bin
bin components for the isort package.


%package legacypython
Summary: legacypython components for the isort package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the isort package.


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
%setup -q -n isort-4.3.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552059627
export LDFLAGS="${LDFLAGS} -fno-lto"
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1552059627
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/isort
cp LICENSE %{buildroot}/usr/share/package-licenses/isort/LICENSE
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/isort/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

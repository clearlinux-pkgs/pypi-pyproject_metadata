#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF893C674816AA95D (lains@archlinux.org)
#
Name     : pypi-pyproject_metadata
Version  : 0.6.1
Release  : 3
URL      : https://files.pythonhosted.org/packages/8e/e3/4314ed332414c059aed340fe2097d5ca065cc8d165c08554c83eb96a59c4/pyproject-metadata-0.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/e3/4314ed332414c059aed340fe2097d5ca065cc8d165c08554c83eb96a59c4/pyproject-metadata-0.6.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/8e/e3/4314ed332414c059aed340fe2097d5ca065cc8d165c08554c83eb96a59c4/pyproject-metadata-0.6.1.tar.gz.asc
Summary  : PEP 621 metadata parsing
Group    : Development/Tools
License  : MIT
Requires: pypi-pyproject_metadata-license = %{version}-%{release}
Requires: pypi-pyproject_metadata-python = %{version}-%{release}
Requires: pypi-pyproject_metadata-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
# pyproject-metadata
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/FFY00/python-pyproject-metadata/main.svg)](https://results.pre-commit.ci/latest/github/FFY00/python-pyproject-metadata/main)
[![checks](https://github.com/FFY00/python-pyproject-metadata/actions/workflows/checks.yml/badge.svg)](https://github.com/FFY00/python-pyproject-metadata/actions/workflows/checks.yml)
[![tests](https://github.com/FFY00/python-pyproject-metadata/actions/workflows/tests.yml/badge.svg)](https://github.com/FFY00/python-pyproject-metadata/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/FFY00/python-pyproject-metadata/branch/main/graph/badge.svg?token=9chBjS1lch)](https://codecov.io/gh/FFY00/python-pyproject-metadata)
[![Documentation Status](https://readthedocs.org/projects/pyproject-metadata/badge/?version=latest)](https://pyproject-metadata.readthedocs.io/en/latest/?badge=latest)

%package license
Summary: license components for the pypi-pyproject_metadata package.
Group: Default

%description license
license components for the pypi-pyproject_metadata package.


%package python
Summary: python components for the pypi-pyproject_metadata package.
Group: Default
Requires: pypi-pyproject_metadata-python3 = %{version}-%{release}

%description python
python components for the pypi-pyproject_metadata package.


%package python3
Summary: python3 components for the pypi-pyproject_metadata package.
Group: Default
Requires: python3-core
Provides: pypi(pyproject_metadata)
Requires: pypi(packaging)

%description python3
python3 components for the pypi-pyproject_metadata package.


%prep
%setup -q -n pyproject-metadata-0.6.1
cd %{_builddir}/pyproject-metadata-0.6.1
pushd ..
cp -a pyproject-metadata-0.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657899664
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyproject_metadata
cp %{_builddir}/pyproject-metadata-0.6.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyproject_metadata/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyproject_metadata/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

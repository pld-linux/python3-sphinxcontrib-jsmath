#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which renders display math in HTML with JavaScript
Summary(pl.UTF-8):	Rozszerzenie Sphinksa tworzące wyświetlanie wzorów matematycznych w HTML przy użyciu JavaScriptu
Name:		python3-sphinxcontrib-jsmath
Version:	2.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-jsmath/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib_jsmath/sphinxcontrib_jsmath-%{version}.tar.gz
# Source0-md5:	af627df8a359609eed7e28e02b38a1a0
URL:		https://pypi.org/project/sphinxcontrib-jsmath/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.7
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
%if %{with tests}
BuildRequires:	python3-Sphinx >= 5
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-jsmath is a Sphinx extension which renders display math
in HTML with JavaScript.

%description -l pl.UTF-8
sphinxcontrib-jsmath to rozszerzenie Sphinksa, tworzące wyświetlanie
wzorów matematycznych w HTML przy użyciu JavaScriptu.

%prep
%setup -q -n sphinxcontrib_jsmath-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENCE.rst README.rst
%{py3_sitescriptdir}/sphinxcontrib/jsmath
%{py3_sitescriptdir}/sphinxcontrib_jsmath-%{version}.dist-info

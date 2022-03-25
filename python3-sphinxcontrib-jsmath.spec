#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which renders display math in HTML with JavaScript
Summary(pl.UTF-8):	Rozszerzenie Sphinksa tworzące wyświetlanie wzorów matematycznych w HTML przy użyciu JavaScriptu
Name:		python3-sphinxcontrib-jsmath
Version:	1.0.1
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-jsmath/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-jsmath/sphinxcontrib-jsmath-%{version}.tar.gz
# Source0-md5:	e45179f0a3608b6766862e0f34c23b62
URL:		https://pypi.org/project/sphinxcontrib-jsmath/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-jsmath is a Sphinx extension which renders display math
in HTML with JavaScript.

%description -l pl.UTF-8
sphinxcontrib-jsmath to rozszerzenie Sphinksa, tworzące wyświetlanie
wzorów matematycznych w HTML przy użyciu JavaScriptu.

%prep
%setup -q -n sphinxcontrib-jsmath-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/jsmath
%{py3_sitescriptdir}/sphinxcontrib_jsmath-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_jsmath-%{version}-py*-nspkg.pth

#
# Conditional build:
%bcond_with	tests	# unit tests [some files are missing in tarball]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Project documentation with Markdown
Summary(pl.UTF-8):	Dokumentacja projektu przy użyciu notacji Markdown
Name:		python-mkdocs
Version:	1.0.4
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mkdocs/
Source0:	https://files.pythonhosted.org/packages/source/m/mkdocs/mkdocs-%{version}.tar.gz
# Source0-md5:	771d52ebb4a79a8ba36fd748da72ae5c
URL:		https://www.mkdocs.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML >= 3.10
BuildRequires:	python-click >= 3.3
BuildRequires:	python-jinja2 >= 2.7.1
BuildRequires:	python-livereload >= 2.5.1
BuildRequires:	python-markdown >= 2.3.1
BuildRequires:	python-mock
BuildRequires:	python-tornado >= 5.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.10
BuildRequires:	python3-click >= 3.3
BuildRequires:	python3-jinja2 >= 2.7.1
BuildRequires:	python3-livereload >= 2.5.1
BuildRequires:	python3-markdown >= 2.3.1
BuildRequires:	python3-tornado >= 5.0
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single
YAML configuration file.

%description -l pl.UTF-8
MkDocs to szybki, prosty i wręcz wspaniały generator statycznych stron
nakierowana na budowanie dokumentacji projektu. Pliki źródłowe
dokumentacji są pisane w notacji Markdown i konfigurowane przy użyciu
pojedynczego pliku konfiguracyjnego YAML.

%package -n python3-mkdocs
Summary:	Project documentation with Markdown
Summary(pl.UTF-8):	Dokumentacja projektu przy użyciu notacji Markdown
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-mkdocs
MkDocs is a fast, simple and downright gorgeous static site generator
that's geared towards building project documentation. Documentation
source files are written in Markdown, and configured with a single
YAML configuration file.

%description -n python3-mkdocs -l pl.UTF-8
MkDocs to szybki, prosty i wręcz wspaniały generator statycznych stron
nakierowana na budowanie dokumentacji projektu. Pliki źródłowe
dokumentacji są pisane w notacji Markdown i konfigurowane przy użyciu
pojedynczego pliku konfiguracyjnego YAML.

%prep
%setup -q -n mkdocs-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/mkdocs{,-3}
%endif

%if %{with python2}
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/mkdocs
%{py_sitescriptdir}/mkdocs
%{py_sitescriptdir}/mkdocs-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mkdocs
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/mkdocs-3
%{py3_sitescriptdir}/mkdocs
%{py3_sitescriptdir}/mkdocs-%{version}-py*.egg-info
%endif

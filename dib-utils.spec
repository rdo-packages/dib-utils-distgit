%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    0.0.11
Release:    1%{?dist}
License:    ASL 2.0
Group:      System Environment/Base
URL:        https://git.openstack.org/cgit/openstack/dib-utils
Source0:    https://tarballs.openstack.org/dib-utils/dib-utils-%{upstream_version}.tar.gz

BuildArch: noarch

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-d2to1
BuildRequires: python-pbr

Conflicts: diskimage-builder < 0.1.15

%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc README.md
%{_bindir}/dib-run-parts
%{python_sitelib}/dib_utils*

%changelog
* Fri Feb 10 2017 Alfredo Moralejo <amoralej@redhat.com> 0.0.11-1
- Update to 0.0.11


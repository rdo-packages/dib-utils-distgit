# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver 3
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

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

BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr

Conflicts: diskimage-builder < 0.1.15

%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}


%files
%doc README.md
%{_bindir}/dib-run-parts
%{pyver_sitelib}/dib_utils*

%changelog
* Thu Aug 16 2018 RDO <dev@lists.rdoproject.org> 0.0.11-1
- Update to 0.0.11


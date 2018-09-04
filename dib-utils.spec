# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pydefault 3
%else
%global pydefault 2
%endif

%global pydefault_bin python%{pydefault}
%global pydefault_sitelib %python%{pydefault}_sitelib
%global pydefault_install %py%{pydefault}_install
%global pydefault_build %py%{pydefault}_build
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    XXX
Release:    XXX
License:    ASL 2.0
Group:      System Environment/Base
URL:        https://git.openstack.org/cgit/openstack/dib-utils
Source0:    https://tarballs.openstack.org/dib-utils/dib-utils-%{upstream_version}.tar.gz

BuildArch: noarch

BuildRequires: python%{pydefault}-devel
BuildRequires: python%{pydefault}-setuptools
BuildRequires: python%{pydefault}-pbr
%if %{pydefault} == 2
BuildRequires: python-d2to1
%else
BuildRequires: python%{pydefault}-d2to1
%endif

Conflicts: diskimage-builder < 0.1.15

%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%{pydefault_build}

%install
%{pydefault_install}


%files
%doc README.md
%{_bindir}/dib-run-parts
%{pydefault_sitelib}/dib_utils*

%changelog

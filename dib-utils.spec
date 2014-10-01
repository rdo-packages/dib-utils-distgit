Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    0.0.7
Release:    1%{?dist}
License:    ASL 2.0
Group:      System Environment/Base
URL:        https://git.openstack.org/cgit/openstack/dib-utils
Source0:    http://tarballs.openstack.org/dib-utils/dib-utils-%{version}.tar.gz

Patch0001: 0001-Update-dib-run-parts.patch

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
%setup -q -n %{name}-%{version}

%patch0001 -p1

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}


%files
%doc README.md
%{_bindir}/dib-run-parts
%{python_sitelib}/dib_utils*

%changelog
* Wed Oct 01 2014 James Slagle <jslagle@redhat.com> 0.0.7-1
- Update to upstream 0.0.7

* Thu Sep 18 2014 James Slagle <jslagle@redhat.com> - 0.0.6-3
- Add patch to update dib-run-parts to fix sourcing of environment.d files

* Wed Sep 17 2014 James Slagle <jslagle@redhat.com> - 0.0.6-2
- Add python BuildRequires

* Wed Sep 17 2014 James Slagle <jslagle@redhat.com> - 0.0.6-1
- Rebase on upstream dib-utils.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Ben Nemec <bnemec@redhat.com> - 0.0.0-1
- Initial package creation

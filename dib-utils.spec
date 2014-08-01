%global dib_release 0.1.15

Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    0.0.0
Release:    2%{?dist}
License:    ASL 2.0
Group:      System Environment/Base
# The long-term direction upstream is to split these files into their own
# source repository, but due to time constraints we are executing the split
# now in the rpm build.
URL:        https://launchpad.net/diskimage-builder
Source0:    http://tarballs.openstack.org/dib-utils/dib-utils-%{dib_release}.tar.gz

BuildArch: noarch

Conflicts: diskimage-builder < 0.1.15

%prep
%setup -q -n dib-utils-%{upstream_version}

# When the upstream repo is available this will be changed to a standard Python install
%install
mkdir -p %{buildroot}%{_bindir}
cp bin/dib-run-parts %{buildroot}%{_bindir}

%description
Dependencies of diskimage-builder that are useful standalone.

%files
%{_bindir}/dib-run-parts

%changelog
* Fri Aug 01 2014 Derek Higgins <derekh@redhat.com> - XXX
- Update to use dib-utils (opposed to taking stuff out of diskimage-builder)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Ben Nemec <bnemec@redhat.com> - 0.0.0-1
- Initial package creation

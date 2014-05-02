%global dib_release 0.1.15

Name:       dib-utils
Summary:    Pieces of diskimage-builder that are useful standalone
Version:    0.0.0
Release:    1%{?dist}
License:    ASL 2.0
Group:      System Environment/Base
# The long-term direction upstream is to split these files into their own
# source repository, but due to time constraints we are executing the split
# now in the rpm build.
URL:        https://launchpad.net/diskimage-builder
Source0:    http://tarballs.openstack.org/diskimage-builder/diskimage-builder-%{dib_release}.tar.gz

BuildArch: noarch

Conflicts: diskimage-builder < 0.1.15

%prep
%setup -q -n diskimage-builder-%{dib_release}

# When the upstream repo is available this will be changed to a standard Python install
%install
mkdir -p %{buildroot}%{_bindir}
cp bin/dib-run-parts %{buildroot}%{_bindir}

%description
Pieces of diskimage-builder that are useful standalone.
This allows them to be used without pulling in all of
diskimage-builder and its dependencies.

%files
%doc LICENSE
%{_bindir}/dib-run-parts

%changelog
* Mon Apr 28 2014 Ben Nemec <bnemec@redhat.com> - 0.0.0-1
- Initial package creation

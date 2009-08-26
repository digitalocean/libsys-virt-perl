# Automatically generated by perl-Sys-Virt.spec.PL

%define perlvendorarch %(perl -e 'use Config; print $Config{installvendorarch}')
%define perlvendorlib %(perl -e 'use Config; print $Config{installvendorlib}')
%define perlvendorprefix %(perl -e 'use Config; print $Config{vendorprefix}')
%define perlvendorman1 %{perlvendorprefix}/share/man/man1
%define perlvendorman3 %{perlvendorprefix}/share/man/man3
%define perlversion %(perl -e 'use Config; print $Config{version}')

%define appname Sys-Virt
%define _extra_release %{?extra_release:%{extra_release}}

Summary: Sys::Virt - Perl API to libvirt library
Name: perl-%{appname}
Version: 0.2.1
Release: 1%{_extra_release}
License: GPLv2 or Artistic
Group: Development/Tools
Source: %{appname}-%{version}.tar.gz
BuildRoot: /var/tmp/%{appname}-%{version}-root
Requires: perl >= %{perlversion}
Requires: libvirt >= 0.6.4
BuildRequires: libvirt-devel >= 0.6.4
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)

%description
Sys::Virt provides an API for using the libvirt library from Perl

%prep
%setup -q -n %{appname}-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=$RPM_BUILD_ROOT/usr
make


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALLVENDORMAN3DIR=$RPM_BUILD_ROOT%{perlvendorman3} INSTALLVENDORMAN1DIR=$RPM_BUILD_ROOT%{perlvendorman1}
find $RPM_BUILD_ROOT -name perllocal.pod -exec rm -f {} \;
find $RPM_BUILD_ROOT -name .packlist -exec rm -f {} \;

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc AUTHORS
%doc LICENSE
%doc README
%doc INSTALL
%doc examples/*.pl
%{perlvendorman3}/*
%{perlvendorarch}/Sys/Virt.pm
%{perlvendorarch}/Sys/Virt/
%{perlvendorarch}/auto/Sys/Virt/

%changelog
* Fri Mar 24 2006  <berrange@redhat.com> - 0.0.1-1
- Initial build

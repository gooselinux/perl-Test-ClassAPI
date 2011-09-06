Name: 		perl-Test-ClassAPI
Version: 	1.06
Release: 	2.1%{?dist}
Summary: 	Provides basic first-pass API testing for large class trees
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/Test-ClassAPI/
Source0: 	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Test-ClassAPI-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: 	noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Config::Tiny) >= 2.00
BuildRequires:  perl(Class::Inspector) >= 1.12
BuildRequires:  perl(File::Spec) >= 0.83

# Explictly required by lib/Test/ClassAPI.pm
BuildRequires:  perl(Params::Util) >= 1.00

# For improved tests
BuildRequires:  perl(Test::Pod)

# For improved tests
BuildRequires: perl(Test::CPAN::Meta) >= 0.12
BuildRequires: perl(Pod::Simple) >= 3.07
BuildRequires: perl(Test::MinimumVersion) >= 0.008


%description
Provides basic first-pass API testing for large class trees.

For many APIs with large numbers of classes, it can be very useful to be 
able to do a quick once-over to make sure that classes, methods, and 
inheritance is correct, before doing more comprehensive testing.
This module aims to provide such a capability.

%prep
%setup -q -n Test-ClassAPI-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test AUTOMATED_TESTING=1

%files
%defattr(-,root,root,-)
%doc Changes LICENSE
%{perl_vendorlib}/Test
%{_mandir}/man3/*

%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.06-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.06-1
- Upstream update.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep 16 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.05-3
- Reflect perl(Test::CPAN::Meta) >= 0.12 finally being available in Fedora.

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.05-2
- Bump release.

* Tue Aug 26 2008 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.05-1
- Upstream update.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-4
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-3
- rebuild for new perl

* Thu Sep 06 2007 Ralf Corsépius <rc040203@freenet.de> - 1.04-2
- Update license tag.

* Mon Mar 12 2007 Ralf Corsépius <rc040203@freenet.de> - 1.04-1
- Upstream update.
- BR: perl(ExtUtils::MakeMaker).

* Fri Feb 16 2007 Ralf Corsépius <rc040203@freenet.de> - 1.03-1
- Upstream update.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.02-4
- Mass rebuild.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 1.02-3
- Rebuild for perl-5.8.8.

* Tue Sep 14 2005 Ralf Corsepius <rc040203@freenet.de> - 1.02-2
- New %%summary.
- Extend %%description.
- Don't put README into %%doc (Redundant to man page).

* Tue Sep 13 2005 Ralf Corsepius <rc040203@freenet.de> - 1.02-1
- Spec file cleanup.
- FE submission.

* Wed Jun 22 2005 Ralf Corsepius <ralf@links2linux.de> - 1.02-0.pm.0
- Initial packman version.

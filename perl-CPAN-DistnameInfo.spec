%define upstream_name    CPAN-DistnameInfo
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Extract distribution name and version from a distribution filename
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Many online services that are centered around CPAN attempt to associate
multiple uploads by extracting a distribution name from the filename of the
upload. For most distributions this is easy as they have used
ExtUtils::MakeMaker or Module::Build to create the distribution, which results
in a uniform name. But sadly not all uploads are created in this way.

CPAN::DistnameInfo uses heuristics that have been learnt by
http://search.cpan.org/ to extract the distribution name and version from
filenames and also report if the version is to be treated as a developer
release.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/CPAN
%{_mandir}/*/*

%changelog
* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1mdv2011.0
+ Revision: 644733
- update to new version 0.12

* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 622678
- update to new version 0.11

* Sun Mar 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 528429
- update to 0.10

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 473714
- update to 0.09

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 403027
- rebuild using %%perl_convert_version

* Thu May 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2010.0
+ Revision: 372882
- update to new version 0.08

* Wed Jul 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.0
+ Revision: 230637
- update to new version 0.07

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.06-1mdv2008.1
+ Revision: 131401
- kill re-definition of %%buildroot on Pixel's request


* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.1
+ Revision: 88557
- Import perl-CPAN-DistnameInfo

* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.1
- first mdv release


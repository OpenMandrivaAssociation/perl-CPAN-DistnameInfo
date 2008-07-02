%define module      CPAN-DistnameInfo
%define name        perl-%{module}
%define version     0.07
%define release     %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Extract distribution name and version from a distribution filename
License:    GPL or Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/CPAN/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CPAN
%{_mandir}/*/*



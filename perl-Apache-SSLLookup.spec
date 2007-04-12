%define module	Apache-SSLLookup
%define name	perl-%{module}
%define version	2.00_04
%define release	1mdk

Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   Hooks for various mod_ssl functions
License:   GPL or Artistic
Group:     Development/Perl
Url:       http://search.cpan.org/dist/%{name}/
Buildrequires:	perl-devel
Buildrequires:	apache-mod_perl-devel
Buildroot: %{_tmppath}/%{name}-%{version}
Source:    http://search.cpan.org/CPAN/authors/id/G/GE/GEOFF/Apache-SSLLookup-2.00_04.tar.gz

%description

Apache::SSLLookup is a glue layer between Perl handlers and the
mod_ssl public API.  under normal circumstances, you would use
subprocess_env() to glean information about mod_ssl.
However, this is only possible after mod_ssl runs its fixups,
that is, Perl handlers can only accurately check the
subprocess_env table for mod_ssl information in the
PerlResponsePhase or later.
This module allows you to query mod_ssl directly via its public
C API at any point in the request cycle.  but without using C,
of course.

%prep
%setup -q -n %{module}-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS"
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} CCFLAGS=-I/usr/include/apr-0
#%{__make} test

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root)
#%doc Changes README
%{perl_vendorarch}/auto/Apache/SSLLookup/*
%{perl_vendorarch}/Apache/*
%{_mandir}/man3/*


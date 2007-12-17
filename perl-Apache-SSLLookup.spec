%define module	Apache-SSLLookup

Summary:	Hooks for various mod_ssl functions
Name:		perl-%{module}
Version:	2.00_04
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GE/GEOFF/Apache-SSLLookup-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	apache-mod_perl-devel
BuildRequires:	apr-devel

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
export CFLAGS="%{optflags}"

%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CCFLAGS="$CCFLAGS `apr-1-config --includes`"

#%{__make} test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root)
#%doc Changes README
%{perl_vendorarch}/auto/Apache/SSLLookup/*
%{perl_vendorarch}/Apache/*
%{_mandir}/man3/*

%define upstream_name	 Apache-SSLLookup
Name:       perl-%{upstream_name}
Version:    2.00_04
Release:	8

Summary:	Hooks for various mod_ssl functions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GE/GEOFF/Apache-SSLLookup-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	apache-mod_perl-devel
BuildRequires:	apr-devel
BuildRequires:	perl-devel

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{version}

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.0_400-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.0_400-4
+ Revision: 680457
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.0_400-3mdv2011.0
+ Revision: 555665
- rebuild

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 2.0_400-1mdv2010.1
+ Revision: 504566
- rebuild using %2.00_04 Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.00_04-6mdv2010.0
+ Revision: 430258
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.00_04-5mdv2009.0
+ Revision: 255286
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 2.00_04-3mdv2008.1
+ Revision: 151820
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 2.00_04-2mdv2008.0
+ Revision: 66861
- misc spec file fixes


* Mon Oct 31 2005 Arnaud Desmons <adesmons@mandriva.org> 2.00_04-1mdk
- Initial specfile


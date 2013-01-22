#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	SpamAssassin
Summary:	Mail::SpamAssassin - Spam detector and markup engine
#Summary(pl.UTF-8):
Name:		perl-Mail-SpamAssassin
Version:	3.3.1
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMASON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a93f81fda315411560ff5da099382d2
URL:		http://search.cpan.org/dist/Mail-SpamAssassin/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-NetAddr-IP
BuildRequires:	perl-Net-DNS >= 0.34
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::SpamAssassin is a module to identify spam using several methods
including text analysis, internet-based realtime blacklists,
statistical analysis, and internet-based hashing algorithms.

Using its rule base, it uses a wide range of heuristic tests on mail
headers and body text to identify "spam", also known as unsolicited
bulk email. Once identified as spam, the mail can then be tagged as
spam for later filtering using the user's own mail user agent
application or at the mail transfer agent.

If you wish to use a command-line filter tool, try the spamassassin or
the spamd/spamc tools provided.

# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor < /dev/null
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes CREDITS INSTALL README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Mail/SpamAssassin.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin
%{perl_vendorlib}/Mail/SpamAssassin/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Bayes
%{perl_vendorlib}/Mail/SpamAssassin/Bayes/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/BayesStore
%{perl_vendorlib}/Mail/SpamAssassin/BayesStore/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Conf
%{perl_vendorlib}/Mail/SpamAssassin/Conf/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Locker
%{perl_vendorlib}/Mail/SpamAssassin/Locker/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Logger
%{perl_vendorlib}/Mail/SpamAssassin/Logger/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Message
%{perl_vendorlib}/Mail/SpamAssassin/Message/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Message/Metadata
%{perl_vendorlib}/Mail/SpamAssassin/Message/Metadata/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Plugin
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/*.pm
%dir %{perl_vendorlib}/Mail/SpamAssassin/Util
%{perl_vendorlib}/Mail/SpamAssassin/Util/*.pm
%dir %{perl_vendorarch}/auto/Mail/SpamAssassin
%{_mandir}/man?/*

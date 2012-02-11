#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Compress
%define	pnam	Raw-Zlib
Summary:	Compress::Raw::Zlib - Low-Level Interface to zlib compression library
Summary(pl.UTF-8):	Compress::Raw::Zlib - niskopoziomowy interfejs do biblioteki kompresji zlib
Name:		perl-Compress-Raw-Zlib
Version:	2.048
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f9d0b38e19bfbd63dea868d9aab37bd3
URL:		http://search.cpan.org/dist/Compress-Raw-Zlib/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	zlib-devel >= 1.2.3
Requires:	perl-dirs >= 1.0-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Compress::Raw::Zlib module provides a Perl interface to the zlib
compression library.

%description -l pl.UTF-8
Moduł Compress::Raw::Zlib udostępnia perlowy interfejs do biblioteki
kompresji zlib.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

cat > config.in <<EOF
BUILD_ZLIB = False
INCLUDE = /usr/include
LIB = %{_libdir}
OLD_ZLIB = False
GZIP_OS_CODE = AUTO_DETECT
EOF

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Compress/Raw/Zlib.pm
%dir %{perl_vendorarch}/auto/Compress/Raw/Zlib
%{perl_vendorarch}/auto/Compress/Raw/Zlib/Zlib.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Raw/Zlib/Zlib.so
%{perl_vendorarch}/auto/Compress/Raw/Zlib/autosplit.ix
%{_mandir}/man3/Compress::Raw::Zlib.3pm*
%{_examplesdir}/%{name}-%{version}

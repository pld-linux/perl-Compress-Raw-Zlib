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
Version:	2.074
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Compress/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a648d15ce8bc65111a37a56b3daa4066
URL:		http://search.cpan.org/dist/Compress-Raw-Zlib/
BuildRequires:	perl-ExtUtils-MakeMaker >= 5.16
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
%attr(755,root,root) %{perl_vendorarch}/auto/Compress/Raw/Zlib/Zlib.so
%{_mandir}/man3/Compress::Raw::Zlib.3pm*
%{_examplesdir}/%{name}-%{version}

Summary:	Afrikaans dictionary for aspell
Summary(pl):	Afrykanerski s³ownik dla aspella
Name:		aspell-af
Version:	0.50
%define	subv	0
Release:	1
License:	LGPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/af/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	bde617a195e70364f96eea71cf71a333
URL:		http://aspell.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afrikaans dictionary (i.e. word list) for aspell.

%description -l pl
Afrykanerski s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*

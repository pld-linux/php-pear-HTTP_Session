%define		_status		beta
%define		_pearname	HTTP_Session
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - Object-oriented interface to the session_* family functions
Summary(pl.UTF-8):	%{_pearname} - Obiektowy interfejs do funkcji z rodziny session_*
Name:		php-pear-%{_pearname}
Version:	0.5.6
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	96a45274b2164f13c3b73e274453787d
URL:		http://pear.php.net/package/HTTP_Session/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.3
Suggests:	php-pear-DB
Suggests:	php-pear-MDB
Suggests:	php-pear-MDB2
Obsoletes:	php-pear-HTTP_Session-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB.*)' 'pear(MDB.*)' 'pear(MDB2.*)'

%description
Object-oriented interface to the session_* family functions; it
provides extra features such as database storage for session data
using DB package. It introduces new methods like isNewSession(),
setCookieless(), abandon(), setExpire(), setIdle(), isExpired(),
isIdled() and others.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet jest obiektowo zorientowanym interfejsem do funkcji z
rodziny session_*. Dostarcza dodatkowe możliwości, takie jak
składowanie danych sesji w bazie danych przy użyciu pakietu DB.
Wprowadza nowe metody, takie jak isNewSession(), setCookieless(),
abandon(), setExpire(), setIdle(), isExpired(), isIdled() i inne.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/HTTP/Session
%dir %{php_pear_dir}/HTTP/Session/Container
%{php_pear_dir}/HTTP/*.php
%{php_pear_dir}/HTTP/Session/*.php
%{php_pear_dir}/HTTP/Session/Container/*.php

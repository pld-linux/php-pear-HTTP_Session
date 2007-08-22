%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Session
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Object-oriented interface to the session_* family functions
Summary(pl.UTF-8):	%{_pearname} - Obiektowy interfejs do funkcji z rodziny session_*
Name:		php-pear-%{_pearname}
Version:	0.5.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	96a45274b2164f13c3b73e274453787d
URL:		http://pear.php.net/package/HTTP_Session/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.3
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Container
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Container/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

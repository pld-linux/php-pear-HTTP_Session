%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	Session
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Object-oriented interface to the session_* family functions
Summary(pl):	%{_pearname} - Obiektowy interfejs do funkcji z rodziny session_*
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c97b39e3f2b8cd76f80ab94650573aaf
URL:		http://pear.php.net/package/HTTP_Session/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object-oriented interface to the session_* family functions; it
provides extra features such as database storage for session data
using DB package. It introduces new methods like isNewSession(),
setCookieless(), abandon(), setExpire(), setIdle(), isExpired(),
isIdled() and others.

In PEAR status of this package is: %{_status}.

%description -l pl
Ten pakiet jest obiektowo zorientowanym interfejsem do funkcji z
rodziny session_*. Dostarcza dodatkowe mo¿liwo¶ci, takie jak
sk³adowanie danych sesji w bazie danych przy u¿yciu pakietu DB.
Wprowadza nowe metody, takie jak isNewSession(), setCookieless(),
abandon(), setExpire(), setIdle(), isExpired(), isIdled() i inne.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Container

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Container/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Container

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Container
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Container/*.php

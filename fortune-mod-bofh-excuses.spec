Summary:	Collection of Bofh Excuses Fortunes
Name:		fortune-mod-bofh-excuses
Version:	1.0
Release:	10
Copyright:	BSD
Group:		Amusements/Games
Source0:	%{name}.tgz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's
your program. Fun-loving system administrators can add fortune to
users' .login files, so that the users get their dose of wisdom 
each time they log in.

Install fortune if you want a program which will bestow these random
bits o' wit.

%prep
install -d %{name}
tar zxf %{SOURCE0} -C %{name}/

%build

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}

install -d		$RPM_BUILD_ROOT%{_datadir}/games/fortunes
install bofh-excuses*	$RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*

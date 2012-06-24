Summary:	Collection of Bofh Excuses Fortunes
Summary(pl):	Zestaw fortunek z wym�wkami administrator�w (BOFH-�w)
Name:		fortune-mod-bofh-excuses
Version:	1.1
Release:	4
License:	BSD
Group:		Applications/Games
BuildRequires:	fortune-mod
Requires:	fortune-mod
Source0:	http://sec.irq.org/sw/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

%description -l pl
Fortune-mod zawiera wci�� popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochot� na odrobin� m�dro�ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog� doda� fortune do plik�w .login u�ytkownik�w tak,
by ka�dy otrzyma� swoj� dawk� m�dro�ci przy logowaniu.

%prep
%setup -q -n bofh

%build
strfile bofh-excuses

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install bofh-excuses* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*

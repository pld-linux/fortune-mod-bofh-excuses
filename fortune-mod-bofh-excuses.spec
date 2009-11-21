Summary:	Collection of Bofh Excuses Fortunes
Summary(pl.UTF-8):	Zestaw fortunek z wymówkami administratorów (BOFH-ów)
Name:		fortune-mod-bofh-excuses
Version:	1.1
Release:	5
License:	BSD
Group:		Applications/Games
Source0:	http://sec.irq.org/sw/%{name}-%{version}.tgz
# Source0-md5:	026b0ccf09187bc03a16140d6c800210
BuildRequires:	fortune-mod
Requires:	fortune-mod
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

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

Summary:	Collection of Bofh Excuses Fortunes
Summary(pl):	Zestaw fortunek z wymÛwkami administratorÛw (BOFH-Ûw)
Name:		fortune-mod-bofh-excuses
Version:	1.1
Release:	2
License:	BSD
Group:		Applications/Games
Group(cs):	Aplikace/Hry
Group(da):	Programmer/Spil
Group(de):	Applikationen/Spiele
Group(es):	Aplicaciones/Juegos
Group(fr):	Applications/Jeux
Group(is):	Forrit/Leikir
Group(it):	Applicazioni/Giochi
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•≤°º•‡
Group(no):	Applikasjoner/Spill
Group(pl):	Aplikacje/Gry
Group(pt):	AplicaÁıes/Jogos
Group(ru):	“…Ãœ÷≈Œ…—/È«“Ÿ
Group(sl):	Programi/Igre
Group(sv):	Till‰mpningar/Spel
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/∂«“…
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
Fortune-mod zawiera wci±ø popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotÍ na odrobinÍ m±dro∂ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaÊ fortune do plikÛw .login uøytkownikÛw tak,
by kaødy otrzyma≥ swoj± dawkÍ m±dro∂ci przy logowaniu.

%prep
%setup -q -n bofh

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install bofh-excuses* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*

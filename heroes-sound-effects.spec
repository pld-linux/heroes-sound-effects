Summary:	Game like Nibbles but different - sound effects
Summary(pl):	Gra w stylu Nibbles, ale inna - efekty d¼wiêkowe
Name:		heroes-sound-effects
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/heroes/%{name}-%{version}.tar.bz2
# Source0-md5:	1c04db6da3d98eebfb3119460701cd5b
URL:		http://heroes.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but
includes many graphical improvements and new game features. In it, you
must maneuver a small vehicle around a world and collect powerups
while avoiding obstacles, your opponents' trails, and even your own
trail. Several modes of play are available, including
"get-all-the-bonuses", deathmatch, and "squish-the-pedestrians".
This package containts sound effects.

%description -l pl
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeñ i nowe w³asno¶ci. W tej grze musisz
manewrowaæ ma³ym pojazdem i zbieraæ dopalacze, unikaj±c przeszkód i
¶ladów przeciwników, a nawet swojego w³asnego ¶ladu. S± dostêpne ró¿ne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjed¼-pieszych".
Pakiet zawiera efekty d¼wiêkowe.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_datadir}/heroes/sfx

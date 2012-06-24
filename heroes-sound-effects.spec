Summary:	Game like Nibbles but different - sound effects
Summary(pl.UTF-8):	Gra w stylu Nibbles, ale inna - efekty dźwiękowe
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

%description -l pl.UTF-8
Heroes jest podobny do starych gier "Tron" i "Nibbles", ale zawiera
wiele graficznych ulepszeń i nowe własności. W tej grze musisz
manewrować małym pojazdem i zbierać dopalacze, unikając przeszkód i
śladów przeciwników, a nawet swojego własnego śladu. Są dostępne różne
tryby gry, w tym "zbierz-wszystkie-premie", deathmatch oraz
"rozjedź-pieszych".
Pakiet zawiera efekty dźwiękowe.

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

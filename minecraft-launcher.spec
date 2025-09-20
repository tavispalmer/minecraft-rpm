Name:           minecraft-launcher
Version:        2.1.3
Release:        1%{?dist}
Summary:        Official Minecraft Launcher

License:        All rights reserved
URL:            https://minecraft.net/
Source0:        https://launcher.mojang.com/download/Minecraft.deb

BuildRequires:  dpkg

%description


%prep
/usr/bin/dpkg-deb -x %{SOURCE0} %{buildroot}


%files
%{_bindir}/minecraft-launcher
%{_datadir}/applications/minecraft-launcher.desktop
%{_datadir}/icons/hicolor/symbolic/apps/minecraft-launcher.svg

Name:           minecraft-launcher
Version:        2.1.3
Release:        1%{?dist}
Summary:        Official Minecraft Launcher

License:        All rights reserved
URL:            https://www.minecraft.net/
Source0:        https://launcher.mojang.com/download/Minecraft.deb

BuildRequires:  dpkg

%description
Official Minecraft Launcher


%prep
/usr/bin/dpkg-deb -x %{SOURCE0} %{buildroot}


%files
%{_bindir}/minecraft-launcher
%{_datadir}/applications/minecraft-launcher.desktop
%{_datadir}/icons/hicolor/symbolic/apps/minecraft-launcher.svg



%changelog
* Sun Jul 27 2025 Tavis Palmer
- 

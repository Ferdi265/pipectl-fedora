Name:           pipectl
Version:        0.5.0
Release:        %autorelease
Summary:        Simple named pipe management utility

License:        GPL-3.0-or-later
URL:            https://github.com/Ferdi265/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# Ferdinand Bachmann <ferdinand.bachmann@yrlf.at> at keys.openpgp.org
Source2:        gpgkey-BC1D9BD570235175.asc

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  pkgconfig(scdoc)

%description
Tool to create and manage short-lived named pipes.

pipectl can be used to e.g. control a longer-lived program using short
commands from elsewhere in the system without needing a complex IPC
mechanism such as UNIX domain sockets.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup


%build
%cmake \
    -DINSTALL_DOCUMENTATION:BOOL=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_bindir}/pipectl
%{_mandir}/man1/pipectl.1*


%changelog
%autochangelog

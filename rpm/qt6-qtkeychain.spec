Name:       qt6-qtkeychain

%global qt_version 6.6.0

Summary:    Qt API for storing passwords securely
Version:    0.14.3
Release:    0
Group:      Applications
License:    BSD-3-Clause
URL:        https://github.com/frankosterfeld/qtkeychain
Source0:    %{name}-%{version}.tar.gz

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel >= %{qt_version}
BuildRequires:  qt6-qtbase-private-devel >= %{qt_version}

%description
%{summary}.

%if "%{?vendor}" == "chum"
PackageName: qt6-qtkeychain
PackagerName: nephros
Custom:
  Repo: https://github.com/frankosterfeld/qtkeychain
  PackagingRepo: https://github.com/sailfishos-chum/qtkeychain
Categories:
 - Library
%endif

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
%cmake_qt6 \
    -DBUILD_WITH_QT6=ON \
    -DBUILD_TEST_APPLICATION=0 \
    -DBUILD_TRANSLATIONS=0 \
    -DLIBSECRET_SUPPORT=0

%cmake_build

%install
rm -rf %{buildroot}
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_qt6_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_qt6_libdir}/*.so
%{_qt6_libdir}/cmake/*
%{_includedir}/qt6keychain/
%{_qt6_archdatadir}/*

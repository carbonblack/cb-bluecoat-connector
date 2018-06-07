%define name python-cb-bluecoat-connector
%define version 1.2
%define unmangled_version 1.2
%define release 9
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Summary: Carbon Black Bluecoat Bridge
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Carbon Black
Url: http://www.carbonblack.com/

%description
UNKNOWN

%prep
%setup -n %{name}-%{unmangled_version}

%build
pyinstaller cb-bluecoat-connector.spec

%install
python setup.py install_cb --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%post
#!/bin/sh

mkdir -p /usr/share/cb/integrations/bluecoat/db
chmod +x /etc/init.d/cb-bluecoat-connector
chkconfig --add cb-bluecoat-connector
chkconfig --level 345 cb-bluecoat-connector on

# not auto-starting because conf needs to be updated
#/etc/init.d/cb-bluecoat-connector start


%preun
#!/bin/sh

/etc/init.d/cb-bluecoat-connector stop

chkconfig --del cb-bluecoat-connector


%files -f INSTALLED_FILES
%defattr(-,root,root)

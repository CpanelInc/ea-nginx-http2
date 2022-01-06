Name:           ea-nginx-http2
Version:        1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4552 for more details
%define release_prefix 1
Release:        %{release_prefix}%{?dist}.cpanel
Summary:        Enable http2 config for ea-nginx
License:        GPL
Group:          System Environment/Libraries
URL:            http://www.cpanel.net
Vendor:         cPanel, Inc.
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       ea-nginx ea-apache24-mod_http2

Source0:        http2.conf

%description
Makes ea-nginx configure http2 support on SSL requests.

%build
echo "Nothing to build"

%install
%{__mkdir_p} %{buildroot}/etc/nginx/conf.d
install %{SOURCE0} %{buildroot}/etc/nginx/conf.d/http2.conf

%clean
rm -rf %{buildroot}

%posttrans
/usr/local/cpanel/scripts/ea-nginx config --all

%files
%defattr(0644,root,root,0755)
%config(noreplace) /etc/nginx/conf.d/http2.conf

%changelog
* Wed Dec 29 2021 Daniel Muey <dan@cpanel.net> - 1.0-1
- ZC-9618: Initial version

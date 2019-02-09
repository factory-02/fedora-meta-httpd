Name:                           meta-httpd
Version:                        1.0.1
Release:                        1%{?dist}
Summary:                        META-package for install and configure HTTPD
License:                        GPLv3

Source10:                       httpd.custom.conf

Requires:                       httpd

%description
META-package for install and configure HTTPD.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/00-httpd.custom.conf

%files
%config %{_sysconfdir}/httpd/conf.d/00-httpd.custom.conf

%changelog
* Sat Feb 09 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1

* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.

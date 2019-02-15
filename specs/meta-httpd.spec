Name:                           meta-httpd
Version:                        1.0.3
Release:                        1%{?dist}
Summary:                        META-package for install and configure HTTPD
License:                        GPLv3

Source10:                       httpd.custom.conf

Requires:                       httpd mod_ssl

%description
META-package for install and configure HTTPD.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
%{__mkdir} -p %{buildroot}%{_sysconfdir}/httpd/conf.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/00-httpd.custom.conf

%files
%config %{_sysconfdir}/httpd/conf.d/00-httpd.custom.conf

%changelog
* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.3-1
- New version: 1.0.3.

* Mon Feb 11 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.2-1
- New version: 1.0.2.

* Sat Feb 09 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.

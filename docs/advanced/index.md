# Advanced topics

## SELinux

For distributions that use SELinux (e.g. CentOS, RHEL, Fedora), the following commands can be used to configure SELinux:

```bash
sudo semanage fcontext -a -t httpd_sys_content_t "/srv/rdmo/rdmo-app(/.*)?"
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/srv/rdmo/rdmo-app/static_root/CACHE(/.*)?"
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/srv/rdmo/rdmo-app/log(/.*)?"
sudo semanage fcontext -a -t httpd_sys_script_exec_t -f f "/srv/rdmo/rdmo-app/env(/.*)?/.+\.so(\.[^/]*)*"
sudo restorecon -R -v /srv/rdmo
sudo setsebool -P httpd_can_network_connect=1
```

While this is the prefereble way, you can also set `selinux` to `permissive` or `disabled` in `/etc/selinux/config` (and reboot afterwards).

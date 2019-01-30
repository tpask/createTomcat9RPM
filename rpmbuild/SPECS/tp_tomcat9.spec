#tomcat spec file
%define version 1.0.0
%define release 1
%define java_jdk java-1.8.0-openjdk-devel
%define tomcat_uri https://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.14/bin/apache-tomcat-9.0.14.tar.gz
%define tarball %(echo %{tomcat_uri} |awk -F "/" '{print $NF}')
%define tomcat_ver %(echo ${tarball} |sed "s/\.tar\.gz//")
%define tomcat_init /home/vagrant/dev/tomcat9/tomcat
%define CATALINA_HOME /opt/tomcat
%define pid_dir %{CATALINA_HOME}/temp
%define tomcat_user tomcat



Name: tp_tomcat9
Packager: Thien P.
Version: %{version}
Release: %{release}
BuildArch: x86_64
Summary: RPM to install java-1.8.0-openjdk-devel and apache-tomcat-9.0.14.tar.gz  
License: GPL
URL: https://www.k9lovers.io
Requires: %{java_jdk}
Provides: wget

%description
This RPM does the following:
- installs java-1.8.0-openjdk-devel and apache-tomcat-9.0.14.tar.gz to /opt/tomcat.
- creates user tomcat
- configures init.d to auto start tomcat using tomcat user after reboot
- once installed you can use service tomcat start to start tomcat or reboot-

%prep
###
# create build tree and copy files to necessary files to it
###

echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp %{tomcat_init} $RPM_BUILD_ROOT/etc/init.d
exit

%pre

#create tomcat user
useradd -m -U -s /bin/false %{tomcat_user}

# download tomcat tarball
cd
wget %{tomcat_uri}
tar -xvzf %{tarball}
if [ -e %{CATALINA_HOME} ]; then mv -f %{CATALINA_HOME} %{CATALINA_HOME}.old ; fi
mv %{tomcat_ver} %{CATALINA_HOME}
chown -Rc %{tomcat_user}:%{tomcat_user} ${CATALINA_HOME}
chmod 755 %{CATALINA_HOME}
chmod u+x %{CATALINA_HOME}/bin/*.sh


%files
%attr(0750, root, root) /etc/init.d/*
%attr(770, %{tomcat_user}, %{tomcat_usr})

%post
chkconfig --add tomcat

%preun 
service tomcat stop


%postun
service tomcat stop
rm -rf %{CATALINA_HOME}
rm -f %{tomcat_init}
userdel %{tomcat_user}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 19 2019 Thien P. <thien@k9lovers.io>
  - Original package


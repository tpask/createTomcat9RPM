Name: tp_tomcat9
Packager: Thien P.
Version: 1.0.0
Release: 1
BuildArch: x86_64
Summary: RPM to install java-1.8.0-openjdk-devel and apache-tomcat-9.0.14.tar.gz  
License: GPL
URL: https://www.k9lovers.io
Requires: java-1.8.0-openjdk-devel
Requires: wget

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
#**** must define path to tomcat ***
tomcat_init_file="/home/centos/rpmbuild/dev/tomcat9/tomcat"
#****

echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cp $tomcat_init_file $RPM_BUILD_ROOT/etc/init.d
exit

%pre
#define all my vars
CATALINA_HOME="/opt/tomcat"
pidDir="$CATALINA_HOME/temp"
tomcatUri="https://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.14/bin/apache-tomcat-9.0.14.tar.gz"
tarBall=`echo $tomcatUri |awk -F "/" '{print $NF}'`
tomcatVer=$(echo $tarBall |sed "s/\.tar\.gz//")

#create tomcat user
useradd -m -U -s /bin/false tomcat

# download tomcat tarball
cd
wget $tomcatUri
tar -xvzf $tarBall
if [ -e $CATALINA_HOME ]; then mv -f $CATALINA_HOME $CATALINA_HOME.old ; fi
mv $tomcatVer $CATALINA_HOME
chown -R tomcat:tomcat $CATALINA_HOME
chmod 755 $CATALINA_HOME
chmod u+x $CATALINA_HOME/bin/*.sh
if [ ! -d $pidDir ]; then mkdir -p $pidDir ; fi
chmod 777 $pidDir

%files
%attr(0750, root, root) /etc/init.d/*

%post
chkconfig --add tomcat

%postun
service tomcat stop
rm -rf /opt/tomcat
rm -f /etc/init.d/tomcat
userdel tomcat

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 19 2019 Thien P. <thien@k9lovers.io>
  - Original package


# removes tomcat manualy
: <<'END'
service tomcat stop
rm -rf /opt/*
rm -f /etc/init.d/tomcat
userdel tomcat
END

#remove tomcat rpm created by sample script
sudo yum erase -y tp_tomcat9-1.0.0-1.x86_64
sudo yum erase -y java_jdk java-1.8.0-openjdk-devel
 

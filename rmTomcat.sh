# removes tomcat manualy
: <<'END'
service tomcat stop
rm -rf /opt/*
rm -f /etc/init.d/tomcat
userdel tomcat
END

#remove tomcat rpm created by sample script
#sudo yum erase tp_tomcat9-1.0.0-1.x86_64


#!/bin/bash
#
# tomcatd       Start Tomcat server
# chkconfig: 345 99 10
# description: Tomcat Web Application Server
#
# processname: tomcat

### BEGIN INIT INFO
# Provides: tomcat
# Required-Start: $network $syslog
# Required-Stop: $network $syslog
# Default-Start:
# Default-Stop:
# Short-Description: Start tomcat server
### END INIT INFO

# Source function library.
. /etc/rc.d/init.d/functions

prog=tomcat
RETVAL=$?
lockfile=/var/lock/subsys/$prog

# Tomcat init Variables
# for additional tomcat config please use setenv

#CATALINA_HOME is the location of the bin files of Tomcat
export CATALINA_HOME="/opt/tomcat"
#TOMCAT_USER is the default user of tomcat
TOMCAT_USER=tomcat
#SHUTDOWN_VERBOSE Whether to annoy the user with "attempting to shut down" messages or not
SHUTDOWN_VERBOSE="false"
#SHUTDOWN_WAIT Time to wait in seconds, before killing process
SHUTDOWN_WAIT="20"

# Start of the script
start() {
    echo -n $"Starting $prog: "
    daemon --user $TOMCAT_USER "$CATALINA_HOME/bin/catalina.sh" start
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch $lockfile
    return $RETVAL
}

stop() {
    echo -n $"Shutting down $prog: "
    daemon --user $TOMCAT_USER "$CATALINA_HOME/bin/catalina.sh" stop
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f $lockfile
    return $RETVAL
}

rhstatus(){
    status -p "$CATALINA_PID" $prog
}

case $1 in
    start)
        start
    ;;
    stop)
        stop
    ;;
    restart)
        stop
        start
    ;;
    status)
        rhstatus
    ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
    ;;
esac
exit 0

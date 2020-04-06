FROM ubuntu:16.04

COPY tomcat9024 /tomcat
RUN useradd tomcat
RUN chmod -R +x /tomcat/bin/*.sh
RUN chown -R tomcat:tomcat /tomcat/logs/
RUN chown -R tomcat:tomcat /tomcat/work/
RUN chown -R tomcat:tomcat /tomcat/temp/

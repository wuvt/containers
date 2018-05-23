FROM docker.elastic.co/logstash/logstash-oss:6.2.4
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/ /usr/share/logstash/pipeline/
ADD patterns/ /usr/share/logstash/patterns/
ADD templates/ /usr/share/logstash/templates/
#ADD config/ /usr/share/logstash/config/

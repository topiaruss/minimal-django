FROM jwilder/nginx-proxy

COPY certs /etc/nginx/certs/
COPY vhost.d /etc/nginx/vhost.d/

RUN { \
      echo 'proxy_headers_hash_max_size 1024;'; \
      echo 'proxy_headers_hash_bucket_size 128;'; \
    } > /etc/nginx/conf.d/e_prevent_hash_overflow.conf

RUN { \
      echo 'server_tokens off;'; \
      echo 'client_max_body_size 100m;'; \
    } > /etc/nginx/conf.d/f_enable_large_images.conf

RUN { \
      echo 'error_log  /var/log/nginx/error.log  debug;'; \
    } > /etc/nginx/conf.d/g_error_log.conf

#RUN { \
#      echo 'proxy_read_timeout 3000s;'; \
#    } > /etc/nginx/conf.d/h_set_long_timeout_for_debug.conf

#RUN { \
#      echo 'proxy_pass_header  Set-Cookie;'; \
#    } > /etc/nginx/conf.d/i_set_other_headers.conf

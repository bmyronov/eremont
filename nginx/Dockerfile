FROM nginx:latest

# remove default config
RUN rm /etc/nginx/conf.d/default.conf

# copy custom configs
COPY nginx.conf /etc/nginx/conf.d/
COPY proxy_params /etc/nginx
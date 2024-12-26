FROM nginx:alpine

# Copy any default config or custom configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY sites/*.conf /etc/nginx/conf.d/

# Expose ports if needed (not strictly needed with docker-compose)
EXPOSE 80
EXPOSE 443

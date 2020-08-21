# => Node container
FROM node:alpine as builder
WORKDIR /app
COPY ../../probo-dashboard/package.json .
COPY ../../probo-dashboard/package-lock.json .
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY ../../probo-dashboard/ .
RUN npm run build


# => Run container
FROM nginx:1.15.2-alpine

# Nginx config
RUN rm -rf /etc/nginx/conf.d/*
COPY default.conf /etc/nginx/conf.d/
COPY gzip.conf /etc/nginx/conf.d/

# Static build
COPY --from=builder /app/build /usr/share/nginx/html/

# Default port exposure
EXPOSE 80

# Initialize environment variables into filesystem
WORKDIR /usr/share/nginx/html
COPY ../script/setenv.sh .
COPY ../assets/.env .

# Add bash
RUN apk add --no-cache bash

# Run script which initializes env vars to fs
RUN chmod +x env.sh
# RUN ./env.sh

# Start Nginx server
CMD ["/bin/bash", "-c", "/usr/share/nginx/html/setenv.sh && nginx -g \"daemon off;\""]

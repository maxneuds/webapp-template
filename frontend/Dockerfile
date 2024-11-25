# Stage 1: Build Angular application
FROM node:22-bookworm AS builder

WORKDIR /app
COPY . /app
RUN npm install
RUN npm run build --prod

# Stage 2: Serve the application
FROM nginx:alpine-slim

# Copy built Angular files from the builder stage
COPY --from=builder /app/dist/browser /usr/share/nginx/html
COPY --from=builder /app/nginx.conf /etc/nginx/conf.d/default.conf


# Start the NGINX server
EXPOSE 80
# ENTRYPOINT ["sh"]
ENTRYPOINT ["nginx", "-g", "daemon off;"]


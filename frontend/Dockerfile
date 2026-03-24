# =========================================
# Build Vue (Node.js)
# =========================================
FROM node:20-alpine AS builder

WORKDIR /app

# Копируем package.json (Docker кэширует!)
COPY package*.json ./
RUN npm ci  #Полная установка (dev+prod)

# Копируем код + билд
COPY . .
RUN npm run build

# =========================================
#  Nginx Production
# =========================================
FROM nginx:alpine

# Копируем Vue статику
COPY --from=builder /app/dist /usr/share/nginx/html

# ORS + SPA config
COPY nginx.conf /etc/nginx/conf.d/default.conf



# Порт 80 (nginx default)
EXPOSE 80

# Запуск nginx
CMD ["nginx", "-g", "daemon off;"]

FROM node AS builder

WORKDIR /app

COPY . .

# installing the dependencies of the react app inside the container.
RUN npm i

# creating the dist folder inside the container and copying the contents of the dist folder from the host to the container.
RUN npm run build

# add nginx for running the react app in production mode.
FROM nginx

COPY --from=builder /app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
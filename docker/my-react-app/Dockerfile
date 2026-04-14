FROM node:22

WORKDIR /app

COPY . .

RUN npm i

EXPOSE 5173

ENTRYPOINT ["npm", "run", "dev"]
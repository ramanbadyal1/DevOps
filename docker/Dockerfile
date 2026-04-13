# Base Image
FROM node

# need to select a directory for the project to keep the code in
WORKDIR /app

# need to copy the source code into the working directory
COPY . .

# installing dependencies
RUN npm i

# telling system which port is exposed for this app. It does not publish the port though.
EXPOSE 3000

# cmd commands to start the project
CMD ["npm", "start"]
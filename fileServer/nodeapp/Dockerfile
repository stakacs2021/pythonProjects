# 1) Use an official Node.js runtime as a parent image
FROM node:14-alpine

# 2) Set the working directory
WORKDIR /app

# 3) Copy package.json and package-lock.json
COPY package*.json ./

# 4) Install dependencies
RUN npm install

# 5) Copy the rest of the application files
COPY . .

# 6) Create the uploads folder
RUN mkdir -p uploads

# 7) Expose the server port
ENV PORT=8080

# 8) Run the application
CMD ["node", "server.js"]

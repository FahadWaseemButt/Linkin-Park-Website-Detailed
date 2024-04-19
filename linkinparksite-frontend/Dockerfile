# Use the official Node.js image as base
FROM node:16-alpine as build

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the remaining application code to the working directory
COPY . .

# Build the React app
RUN npm run build

# Use Nginx as a lightweight web server to serve the static files
FROM nginx:alpine

# Copy the built React app from the previous stage to the Nginx server directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Command to run the Nginx server
CMD ["nginx", "-g", "daemon off;"]
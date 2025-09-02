# Use an official node runtime as a parent image
FROM node:16.14.2

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install any needed packages
RUN npm install

# Copy the current directory contents into the container
COPY . .

# Build the app
RUN npm run build

# Install serve to serve the application
RUN npm install -g serve

# Make port 3000 available to the world outside this container
EXPOSE 3000

# Serve the application
CMD ["serve", "-s", "dist"]

FROM node:18-alpine

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

# We use dev mode to allow runtime environment variables from docker-compose
# to be picked up by Next.js, as 'build' bakes them in at build time.
CMD ["npm", "run", "dev"]

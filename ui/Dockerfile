

FROM --platform=linux/amd64 node:18-alpine
WORKDIR /bankapp
EXPOSE 3000
COPY package.json package-lock.json ./
RUN npm install --silent
COPY . ./
CMD ["npm", "run", "ui"]
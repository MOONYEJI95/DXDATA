FROM node:alpine

# 경로 설정
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install --force
RUN npm install react-scripts@5.0.1 -g
EXPOSE 3000
CMD ["npm", "start"]


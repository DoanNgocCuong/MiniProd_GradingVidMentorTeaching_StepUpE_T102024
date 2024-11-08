# Build stage for ViewScoringResults
FROM node:18-alpine AS build-scoring
WORKDIR /app/scoring
COPY ViewScoringResults/package*.json ./
RUN npm install
COPY ViewScoringResults/ .
RUN npm run build

# Build stage for ViewVideoScoringGrading
FROM node:18-alpine AS build-grading
WORKDIR /app/grading
COPY ViewVideoScoringGrading/package*.json ./
RUN npm install
COPY ViewVideoScoringGrading/ .
RUN npm run build

# Final stage with Nginx
FROM nginx:stable-alpine
COPY --from=build-scoring /app/scoring/build /usr/share/nginx/html/scoring
COPY --from=build-grading /app/grading/build /usr/share/nginx/html/grading
COPY shared/layout.html /usr/share/nginx/html/shared/
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"] 
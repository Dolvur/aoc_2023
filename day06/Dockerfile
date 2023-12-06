FROM python:3.9-alpine
WORKDIR /app
COPY . .
ENV part=1
CMD ["sh", "-c", "python3 main_${part}.py"]

FROM alpine:late
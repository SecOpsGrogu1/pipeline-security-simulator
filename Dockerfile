# Secure Dockerfile for passing pipeline (same as Dockerfile.secure)
FROM alpine:3.18
RUN apk add --no-cache openssl
CMD ["openssl", "version"]

FROM n8nio/n8n:latest

USER root

# Install Python3 and PIP
RUN apk add --no-cache python3 py3-pip

# Install requests library
RUN pip install requests

USER node

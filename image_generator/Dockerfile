# Extend from the ollama/ollama base image
FROM python:3.11

# Update the package list and install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app; cd app
WORKDIR /app/
COPY requirements-in.txt ./requirements-in.txt

# Install pip tools and build requirements
RUN pip3 install pip-tools
RUN pip-compile requirements-in.txt -o requirements.txt;
RUN pip3 install -r requirements.txt
# Set the working directory (optional)
EXPOSE 5000

CMD [ "python3", "server/server.py" ]
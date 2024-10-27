

# Node v18.16.1 has npm v9.6.5 (should match the version in package.json `engines` field!)
ARG NODE_VERSION='18.17.1'
# Cypress factory image uses this arg so you can control the base image
ARG BASE_IMAGE='node:18.17.1'

# Enable Cypress factory image when you are ready to do e2e testing
# FROM cypress/factory
FROM ${BASE_IMAGE}

ARG SERVICE_DIR=.
ENV NODE_ENV development

RUN mkdir /app
WORKDIR /app
#RUN npm install --loglevel warn --no-audit
RUN mkdir -p .vite

ENV DEV_PORT 5000
ENV DEV_BINDADDR 0.0.0.0
EXPOSE 5000

#ENTRYPOINT [ "/usr/bin/bash" ]
#CMD ["npm", "run dev"]
#CMD ["sleep", "infinity"]
#CMD npm install; npm run start
CMD npm run dev
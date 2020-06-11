FROM python:3-alpine

ARG VERSION=unknown
ARG GITCOMMIT=unknown
ARG BRANCH=unknown
ARG TAG=unknown

ENV VERSION ${VERSION}
ENV BRANCH ${BRANCH}
ENV GITCOMMIT ${GITCOMMIT}
ENV TAG ${TAG}

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -qr requirements.txt
COPY server.py .

ENTRYPOINT ["python3", "./server.py"]
#CMD ["${VERSION}", "${GITCOMMIT}", $VERSION]
CMD ["${VERSION}", "${BRANCH}", "${GITCOMMIT}"]

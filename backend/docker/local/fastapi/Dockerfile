ARG PYTHON_VERSION=3.13.1

FROM python:${PYTHON_VERSION}-slim-bookworm AS python

# Stage 1: build dependency wheels
FROM python AS python-build-stage 

RUN apt-get update && apt-get install \ 
 --no-install-recommends -y \ 
 build-essential \ 
 libpq-dev\
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Install uv
RUN pip install --no-cache-dir uv
# Copy uv files
COPY ./pyproject.toml ./uv.lock ./

# RUN uv pip compile pyproject.toml --locked --generate-hashes -o requirements.txt
RUN uv pip compile pyproject.toml --generate-hashes --output-file requirements.txt

# RUN  pip wheel \
#  --wheel-dir /usr/src/app/wheels \
#  -r requirements.txt \
#  --no-cache-dir
RUN pip wheel \
  --wheel-dir /usr/src/wheels \
  -r requirements.txt \
  --no-cache-dir

# stage 2 run time stage

FROM python AS python_runtime_build

ARG APP_HOME=/src

ARG APP_USER=fastapi

ARG  APP_GROUP=fastapi

ENV PYTHONDONTWRITEBYTECODE=1 \ 
  PYTHONUNBUFFERED=1


WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install \ 
 --no-install-recommends -y \
 libpq-dev \ 
 sudo git  bash-completion gettext ssh nano \ 
 && apt-get purge -y --auto-remove -o APT::AutoRemoveRecommendsImportant=false \
 && rm -rf /var/lib/apt/lists/* 

RUN groupadd -r ${APP_GROUP} && \ 
 useradd  -r -g ${APP_GROUP} -d ${APP_HOME} -m ${APP_USER}

RUN mkdir -p ${APP_HOME}/backend/app/logs && \ 
 chown -R ${APP_USER}:${APP_GROUP} ${APP_HOME}/backend/app/logs && \
 chmod 775 ${APP_HOME}/backend/app/logs


#install the wheels
# COPY --from=python-build-stage /usr/src/wheels wheels/
COPY --from=python-build-stage /usr/src/wheels /wheels/

# RUN pip install --no-cache-dir --no-index --find-links=/wheels/* \
#  && rm -rf /wheels/
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
 && rm -rf /wheels/

COPY --chown=${APP_USER}:${APP_GROUP} ./backend/docker/local/fastapi/entrypoint.sh /entrypoint.sh
COPY --chown=${APP_USER}:${APP_GROUP} ./backend/docker/local/fastapi/start.sh /start.sh

#sed -> stream editor
# -i change the file itself (inside)   s/ -> substitute    \r -> carragie return that is in windows shells after ending of each line      $-> end of each line    g
RUN sed -i 's/\r$//g' /entrypoint.sh /start.sh  && \
  chmod +x /entrypoint.sh /start.sh 

USER ${APP_USER}

ENTRYPOINT [ "/entrypoint.sh" ]

FROM registry.gitlab.com/phec.net/oci/platformbase:base

USER root

RUN rm -r /home/jovyan/*

COPY . /home/jovyan/

RUN chown -R ${NB_USER}:${NB_USER} /home/jovyan/

USER ${NB_USER}

# Opération si nécessaires : PIP install, R install

CMD jupyter notebook --ip 0.0.0.0

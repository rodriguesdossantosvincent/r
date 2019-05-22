FROM registry.gitlab.com/phec.net/oci/platformbase:base

USER root

RUN rm -r ${HOME}/*

COPY . ${HOME}

RUN chown -R ${NB_USER}:${NB_USER} ${HOME}

USER ${NB_USER}

CMD jupyter notebook --ip 0.0.0.0
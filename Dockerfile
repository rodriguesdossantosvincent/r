FROM registry.gitlab.com/phec.net/oci/platformbase:base

USER root

RUN rm -r ${HOME}/*

COPY . ${HOME}

RUN chown -R ${NB_USER}:${NB_USER} ${HOME}

USER ${NB_USER}

RUN pip install "pip<19" && \
    ${KERNEL_PYTHON_PREFIX}/bin/pip install --no-cache-dir -r "requirements.txt"

RUN Rscript install.R

# Rscript puis ? postBuild ? quel user à la fin ?
#LABEL repo2docker.version "0.8.0+0.gb6c4e7e.dirty"
#LABEL repo2docker.repo "https://github.com/rodriguesdossantosvincent/r"
#LABEL repo2docker.ref "59eebf5eee93eda4b75b4ec9735046291f2a24bc"

RUN chmod +x postBuild

RUN ./postBuild

CMD jupyter notebook --ip 0.0.0.0
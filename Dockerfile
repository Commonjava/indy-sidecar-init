FROM registry.access.redhat.com/ubi8/python-36

RUN mkdir -p /usr/share/indy-sidedcar-init/sidecar-init

ADD sidecarinit /usr/share/indy-sidedcar-init/sidecar-init
ADD setup.py /usr/share/indy-sidedcar-init
ADD scripts/* /usr/local/bin/

RUN chmod +x /usr/local/bin/*

RUN virtualenv --python=$(which python3) /usr/share/indy-sidedcar-init/venv && \
	/usr/share/indy-sidedcar-init/venv/bin/pip install --upgrade pip && \
	/usr/share/indy-sidedcar-init/venv/bin/pip install -e /usr/share/indy-sidedcar-init

USER 1001
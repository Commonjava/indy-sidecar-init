FROM registry.access.redhat.com/ubi8/python-36

USER root

RUN mkdir -p /usr/share/indy-sidecar-init/sidecarinit

ADD sidecarinit /usr/share/indy-sidecar-init/sidecarinit
ADD setup.py /usr/share/indy-sidecar-init
ADD scripts/* /usr/local/bin/
ADD application.yaml /deployments/config/application.yaml

ADD cert/RH-IT-Root-CA.crt /etc/pki/ca-trust/source/anchors/RH-IT-Root-CA.crt
ADD cert/2022-IT-Root-CA.pem /etc/pki/ca-trust/source/anchors/2022-IT-Root-CA.pem
RUN update-ca-trust extract

RUN chmod +x /usr/local/bin/*

RUN virtualenv --python=$(which python3) /usr/share/indy-sidecar-init/venv && \
	/usr/share/indy-sidecar-init/venv/bin/pip install --upgrade pip && \
	/usr/share/indy-sidecar-init/venv/bin/pip install -e /usr/share/indy-sidecar-init

USER 1001

CMD ["sidecar-init"]
# Indy sidecar init
**Deployment**

The sidecar init container is meant to be init-container part of builder and sidecar pod, provides sidecar with initial repos downloaded from archive service.

1. Make sure you have right application.yaml from [indy-sidecar](https://github.com/commonjava/indy-sidecar) container, you must set `sidecar.archive-api` and `sidecar.local-repository` for this to work.

2. mount the same application.yaml across this sidecar-init container as well as the sidecar container.

3. Add init-container part to the pod deploymentconfig and mount preSeedRepo volume as the sidecar does (or whatever defined it in application.yaml config file)

Template of the deployment can be found in template/template-sidecar.yaml

---

**Build container image**

Use Dockerfile or BuildConfig.yaml(for Openshift) to build the container
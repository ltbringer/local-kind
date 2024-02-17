# Setup

We need a working Docker installation, I am using [Docker Desktop](https://www.docker.com/products/docker-desktop/) on WSL 2.
Apart from Docker, we have every other installation included (for Ubuntu-22.04). The sources are included which should make things
easy for other platforms. (MacOS ARM processors might prove more challenging.)
_Scripts may need `sudo`._


## Pre Cluster
These dependencies are required before we create a cluster.
1. Install `kind`.
    ```bash
    bash setup/kind.sh
    ```

## Post Cluster

Once a cluster is created, we'd need `helm` to install applications and `cilium` is needed for
[eBPF](https://cilium.io/get-started/) based networking.
> At the foundation of Cilium is a new Linux kernel technology called eBPF, which enables the dynamic insertion of powerful security, visibility, and networking control logic into the Linux kernel. eBPF is used to provide high-performance networking, multi-cluster and multi-cloud capabilities, advanced load balancing, transparent encryption, extensive network security capabilities, transparent observability, and much more.

1. Install `helm`.
    ```bash
    bash setup/helm.sh
    ```

2. Install `cilium`
    Say your cluster/config.yaml has:
    ```yaml
    name: main
    ```
    then the installation needs `"main"` as an argument. Otherwise `"kind"` would be the assumed name.
    ```bash
    bash setup/cilium.sh main
    ```

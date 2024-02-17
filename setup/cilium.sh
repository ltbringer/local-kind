#!/bin/bash
CLUSTER_NAME=${1:-"kind"}

helm repo add cilium https://helm.cilium.io/
docker pull quay.io/cilium/cilium:v1.15.1
kind --name $CLUSTER_NAME load docker-image quay.io/cilium/cilium:v1.15.1
helm install cilium cilium/cilium --version 1.15.1 \
   --namespace kube-system \
   --set image.pullPolicy=IfNotPresent \
   --set ipam.mode=kubernetes

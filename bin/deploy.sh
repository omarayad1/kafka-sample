#!/bin/bash

set -ex

eval $(minikube docker-env)

# builds images
for dir in ./apps/*/
do
    (cd $dir && ./bin/build.sh)
done

# deploys terraform infra
(cd infra && ./bin/deploy.sh)

echo "done!"

#! /usr/bin/env bash
set -eu
HOST_MOUNT_VOLUME_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
docker run \
    --rm \
    -v "${HOST_MOUNT_VOLUME_PATH}/protos:/protos" \
    qarlm/protoc:latest \
    --working-dir /protos \
    --language python \
    --grpc

cp protos/*.py server
cp protos/*.py client
rm -rf protos/*.py

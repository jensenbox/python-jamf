#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o verbose

VERSION=v10.25.0

docker run \
        --rm \
        -v ${PWD}:/local openapitools/openapi-generator-cli generate \
        -i https://resources.jamf.com/open-api/${VERSION}_JPAPI.json \
        -g python \
        -o /local \
        --additional-properties=packageName=jamf \
        --additional-properties=packageVersion=${VERSION} \
        --additional-properties=projectName=python-jamf
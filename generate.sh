#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail
set -o verbose

docker run \
        --rm \
        -v ${PWD}:/local openapitools/openapi-generator-cli generate \
        -i https://resources.jamf.com/open-api/v10.25.0_JPAPI.json \
        -g python \
        -o /local
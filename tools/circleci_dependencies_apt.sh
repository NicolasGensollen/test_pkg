#!/bin/bash -ef

sudo -E apt-get -yq update
sudo -E apt-get -yq --no-install-suggests --no-install-recommends --allow-unauthenticated --allow-downgrades --allow-change-held-packages install dvipng

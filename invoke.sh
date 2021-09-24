#!/bin/bash

sls invoke local \
--verbose \
--stage prod \
--region us-west-2 \
--aws-profile s \
-f wake \
--runtime python3.8

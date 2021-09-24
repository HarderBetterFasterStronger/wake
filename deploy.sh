#!/bin/bash

AWS_PROFILE=s \
sls deploy \
--verbose \
--stage prod \
--region us-west-2 \
--aws-profile s
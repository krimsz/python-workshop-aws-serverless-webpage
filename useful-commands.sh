#!/usr/bin/env bash
docker build . --tag python-workshop-app
docker tag  python-workshop-app ECR-URL-GOES-HERE
docker push ECR-URL-GOES-HERE
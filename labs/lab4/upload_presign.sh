#!/bin/bash

aws s3 cp "$1" "s3://$2/$(basename "$1")"

aws s3 presign "s3://$2/$(basename "$1")" --expires-in "$3"



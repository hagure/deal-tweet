#!/bin/bash

SERVER = "hm"
PATH_PY_VIRTUAL = "~/path/to/server/bin/activate"
PATH_PY_DEALS = "~/path/to/server/scripts/amazon-deal.py"

#	Add local library checking

ssh hm "source '$PATH_PY_VIRTUAL'; python '$PATH_PY_DEALS' $1"
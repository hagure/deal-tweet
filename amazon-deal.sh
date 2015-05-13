#!/bin/bash


#	Add local library checking

ssh hm "source ~/hebi/bin/activate; python ~/hebi/scripts/amazon-deal.py $1"
#! /bin/bash
REPO_PATH=$(readlink -f $(dirname $0) | grep -E -o "^(.*?\\Netmaxiot)")
echo ""
echo Checking for firmware version
echo =============================
sudo python $REPO_PATH/Software/Python/Netmaxiot_check.py

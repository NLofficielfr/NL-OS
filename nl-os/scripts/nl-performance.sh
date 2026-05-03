#!/bin/bash
echo "Activation du mode performance NL..."
sudo sysctl vm.swappiness=10 2>/dev/null || true
sudo systemctl disable bluetooth 2>/dev/null || true
sudo apt clean 2>/dev/null || true
echo "Mode performance appliqué."

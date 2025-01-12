#!/bin/bash

# Define colors


GREEN='\033[32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Loop through the tools
for tool in asdf nmap ping tcpdump dig arp ifconfig route networksetup; do
    if ! command -v $tool &> /dev/null; then
        echo -e "${RED}$tool is not installed${NC}"
        echo -e "Trying to install required libraries"
        if brew search "$tool" | grep -q "^$tool$"; then
            echo "Found $tool in Homebrew. Installing..."
            brew install "$tool"
            if [[ $? -eq 0 ]]; then
                echo "$tool has been successfully installed."
            else
                echo "Failed to install $tool."
            fi
        
        else
            echo "$tool is not available in Homebrew."
        fi
        
    else
        echo -e "${GREEN}Checking: $tool ...${NC}"
    fi
done

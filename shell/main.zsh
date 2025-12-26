#!/bin/zsh

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-${(%):-%x}}")" && pwd)"

# Source all alias functions
source "$SCRIPT_DIR/mkcd.zsh"
source "$SCRIPT_DIR/rmcd.zsh"

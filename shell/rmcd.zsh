#!/bin/zsh

# rmcd function - remove current directory and cd to parent
rmcd() {
    local output mode force parent_dir dir_name
    
    # Get mode, force flag, parent directory, and directory name from Python script
    output=$(/home/buttered/Codeing/Other/oh-my-alias/aliases/rmcd.py "$@")
    mode=$(echo "$output" | sed -n '1p')
    force=$(echo "$output" | sed -n '2p')
    parent_dir=$(echo "$output" | sed -n '3p')
    dir_name=$(echo "$output" | sed -n '4p')
    
    # Cd to parent first
    cd "$parent_dir"
    
    # Remove the directory
    if [[ "$force" == "True" ]]; then
        rm_cmd="rm -rf"
    else
        rm_cmd="rmdir"
    fi
    
    if [[ "$mode" == "silent" ]]; then
        $rm_cmd "$dir_name" 2>/dev/null
    elif [[ "$mode" == "verbose" ]]; then
        if $rm_cmd "$dir_name" 2>/dev/null; then
            echo "Removed directory: $dir_name"
        else
            echo "Error: Failed to remove directory '$dir_name'" >&2
            return 1
        fi
    elif [[ "$mode" == "cre" ]]; then
        if $rm_cmd "$dir_name" 2>/dev/null; then
            echo "Removed directory: $dir_name"
        fi
    elif [[ "$mode" == "err" ]]; then
        if ! $rm_cmd "$dir_name" 2>/dev/null; then
            echo "Error: Failed to remove directory '$dir_name'" >&2
            return 1
        fi
    else  # default
        $rm_cmd "$dir_name"
    fi
}

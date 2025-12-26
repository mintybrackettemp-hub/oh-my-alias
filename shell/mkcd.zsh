#!/bin/zsh

# mkcd function - create directory and cd into it
mkcd() {
    local output mode parent dir_path
    
    # Get mode, parent flag, and directory path from Python script
    output=$(/home/buttered/Codeing/Other/oh-my-alias/aliases/mkcd.py "$@")
    mode=$(echo "$output" | sed -n '1p')
    parent=$(echo "$output" | sed -n '2p')
    dir_path=$(echo "$output" | sed -n '3p')
    
    # Create directory and cd
    if [[ "$parent" == "True" ]]; then
        mkdir_cmd="mkdir -p"
    else
        mkdir_cmd="mkdir"
    fi
    
    if [[ "$mode" == "silent" ]]; then
        $mkdir_cmd "$dir_path" 2>/dev/null && cd "$dir_path"
    elif [[ "$mode" == "verbose" ]]; then
        if $mkdir_cmd "$dir_path" 2>/dev/null; then
            echo "Created directory: $dir_path"
            cd "$dir_path"
        else
            echo "Error: Failed to create directory '$dir_path'" >&2
            return 1
        fi
    elif [[ "$mode" == "cre" ]]; then
        if $mkdir_cmd "$dir_path" 2>/dev/null; then
            echo "Created directory: $dir_path"
            cd "$dir_path"
        fi
    elif [[ "$mode" == "err" ]]; then
        if ! $mkdir_cmd "$dir_path" 2>/dev/null; then
            echo "Error: Failed to create directory '$dir_path'" >&2
            return 1
        fi
        cd "$dir_path"
    else  # default
        $mkdir_cmd "$dir_path" && cd "$dir_path"
    fi
}

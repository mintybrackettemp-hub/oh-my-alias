#!/usr/bin/env python3
"""
Uninstallation script for oh-my-alias commands (mkcd and rmcd)
"""

import os
import subprocess
import sys

def run_command(cmd, description):
    """Run a command and return success status"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        return False

def get_current_shell():
    """Get the current user's default shell"""
    try:
        result = subprocess.run(['getent', 'passwd', os.getlogin()], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.split(':')[-1].strip()
    except:
        pass
    
    # Fallback
    return os.environ.get('SHELL', '')

def switch_to_bash():
    """Prompt user to switch back to bash as default shell"""
    print("\nYou can switch back to bash as your default shell.")
    
    response = input("Would you like to switch your default shell back to bash? (y/N): ").strip().lower()
    if response in ['y', 'yes']:
        if run_command("chsh -s $(which bash)", "Switching default shell back to bash"):
            print("✓ Default shell changed back to bash")
            print("Please log out and log back in for the changes to take effect")
            return True
    else:
        print("Shell not changed. You can manually switch later with: chsh -s $(which bash)")
    return False

def uninstall():
    print("=== oh-my-alias Uninstallation Script ===\n")
    
    # Get user's home directory
    home_dir = os.path.expanduser('~')
    zshrc_path = os.path.join(home_dir, '.zshrc')
    
    if not os.path.exists(zshrc_path):
        print("✓ ~/.zshrc not found - nothing to uninstall")
        return True
    
    # Read current .zshrc
    with open(zshrc_path, 'r') as f:
        zshrc_content = f.read()
    
    # Check if oh-my-alias is installed
    if 'oh-my-alias' not in zshrc_content and 'main.zsh' not in zshrc_content:
        print("✓ oh-my-alias functions are not installed in ~/.zshrc")
        return True
    
    print("Removing oh-my-alias functions from ~/.zshrc...")
    
    # Remove the oh-my-alias related lines
    lines = zshrc_content.split('\n')
    new_lines = []
    skip_block = False
    
    for line in lines:
        # Check for oh-my-alias comment or source line containing main.zsh
        if line.strip() == '# oh-my-alias functions' or 'main.zsh' in line:
            skip_block = True
            continue
        elif skip_block and line.strip() == '':
            # Skip empty lines that follow the removed block
            continue
        else:
            skip_block = False
            new_lines.append(line)
    
    # Write back the cleaned content
    try:
        with open(zshrc_path, 'w') as f:
            f.write('\n'.join(new_lines).rstrip() + '\n')
        
        print("✓ Successfully removed oh-my-alias functions from ~/.zshrc")
        
        # Check current shell
        current_shell = get_current_shell()
        if 'zsh' in current_shell:
            switch_to_bash()
        
        print("\nUninstallation completed!")
        print("Please restart your terminal or run 'source ~/.zshrc' to apply changes")
        print("The mkcd and rmcd commands will no longer be available")
        return True
        
    except Exception as e:
        print(f"✗ Failed to update ~/.zshrc: {e}")
        return False

if __name__ == '__main__':
    success = uninstall()
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
Installation script for oh-my-alias commands (mkcd and rmcd)
"""

import os
import shutil
import subprocess
import sys
import platform

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

def detect_distro():
    """Detect the Linux distribution"""
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('ID='):
                    return line.split('=')[1].strip().strip('"')
    except FileNotFoundError:
        pass
    
    # Fallback detection
    try:
        result = subprocess.run(['lsb_release', '-i'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.split(':')[1].strip().lower()
    except FileNotFoundError:
        pass
    
    return None

def install_zsh():
    """Install Zsh based on the detected distribution"""
    distro = detect_distro()
    print(f"Detected distribution: {distro}")
    
    if distro in ['ubuntu', 'debian', 'linuxmint', 'pop']:
        return run_command("sudo apt update && sudo apt install -y zsh", "Installing Zsh on Ubuntu/Debian")
    elif distro in ['arch', 'manjaro', 'endeavouros']:
        return run_command("sudo pacman -S --noconfirm zsh", "Installing Zsh on Arch Linux")
    elif distro in ['fedora', 'centos', 'rhel']:
        return run_command("sudo dnf install -y zsh", "Installing Zsh on Fedora/RHEL")
    else:
        print(f"✗ Unsupported distribution: {distro}")
        print("Please install Zsh manually and run this script again")
        return False

def check_zsh_installed():
    """Check if Zsh is installed"""
    try:
        result = subprocess.run(['which', 'zsh'], capture_output=True)
        return result.returncode == 0
    except FileNotFoundError:
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

def switch_to_zsh():
    """Prompt user to switch to Zsh as default shell"""
    print("\nYour current default shell is bash.")
    print("To use the oh-my-alias commands, you need to switch to Zsh.")
    
    response = input("Would you like to switch your default shell to Zsh? (y/N): ").strip().lower()
    if response in ['y', 'yes']:
        if run_command("chsh -s $(which zsh)", "Switching default shell to Zsh"):
            print("✓ Default shell changed to Zsh")
            print("Please log out and log back in for the changes to take effect")
            return True
    else:
        print("Shell not changed. You can manually switch later with: chsh -s $(which zsh)")
    return False

def install():
    print("=== oh-my-alias Installation Script ===\n")
    
    # Check if Zsh is installed
    if not check_zsh_installed():
        print("Zsh is not installed.")
        if not install_zsh():
            print("Installation failed. Please install Zsh manually.")
            return False
    
    # Check current shell
    current_shell = get_current_shell()
    if 'bash' in current_shell:
        switch_to_zsh()
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Paths to the files
    main_script = os.path.join(script_dir, 'shell', 'main.zsh')
    
    # Check if files exist
    if not os.path.exists(main_script):
        print(f"✗ Main script not found at {main_script}")
        return False
    
    # Get user's home directory
    home_dir = os.path.expanduser('~')
    
    # Check for .zshrc
    zshrc_path = os.path.join(home_dir, '.zshrc')
    if not os.path.exists(zshrc_path):
        print("Creating ~/.zshrc file...")
        try:
            with open(zshrc_path, 'w') as f:
                f.write("# Zsh configuration\n")
            print("✓ Created ~/.zshrc")
        except Exception as e:
            print(f"✗ Failed to create ~/.zshrc: {e}")
            return False
    else:
        print("✓ ~/.zshrc already exists")
    
    # Check if already installed
    with open(zshrc_path, 'r') as f:
        zshrc_content = f.read()
    
    if 'source.*main.zsh' in zshrc_content or 'oh-my-alias' in zshrc_content:
        print("oh-my-alias functions are already installed in ~/.zshrc")
        return True
    
    # Add to .zshrc
    print("Adding oh-my-alias functions to ~/.zshrc...")
    try:
        with open(zshrc_path, 'a') as f:
            f.write('\n# oh-my-alias functions\n')
            f.write(f'source "{main_script}"\n')
        
        print("✓ Successfully added oh-my-alias functions to ~/.zshrc")
        print("\nInstallation completed!")
        print("Please restart your terminal or run 'source ~/.zshrc' to use mkcd and rmcd")
        return True
    except Exception as e:
        print(f"✗ Failed to update ~/.zshrc: {e}")
        return False

if __name__ == '__main__':
    success = install()
    sys.exit(0 if success else 1)

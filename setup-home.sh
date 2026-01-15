#!/bin/bash
# setup-home.sh - Home directory setup script
# Part of f-rsta-g-ngen

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOTFILES_DIR="$SCRIPT_DIR/dotfiles"

echo "Setting up home directory..."

# Create necessary directories
mkdir -p "$HOME/.local/bin"
mkdir -p "$HOME/.config"

# Function to backup and link a dotfile
link_dotfile() {
    local src="$1"
    local dest="$2"

    if [ -f "$dest" ] && [ ! -L "$dest" ]; then
        echo "Backing up existing $dest to $dest.backup"
        mv "$dest" "$dest.backup"
    fi

    if [ -L "$dest" ]; then
        rm "$dest"
    fi

    echo "Linking $src -> $dest"
    ln -s "$src" "$dest"
}

# Link dotfiles
if [ -f "$DOTFILES_DIR/.bashrc" ]; then
    link_dotfile "$DOTFILES_DIR/.bashrc" "$HOME/.bashrc"
fi

if [ -f "$DOTFILES_DIR/.gitconfig" ]; then
    link_dotfile "$DOTFILES_DIR/.gitconfig" "$HOME/.gitconfig"
fi

echo ""
echo "Home directory setup complete!"
echo ""
echo "Note: You may need to edit ~/.gitconfig to set your name and email:"
echo "  git config --global user.name \"Your Name\""
echo "  git config --global user.email \"your.email@example.com\""
echo ""
echo "To apply changes to your current shell, run:"
echo "  source ~/.bashrc"

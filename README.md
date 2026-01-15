# f-rsta-g-ngen

## Installation

### PowerShell (Windows)

You can install using PowerShell with a single command:

```powershell
irm https://claude.ai/install.ps1 | iex
```

This command downloads and executes the installation script directly from the Claude website.

### Alternative Methods

#### Manual Installation

1. Download the installer from [https://claude.ai](https://claude.ai)
2. Run the installer for your operating system
3. Follow the on-screen instructions

#### Linux/macOS

```bash
curl -fsSL https://claude.ai/install.sh | sh
```

## Home Directory Setup

This repository includes dotfiles and a setup script to configure your home directory with useful defaults.

### Quick Setup

Run the setup script to configure your home directory:

```bash
./setup-home.sh
```

This will:
- Create `~/.local/bin` and `~/.config` directories
- Symlink `.bashrc` with useful aliases (including `c` for `claude`)
- Symlink `.gitconfig` with sensible defaults

### Manual Setup

You can also copy files manually:

```bash
cp dotfiles/.bashrc ~/.bashrc
cp dotfiles/.gitconfig ~/.gitconfig
```

Remember to update `.gitconfig` with your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Getting Started

After installation, you can start using Claude Code by opening your terminal and running:

```bash
claude
```

For more information, visit the [official documentation](https://claude.ai/docs).
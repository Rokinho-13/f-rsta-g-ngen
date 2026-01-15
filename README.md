# f-rsta-g-ngen

## Installation

### PowerShell (Windows)

#### Quick Install (inspect script first)

```powershell
# Download the script
irm https://claude.ai/install.ps1 -OutFile install.ps1

# Inspect the script before running
notepad install.ps1

# Execute after verification
.\install.ps1
```

#### One-line Install (advanced users only)

For advanced users who trust the source, you can use:

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Warning:** This downloads and executes code directly. Only use if you trust the source.

### Alternative Methods

#### Manual Installation

1. Download the installer from [https://claude.ai](https://claude.ai)
2. Run the installer for your operating system
3. Follow the on-screen instructions

#### Linux/macOS

**Recommended:** Download and inspect before running:

```bash
# Download the script
curl -fsSL https://claude.ai/install.sh -o install.sh

# Inspect the script
cat install.sh
# or use your preferred editor: nano install.sh, vim install.sh, etc.

# Make executable and run after verification
chmod +x install.sh
./install.sh
```

**One-line install (advanced users only):**

```bash
curl -fsSL https://claude.ai/install.sh | sh
```

**Warning:** This downloads and executes code directly. Only use if you trust the source.

## Getting Started

After installation, you can start using Claude Code by opening your terminal and running:

```bash
claude
```

For more information, visit the [official documentation](https://claude.ai/docs).
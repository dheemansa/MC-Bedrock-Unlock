# MC Bedrock Unlocker

A Windows application that automates the process of modifying system DLL files to unlock Minecraft Bedrock Edition features.

## ⚠️ IMPORTANT DISCLAIMER

**This project is created for PROOF OF CONCEPT and EDUCATIONAL purposes only.** 

- **No illegal intent** is associated with this software
- The author does not encourage or endorse any illegal activities
- Users are responsible for complying with their local laws and software licenses
- This tool modifies Windows system files, which may violate Microsoft's Terms of Service
- Use at your own risk and responsibility

## Background

This application automates a manual process that was demonstrated in a YouTube video by SSG channel: https://www.youtube.com/watch?v=6T-Yy4iEBMk

The custom DLL files used in this project are sourced from **untrusted sources** and their safety/legitimacy cannot be guaranteed. The author has simply created an automation tool to replace the manual process without requiring dependencies like IObit Unlocker.


## System Requirements

- Windows 10/11 (32-bit or 64-bit)
- Administrator privileges
- Python 3.7+ (if running from source)
- PyQt5 library (if running from source)

## Installation & Usage

### Method 1: Run from Source
1. Install Python 3.7+
2. Install required dependencies:
   ```bash
   pip install PyQt5
   ```
3. Place custom DLL files in the appropriate `dll/` subdirectories
4. Right-click on Command Prompt/PowerShell and select "Run as Administrator"
5. Navigate to the project directory
6. Run: `python main.py`

### Method 2: Executable (if available)
1. Download the executable release
2. Ensure DLL files are in the correct directory structure
3. Right-click the executable and select "Run as Administrator"

## How It Works

### Unlock Process
1. **File Detection**: Identifies target system DLL files based on architecture
2. **Backup Creation**: Creates `.backup` files of original system DLLs
3. **Ownership Transfer**: Uses `takeown` command to gain file ownership
4. **Permission Modification**: Uses `icacls` to grant full administrator access
5. **File Replacement**: Deletes original files and copies custom DLLs
6. **Verification**: Confirms successful file replacement

### Restore Process
1. **SFC Execution**: Runs `sfc /scannow` command
2. **System Verification**: Windows checks and restores modified system files
3. **Original Files**: Restores Microsoft's original DLL files

## Target Files

The application modifies these Windows system files:

**32-bit Systems:**
- `C:\Windows\System32\Windows.ApplicationModel.Store.dll`

**64-bit Systems:**
- `C:\Windows\System32\Windows.ApplicationModel.Store.dll`
- `C:\Windows\SysWOW64\Windows.ApplicationModel.Store.dll`

## Security Warnings

- **System File Modification**: This tool modifies critical Windows system files
- **Unknown DLL Sources**: Custom DLLs are from untrusted sources
- **Potential Risks**: May cause system instability or security vulnerabilities
- **Backup Recommended**: Create a system restore point before use
- **Antivirus Detection**: May be flagged as potentially unwanted software

## Legal Considerations

- Modifying system files may violate Microsoft's Terms of Service
- Using modified DLLs to bypass software restrictions may violate software licenses
- Users are solely responsible for legal compliance in their jurisdiction
- This tool is provided AS-IS without any warranties

## Technical Implementation

- **Language**: Python 3.7+
- **GUI Framework**: PyQt5
- **Threading**: QThread for non-blocking operations
- **System Commands**: Windows takeown, icacls, sfc utilities
- **Logging**: Python logging module with file and console output

## Troubleshooting

**Common Issues:**
- **Access Denied**: Ensure running as Administrator
- **Missing DLLs**: Verify custom DLL files are in correct directories
- **SFC Fails**: May require Windows installation media for some repairs
- **Process Locked**: Restart system if files are in use

## Contributing

This is a proof-of-concept project. Contributions should focus on code quality and safety improvements rather than expanding functionality for potentially problematic use cases.

## Credits

- Original process demonstrated by SSG YouTube channel
- Custom DLL files sourced from community (untrusted sources)

## License

This project is provided for educational purposes. Users assume all responsibility for its use.

---

**Remember: This tool modifies critical system files. Use with extreme caution and only if you understand the risks involved.**
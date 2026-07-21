# Project Guide: Security Framework Portfolio

## Project Overview
This project is a modular security framework designed for offensive security research, payload generation, and listener management. It is structured as a toolkit to facilitate the development and deployment of various exploit components.

**Key Technologies:**
- **Python:** Primary language for orchestration (`bootstrap.py`) and listener logic.
- **C/C++:** Used for low-level payload development.
- **Lua:** Used for scripting custom payload logic.
- **Shell (Bash):** Used for environment manipulation and payload execution.

**High-Level Architecture:**
The project follows a modular plugin-style architecture where different capabilities (encoders, payloads, listeners) are isolated into their own directories for easy extensibility.

## Getting Started
*Note: As this is a portfolio piece, some components may be in a conceptual state.*

### Prerequisites
- Python 3.x
- GCC/G++ compiler (for `.cpp` and `.c` payloads)
- Lua interpreter (for `.lua` payloads)
- Linux environment (recommended)

### Installation
1. Clone the repository.
2. Ensure all dependencies are installed.
3. Use the `MakeFile` (when fully implemented) to compile native payloads.

### Basic Usage
The intended entry point is `bootstrap.py`, which is designed to initialize the framework and load the necessary modules from the `framework/` directory.

## Project Structure
- `bootstrap.py`: The main entry point and framework initializer.
- `MakeFile`: Build system for compiling native payload components.
- `framework/`: The core logic directory.
    - `payloads/`: Contains various exploit payloads in multiple languages (`.cpp`, `.py`, `.lua`, `.sh`, `.c`).
    - `listeners/`: Logic for handling incoming connections from deployed payloads.
    - `encoders/`: Tools to obfuscate payloads to bypass detection.
    - `bruteforce/`: Modules for credential cracking and service enumeration.
    - `auxilliaries/`: Support scripts and utility tools.
    - `config/`: Configuration settings for the framework and its modules.
    - `utils/`: Shared helper functions used across the framework.

## Development Workflow
- **Adding Payloads:** Place new payload scripts in `framework/payloads/`. If the payload requires compilation, add the target to the `MakeFile`.
- **Module Development:** Follow the pattern established in `framework/listeners/` for creating new network handlers.
- **Documentation:** Use the `ideas.md` files found in each subdirectory to brainstorm and document the theoretical implementation of new features.

## Key Concepts
- **Payloads:** The code executed on a target system.
- **Listeners:** The server-side component that waits for a payload to "call back."
- **Encoding:** The process of modifying payload bytes to avoid signature-based detection (AV/EDR).
- **Bootstrapping:** The process of initializing the framework environment before launching specific modules.

## Common Tasks
- **Compiling a Payload:** Run `make` in the root directory (assuming `MakeFile` is configured).
- **Testing a Listener:** Execute `python3 framework/listeners/listening.py` and attempt a connection from a test payload.
- **Iterating on Ideas:** Update the respective `ideas.md` in the module folder to track feature requests.

## Troubleshooting
- **Compilation Errors:** Ensure the correct compiler flags are set in the `MakeFile` for the target architecture.
- **Connection Issues:** Verify firewall settings and that the listener is bound to the correct interface/port.

## References
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [OWASP](https://owasp.org/)
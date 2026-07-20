# Design Document for C2 Framework

At the end of the day, I constantly hear about frameworks being stuck in one pattern, with easily identifiable IoCs.

Some goals: 
    cli and terminal driven
    expandability and flexibility in payloads



## Legalise note:

Do not actually try this at home kids. I built this to impress employeers, not to cause damage :D

## Feature Ideas:

- **Dynamic Code Loading:** Load packages and code with a watcher script/thread.
- **Customizable Payloads:** Different payloads for different targets. (perhaps a text editor)
- **Command Line Interface:** Simple and powerful CLI for quick interactions.
- **Persistence Mechanisms:** Ensure the agent stays running across reboots. (possible)
- **Network Communication:** Reliable and encrypted communication channels
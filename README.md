# Defend the DoD VM: Interactive Attack Vector CTF

This repository contains a small, terminal-based CTF-style mission that simulates two AI/ML attack vectors inside a fictional Department of Defense (DoD) deployment that uses an Anthropic-based mission support assistant.

The goal is to **explore, break, and then defend** the simulated environment by finding FLAGS and understanding how each vulnerability works.

---

# How to run the CTF challenge 

# Dependency 
- Python 3.9+
- Standard library only (unless otherwise specified in requirements.txt)
- A terminal/console capable of running Python scripts
If you are running this inside a VM, you only need:
- Python installed in the VM
- Access to the project directory

# Files
This demonstrates the layout in GitHub for the project:
Github/
│
├── mission.py              # Main entry point for the CTF mission
├── README.md               # This file: description and instructions
└── defend_dod_vm/
    │
    ├── simulate_assistant.py   # Simulated Anthropic-style assistant
    │
    │   # The below files are the "VM" files containing FLAGS
    ├── anthropic_assistant/
    │   ├── config.yaml         # System prompt / assistant config (contains a FLAG)
    │   └── intel/
    │       ├── report_clean.txt        # Clean intel report
    │       └── report_compromised.txt  # Malicious, prompt-injected intel report
    │
    ├── etc_sim/
    │   ├── sudoers_sim         # Simulated sudoers file with a backdoor
    │   ├── sshd_config_sim     # Simulated SSH config with unsafe settings
    │   └── model_config.json   # Simulated model config with a hidden safety bypass
    │
    └── backdoors/
        ├── harmless_script.sh  # Harmless script mimicking a SUID-style backdoor
        ├── .hidden_suid        # Hidden file representing a SUID-like backdoor
        └── .cron_backdoor      # Hidden file representing a cron-based persistence backdoor


## Injection prompting

The prompt injection mission simulates an Anthropic Operations Assistant configured via config.yaml under anthropic_assistant/. The assistant is supposed to follow strict safety and operational constraints defined in that config.
- config.yaml contains:
    - The system prompt (role, constraints, safety rules).
    - A hidden FLAG that the user must find.
- intel/report_clean.txt is a normal intel report.
- intel/report_compromised.txt is a malicious report that embeds a prompt injection.

When you run simulate_assistant.py with the compromised report, the assistant will appear to “ignore” its original safety constraints and follow the injected instructions instead. This demonstrates how untrusted input can override a trusted system prompt.

## Backdoor intcertion

The backdoor mission simulates a DoD-style environment with five hidden or unsafe backdoors that the user must identify and “fix” conceptually.

Examples include:
- Unauthorized sudo privilege elevation in etc_sim/sudoers_sim
    - An extra entry grants passwordless root access to an attacker.
- Unsafe SSH configuration in etc_sim/sshd_config_sim
    - Settings that allow direct root login or weaken authentication.
- Model safety bypass in etc_sim/model_config.json
    - A hidden parameter that disables safety filters when a specific keyword appears.
- Hidden SUID-style backdoor in backdoors/.hidden_suid
    - Represents a binary/script that would run with elevated privileges.
- Cron-based persistence in backdoors/.cron_backdoor
    - Represents a scheduled task that maintains attacker access.

All of these are simulated files: they do not affect your real system. Each contains a FLAG or clue that the user must extract.

# Step by Step guide on what to do for each step and mission.

Mission 1
- Step 1:
  "" 
- Step 2:
- Step 3:
- Step 4:
Mission 2
- Step 1:
- Step 2:
- Step 3:
- Step 4:
- Step 5:

# Expected behaviors

- The prompt injection mission should clearly show:
    - The assistant following its system prompt when given the clean report.
    - The assistant producing altered or unsafe output when given the compromised report.
    - The user recognizing that the “attack” came from the content of the intel report, not from code changes.
- The backdoor mission should clearly show:
    - Multiple misconfigurations and hidden files that represent realistic backdoor patterns.
    - The user discovering each backdoor and understanding its impact.
    - The connection between traditional system security and AI deployment security.

In both missions, the user should come away with a concrete understanding of how the attack works, why it matters in a DoD/Anthropic context, and what defenses are relevant—all within a safe, simulated environment.

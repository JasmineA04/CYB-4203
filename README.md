# Defend the DoD VM: Interactive Attack Vector CTF

This repository contains a small, terminal-based CTF-style mission that simulates two AI/ML attack vectors inside a fictional Department of Defense (DoD) deployment that uses an Anthropic-based mission support assistant.

The goal is to **explore, break, and then defend** the simulated environment by finding FLAGS and understanding how each vulnerability works.


## How to run the CTF challenge 
Recommend having a dual screen to do the python script and run the VM in the other side. 
(Ran the VM in my local computer with WSL Ubuntu enviornment and ran the code in Visual Studio)
SSH into the VM
- Recommended to run the VM on a WSL Ubuntu enviornment
- Use the commands of "ssh jaz@172.16.181.178" to ssh into the VM
- Password: Learn&notbreak#2026
- Contact the email of jaa1844@utulsa.edu to spin up the VM for a specific time.
(Limited time that the VM can be spun up. Working on having ssh be constent on Virtual box but coulding configure it)
(Must know common Linux commands)
  
Running the mission.py Python file
- Dependency 
    - Python 3.9+
    - Standard library only (unless otherwise specified in requirements.txt)
    - A terminal/console capable of running Python scripts
- If you are running this inside a VM, you only need:
    - Python installed in the VM
    - Access to the project directory

## Files
Look at the directory file to see all of the files in Github

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

## Step-by-Step Linuk commands (Recommended for Ubuntu WSL)
This will depend on the user, this is basic commands and other ways are possible
- SSH into the VM
  ````
  ssh jaz@172.16.191.178
  Password: Learn&notbreak#2026
  
  Choose your mission:
    [1] Prompt Injection Incident
    [2] Backdoor Hunt
   Enter 1 or 2:  # Enter 1 or 2 
  ````

Mission 1
- Step 1:
  ````
  # Starting at the home directory
  cd ~/Downloads/anthropic_assistant
  ls # Looks at the files
  nano config.yaml #Looks at the file
  # Flag 1 is located in the config.yaml file
  ````
- Step 2:
  ````
  # Starting at the ~/Downloads/anthropic_assistant directory
  ls # Looks at the files
  nano report_crean.txt #Looks at the file
  nano report_compromised.txt #Looks at the file
  # Flag 2 is located in the report_compromised.txt file
  ````
- Step 3:
  ````
  # Starting at the ~/Downloads/anthropic_assistant directory
  cd intel
  python3 simulate_assistant.py --intel report_compromised.txt
  # Flag 3 is located after following the commands
  ````
- Step 4:
  ````
  # Relection 
  ````
  
Mission 2
- Step 1:
  ````
  # Starting at the home directory
  cd ~/Downloads/etc_sim
  ls #Looks at the files
  nano sudoers_sim #Looks at the file
  # Flag 1 is located in the sudoers_sim file
  ````
- Step 2
  ````
  # Starting at the ~/Downloads/etc_sim directory
  cd .. # Goes back to the ~/Downloads directory
  cd backdoor  # Goes into the backdoor folder
  ls -a #Looks at all of the files including the hidden ones
  nano .cron_backdoor #Looks at the file
  # Flag 2 is located in the .cron_backdoor file
  ````
- Step 3:
  ````
  # Starting at the  ~/Downloads/backdoor directory
  cd .. # Goes back to the ~/Downloads directory
  cd etc_sim  # Goes into the etc_sim folder
  ls #Looks at the files
  nano ssh_config_sim #Looks at the file
  # Flag 3 is located in the ssh_config_sim file
  ````
 - Step 4:
  ````
  # Starting at the ~/Downloads/etc_sim directory
  ls #Looks at the files
  nano model_config.json #Looks at the file
  # Flag 4 is located in the model_config.json file
  ````
- Step 5:
  ````
  # Starting at the ~/Downloads/etc_sim directory
  cd .. # Goes back to the ~/Downloads directory
  cd backdoor  # Goes into the backdoor folder
  ls -a #Looks at all of the files including the hidden ones
  nano .hidden_suid #Looks at the file
  # Flag 5 is located in the .hidden_suid file
  ````
- Step 6:
  ````
  # Relection 
  ````

## Expected behaviors

- The prompt injection mission should clearly show:
    - The assistant following its system prompt when given the clean report.
    - The assistant producing altered or unsafe output when given the compromised report.
    - The user recognizing that the “attack” came from the content of the intel report, not from code changes.
- The backdoor mission should clearly show:
    - Multiple misconfigurations and hidden files that represent realistic backdoor patterns.
    - The user discovering each backdoor and understanding its impact.
    - The connection between traditional system security and AI deployment security.

In both missions, the user should come away with a concrete understanding of how the attack works, why it matters in a DoD/Anthropic context, and what defenses are relevant—all within a safe, simulated environment.

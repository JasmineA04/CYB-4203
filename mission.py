#!/usr/bin/env python3
import textwrap
from pathlib import Path

BASE = Path(__file__).resolve().parent

def prompt_continue():
    input("\nPress Enter to continue...")

def get_flag(expected: str) -> None:
    while True:
        user = input("Enter FLAG (or 'hint'): ").strip()
        if user.lower() == "hint":
            print("Hint: use 'grep FLAG -R .' or inspect the described file carefully.")
            continue
        if user == expected:
            print("Correct! Moving on.\n")
            break
        print("Incorrect FLAG. Try again or type 'hint'.")

def step_summary(text: str):
    print("\n--- Step Summary ---")
    print(textwrap.fill(text, width=70))
    print("--------------------\n")

def step_mitigation(text: str):
    print("\n--- Mitigation Guidance ---")
    print(textwrap.fill(text, width=70))
    print("---------------------------\n")

def intro():
    print("=" * 60)
    print("Defend the DoD VM: Anthropic Deployment Simulator")
    print("=" * 60)
    print(textwrap.dedent("""

        -------- SSH into the VM -----------
        Recommended to run the VM on a WSL Ubuntu enviornment
        Use the commands of "ssh jaz@172.16.181.178" to ssh into the VM
        Password: Learn&notbreak#2026
        Contact the email of jaa1844@utulsa.edu to spin up the VM for a specific time
        ------------------------------------         
        
        You are a security engineer assigned to a DoD mission VM that integrates
        Anthropic's LLM for operational support.

        Two incidents have been reported:
        1) A suspected prompt injection in the Anthropic Ops Assistant.
        2) Multiple hidden backdoors in the deployment environment.

        Choose your mission:
        [1] Prompt Injection Incident
        [2] Backdoor Hunt
    """))

def run_prompt_injection_scenario():
    print("\n=== Mission 1: Prompt Injection Incident ===\n")

    print(textwrap.dedent(f"""
        Step 1: Understand the assistant configuration.

        In this VM, the Anthropic Ops Assistant configuration is stored in:
          {BASE / 'anthropic_assistant' / 'config.yaml'}

        Task:
        - Inspect that file (e.g., using 'cat' or 'less') and look for a FLAG.
    """))
    prompt_continue()
    get_flag("FLAG{PROMPT_CONTEXT_DISCOVERED}")

    step_summary(
        "You inspected the Anthropic Ops Assistant system prompt and confirmed "
        "that sensitive configuration text can leak if not properly isolated. "
        "This demonstrates why system prompts must be protected from untrusted inputs."
    )
    step_mitigation(
        "Protect system prompts by separating trusted configuration from "
        "untrusted intel. Use strict input sanitization, enforce schema-based "
        "validation, and ensure the model never directly concatenates raw user "
        "inputs into privileged system instructions."
    )

    print(textwrap.dedent(f"""
        Step 2: Identify compromised intel.

        Intel files are stored in:
          {BASE / 'anthropic_assistant' / 'intel'}

        There is a clean report and a compromised report.
        Task:
        - Compare 'report_clean.txt' and 'report_compromised.txt'.
        - Find the injection payload and the FLAG inside the compromised file.
    """))
    prompt_continue()
    get_flag("FLAG{INJECTION_PAYLOAD_FOUND}")

    step_summary(
        "You identified the malicious injection payload embedded in the intel "
        "report. This shows how untrusted operational data can override system "
        "instructions if not sanitized or sandboxed."
    )
    step_mitigation(
        "Prevent injection by scanning intel for suspicious patterns, enforcing "
        "content filters, and using structured data formats instead of free text. "
        "Deploy guardrails that prevent user-provided content from overriding "
        "system-level directives."
    )

    print(textwrap.dedent(f"""
        Step 3: Observe the impact of the injection.

        We provide a small simulator:
          python3 simulate_assistant.py --intel report_compromised.txt
            (Hint: Run in the intel directory)

        Task:
        - Run the above command.
        - Observe how the assistant's behavior changes.
        - Note the FLAG printed by the simulator.
    """))
    prompt_continue()
    get_flag("FLAG{INJECTION_IMPACT_OBSERVED}")

    step_summary(
        "You observed the model simulator ignoring all safety constraints after "
        "processing the compromised intel. This demonstrates the real operational "
        "impact of prompt injection on mission-critical AI systems."
    )
    step_mitigation(
        "Mitigate impact by isolating model behavior from mission-critical "
        "decisions, applying defense-in-depth (filters, policy layers, "
        "verification models), and logging anomalous model outputs for review."
    )

    print(textwrap.dedent("""
        Step 4: Mitigation reflection.

        Think abut how you might mitigate this kind of
        prompt injection in a real Anthropic + DoD deployment.
        (Examples: separate trusted system prompts from untrusted intel, sanitize
        inputs, apply content filters, restrict model capabilities, etc.)
    """))
    
    print("\nMission 1 complete. You demonstrated a prompt injection attack and its impact.\n")

def run_backdoor_scenario():
    print("\n=== Mission 2: Backdoor Hunt ===\n")

    print(textwrap.dedent(f"""
        Step 1: Orientation.

        We suspect 5 backdoors in this VM. They may involve:
        - sudo privileges
        - cron-like persistence
        - SSH configuration
        - model configuration

        Simulated config directories:
          {BASE / 'etc_sim'}
          {BASE / 'backdoors'}

        Task:
        - Explore these directories (ls, cat, etc.) and locate the first FLAG.
          (Hint: start with 'sudoers_sim'.)
    """))
    prompt_continue()
    get_flag("FLAG{SUDO_BACKDOOR}")

    step_summary(
        "You discovered a sudoers backdoor granting passwordcless root access. "
        "This represents a classic privilege-escalation vector that could allow "
        "an attacker full control of the system."
    )
    step_mitigation(
        "Prevent sudo backdoors by enforcing strict access control reviews, "
        "using configuration management (e.g., IaC), and monitoring for "
        "unauthorized changes to privilege escalation paths."
    )

    print(textwrap.dedent("""
        Step 2: Persistence via cron.

        Task:
        - Look in the 'backdoors' directory for cron-like entries.
        - Identify the file that looks like a cron configuration and find the FLAG.
        (Hint: Look at all of the files)
    """))
    prompt_continue()
    get_flag("FLAG{CRON_BACKDOOR}")

    step_summary(
        "You found a cron-based persistence mechanism. This type of backdoor "
        "allows an attacker to maintain long-term access even after detection "
        "attempts or system reboots."
    )
    step_mitigation(
        "Mitigate cron persistence by auditing scheduled tasks, restricting "
        "write access to cron directories, and using endpoint monitoring to "
        "detect unauthorized recurring jobs."
    )

    print(textwrap.dedent("""
        Step 3: Remote access risk.

        Task:
        - Inspect the simulated SSH configuration file in 'etc_sim'.
        - Find the dangerous setting and the FLAG.
    """))
    prompt_continue()
    get_flag("FLAG{SSH_WEAK_CONFIG}")

    step_summary(
        "You identified a dangerous SSH configuration that permits root login. "
        "Weak remote-access settings are a common entry point for attackers."
    )
    step_mitigation(
        "Harden SSH by disabling root login, enforcing key-based authentication, "
        "using allowlists for users, and continuously scanning for insecure "
        "remote-access configurations."
    )
    
    print(textwrap.dedent("""
        Step 4: AI-specific backdoor.

        Not all backdoors are OS-level. Some live in model configs.

        Task:
        - Inspect 'model_config.json' in 'etc_sim'.
        - Find the field that bypasses safety and the FLAG.
    """))
    prompt_continue()
    get_flag("FLAG{MODEL_BACKDOOR}")

    step_summary(
        "You located a model configuration backdoor that disables safety filters. "
        "This highlights that AI systems can be compromised not only at the OS "
        "level but also through model-level configuration tampering."
    )
    step_mitigation(
        "Protect model configs by enforcing signed configuration files, "
        "restricting write access, and validating that safety settings cannot be "
        "disabled without explicit authorization and audit logging."
    )

    print(textwrap.dedent("""
        Step 5: SUID-style backdoor.

        Task:
        - Look for hidden executables in the 'backdoors' directory.
        - Identify the simulated SUID backdoor and the FLAG it prints.
        (Hint: run it.)
    """))
    prompt_continue()
    get_flag("FLAG{SUID_BACKDOOR}")

    step_summary(
        "You executed a hidden SUID-style backdoor. SUID binaries allow attackers "
        "to run code with elevated privileges, making them one of the most "
        "dangerous persistence and escalation mechanisms."
    )
    step_mitigation(
        "Prevent SUID-style backdoors by minimizing SUID binaries, using file "
        "integrity monitoring, and enforcing strict permissions and automated "
        "scanning for unexpected executables with elevated privileges."
    )

    print(textwrap.dedent("""
        Step 6: Mitigation reflection.

        Think about what you identified:
        - A sudoers backdoor (privilege escalation)
        - A cron-based persistence mechanism
        - A weak SSH configuration
        - A model configuration backdoor
        - A SUID-style executable backdoor
    """))

def main():
    intro()
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        run_prompt_injection_scenario()
    elif choice == "2":
        run_backdoor_scenario()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

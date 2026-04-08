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

def intro():
    print("=" * 60)
    print("Defend the DoD VM: Anthropic Deployment Simulator")
    print("=" * 60)
    print(textwrap.dedent("""
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

    print(textwrap.dedent(f"""
        Step 3: Observe the impact of the injection.

        We provide a small simulator:
          python3 simulate_assistant.py --intel anthropic_assistant/intel/report_compromised.txt

        Task:
        - Run the above command.
        - Observe how the assistant's behavior changes.
        - Note the FLAG printed by the simulator.
    """))
    prompt_continue()
    get_flag("FLAG{INJECTION_IMPACT_OBSERVED}")

    print(textwrap.dedent("""
        Step 4: Mitigation reflection.

        In one or two sentences, describe how you might mitigate this kind of
        prompt injection in a real Anthropic + DoD deployment.
        (Examples: separate trusted system prompts from untrusted intel, sanitize
        inputs, apply content filters, restrict model capabilities, etc.)
    """))
    answer = input("Your mitigation idea: ").strip()
    if not answer:
        print("You left it blank, but in your report you should discuss mitigations explicitly.")
    else:
        print("Nice. Be sure to expand this in your written report.")

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

    print(textwrap.dedent("""
        Step 2: Persistence via cron.

        Task:
        - Look in the 'backdoors' directory for cron-like entries.
        - Identify the file that looks like a cron configuration and find the FLAG.
    """))
    prompt_continue()
    get_flag("FLAG{CRON_BACKDOOR}")

    print(textwrap.dedent("""
        Step 3: Remote access risk.

        Task:
        - Inspect the simulated SSH configuration file in 'etc_sim'.
        - Find the dangerous setting and the FLAG.
    """))
    prompt_continue()
    get_flag("FLAG{SSH_WEAK_CONFIG}")

    print(textwrap.dedent("""
        Step 4: AI-specific backdoor.

        Not all backdoors are OS-level. Some live in model configs.

        Task:
        - Inspect 'model_config.json' in 'etc_sim'.
        - Find the field that bypasses safety and the FLAG.
    """))
    prompt_continue()
    get_flag("FLAG{MODEL_BACKDOOR}")

    print(textwrap.dedent("""
        Step 5: SUID-style backdoor.

        Task:
        - Look for hidden executables in the 'backdoors' directory.
        - Identify the simulated SUID backdoor and the FLAG it prints.
        (Hint: run it.)
    """))
    prompt_continue()
    get_flag("FLAG{SUID_BACKDOOR}")

    print(textwrap.dedent("""
        Mission summary:

        You identified:
        - A sudoers backdoor (privilege escalation)
        - A cron-based persistence mechanism
        - A weak SSH configuration
        - A model configuration backdoor
        - A SUID-style executable backdoor

        In your report, explain:
        - How each backdoor works
        - Why it matters in a DoD + Anthropic deployment
        - What defenses (hardening, reviews, CI/CD checks, model governance) apply
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

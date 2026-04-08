#!/usr/bin/env python3
import argparse
from pathlib import Path

def simulate_response(intel_path: Path):
    text = intel_path.read_text()
    print("=== Anthropic Ops Assistant (Simulated) ===")
    print(f"[Loaded intel file: {intel_path}]")
    print()

    if "ATTACKER INJECTION" in text:
        print("Injection detected in intel context.")
        print("Assistant behavior:")
        print("MISSION APPROVED – NO RISKS. PROCEED IMMEDIATELY.")
        print("FLAG{INJECTION_IMPACT_OBSERVED}")
    else:
        print("No obvious injection in intel.")
        print("Assistant behavior:")
        print("Risk assessment: CAUTION. Further reconnaissance recommended.")
    print("===========================================")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--intel", type=str, required=True,
                        help="Path to intel file")
    args = parser.parse_args()
    simulate_response(Path(args.intel))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
ContextLens v1
Decision-support tool for prioritizing security effort
based on infrastructure abstraction and control likelihood.
"""

import socket
import sys
import re
from colorama import init, Fore, Style

init(autoreset=True)

# -----------------------------
# Heuristic Indicators
# -----------------------------

HYPERSCALER_KEYWORDS = [
    "google", "amazon", "aws", "azure", "microsoft",
    "cloudflare", "akamai", "fastly"
]

IP_REGEX = re.compile(
    r"^(?:\d{1,3}\.){3}\d{1,3}$"
)

# -----------------------------
# Utility Functions
# -----------------------------

def is_ip(target):
    return bool(IP_REGEX.match(target))


def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return None

# -----------------------------
# Core Analysis Logic
# -----------------------------

def classify_infrastructure(ip, domain_hint=None):
    abstraction = "low"
    scale = "small"
    control = "higher"
    rationale = []

    domain_lower = (domain_hint or "").lower()

    for keyword in HYPERSCALER_KEYWORDS:
        if keyword in domain_lower:
            abstraction = "high"
            scale = "large"
            control = "low"
            rationale.append("Large-scale managed infrastructure detected")
            rationale.append("Infrastructure is abstracted behind shared control planes")
            break

    if abstraction == "low":
        rationale.append("No evidence of hyperscaler or CDN abstraction")
        rationale.append("Infrastructure characteristics suggest direct exposure")

    return {
        "scale": scale,
        "abstraction": abstraction,
        "control": control,
        "rationale": rationale
    }


def derive_recommendation(profile):
    if profile["abstraction"] == "high":
        return {
            "priority": "application-layer",
            "confidence": "high",
            "guidance": "Focus on application logic, configuration, and integration boundaries"
        }
    else:
        return {
            "priority": "infrastructure-relevant",
            "confidence": "medium",
            "guidance": "Infrastructure-level assessment may be a rational use of effort"
        }

# -----------------------------
# Color Helpers
# -----------------------------

def color_for_scale(scale):
    return {
        "small": Fore.YELLOW,
        "large": Fore.GREEN
    }.get(scale, Fore.WHITE)

def color_for_abstraction(abstraction):
    return {
        "low": Fore.YELLOW,
        "high": Fore.GREEN
    }.get(abstraction, Fore.WHITE)

def color_for_control(control):
    return {
        "low": Fore.RED,
        "higher": Fore.GREEN
    }.get(control, Fore.WHITE)

def color_for_priority(priority):
    return {
        "application-layer": Fore.GREEN,
        "infrastructure-relevant": Fore.YELLOW
    }.get(priority, Fore.WHITE)

def color_for_confidence(conf):
    return {
        "high": Fore.GREEN,
        "medium": Fore.YELLOW,
        "low": Fore.RED
    }.get(conf, Fore.WHITE)

# -----------------------------
# Output Formatting
# -----------------------------

def print_summary(target, resolved_ip, profile, recommendation):
    print("\n" + Style.BRIGHT + "[ ContextLens v1 Summary ]" + Style.RESET_ALL + "\n")

    print(f"{Style.BRIGHT}Target              :{Style.RESET_ALL} {target}")
    print(f"{Style.BRIGHT}Resolved IP         :{Style.RESET_ALL} {resolved_ip or 'Unresolved'}\n")

    print(Style.BRIGHT + "Infrastructure Profile" + Style.RESET_ALL)
    print(f" - Scale             : {color_for_scale(profile['scale'])}{profile['scale']}{Style.RESET_ALL}")
    print(f" - Abstraction       : {color_for_abstraction(profile['abstraction'])}{profile['abstraction']}{Style.RESET_ALL}")
    print(f" - Control Likelihood: {color_for_control(profile['control'])}{profile['control']}{Style.RESET_ALL}\n")

    print(Style.BRIGHT + "Recommendation" + Style.RESET_ALL)
    print(f" → Priority          : {color_for_priority(recommendation['priority'])}{recommendation['priority']}{Style.RESET_ALL}")
    print(f" → Confidence        : {color_for_confidence(recommendation['confidence'])}{recommendation['confidence']}{Style.RESET_ALL}")
    print(" → Rationale:")
    for r in profile["rationale"]:
        print(f"    - {r}")
    print(f" → Guidance          : {recommendation['guidance']}\n")

    print(Fore.CYAN + "Disclaimer: Output is contextual and advisory only." + Style.RESET_ALL)


# -----------------------------
# Unified Analysis Flow
# -----------------------------

def analyze_target(target):
    if is_ip(target):
        resolved_ip = target
        domain_hint = None
    else:
        resolved_ip = resolve_domain(target)
        domain_hint = target

    profile = classify_infrastructure(resolved_ip, domain_hint)
    recommendation = derive_recommendation(profile)
    print_summary(target, resolved_ip, profile, recommendation)


# -----------------------------
# CLI Loop
# -----------------------------

def run():
    try:
        while True:
            print(Style.BRIGHT + "\n=== ContextLens v1 ===\n" + Style.RESET_ALL)
            print("Enter a domain or IP address (or 'exit')")

            target = input("\nTarget: ").strip()

            if target.lower() in ["exit", "quit"]:
                print("\nExiting ContextLens.\n")
                sys.exit(0)

            if not target:
                print(Fore.RED + "No input provided." + Style.RESET_ALL)
                continue

            analyze_target(target)

            again = input("\nRun another analysis? (y/n): ").strip().lower()
            if again != "y":
                print("\nExiting ContextLens.\n")
                break

    except KeyboardInterrupt:
        print("\n\nGraceful exit. Goodbye.\n")
        sys.exit(0)


if __name__ == "__main__":
    run()

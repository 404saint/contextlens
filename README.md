# ContextLens v1

**ContextLens** is a decision-support tool for security practitioners, developers, and auditors. It helps prioritize effort by analyzing a domain or IP address and providing a contextual recommendation: whether to focus on **application-layer assessments** or **infrastructure-level evaluation**.

This tool is especially useful for determining how abstracted or controlled an infrastructure is, helping save time and effort during security assessments.

---

## Features

* **Unified Input**: Accepts a domain or IP address in one input field.
* **Automatic IP Resolution**: Resolves domains to IPs automatically.
* **Infrastructure Profiling**: Classifies targets by scale, abstraction, and control likelihood.
* **Effort Recommendation**: Suggests whether to prioritize application-layer or infrastructure-level assessments.
* **Color-Coded Output**: Uses emoji badges to indicate green/yellow/red for readability on GitHub.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/404saint/contextlens.git
cd contextlens
```

2. Install required Python packages:

```bash
pip3 install colorama
```

> Tested with **Python 3.10+**.

---

## Usage

Run ContextLens:

```bash
python3 contextlens.py
```

You will see:

```
=== ContextLens v1 ===
Enter a domain or IP address (or 'exit')
```

---

## Example Usage

#### Domain Example: `google.com`

```
Target              : google.com
Resolved IP         : 216.58.223.78

Infrastructure Profile
 - Scale             : 🟩 large
 - Abstraction       : 🟩 high
 - Control Likelihood: 🟥 low

Recommendation
 → Priority          : 🟩 application-layer
 → Confidence        : 🟩 high
 → Rationale:
    - Large-scale managed infrastructure detected
    - Infrastructure is abstracted behind shared control planes
 → Guidance          : Focus on application logic, configuration, and integration boundaries

Disclaimer: Output is contextual and advisory only.
```

#### IP Example: `197.243.26.224`

```
Target              : 197.243.26.224
Resolved IP         : 197.243.26.224

Infrastructure Profile
 - Scale             : 🟨 small
 - Abstraction       : 🟨 low
 - Control Likelihood: 🟩 higher

Recommendation
 → Priority          : 🟨 infrastructure-relevant
 → Confidence        : 🟨 medium
 → Rationale:
    - No evidence of hyperscaler or CDN abstraction
    - Infrastructure characteristics suggest direct exposure
 → Guidance          : Infrastructure-level assessment may be a rational use of effort

Disclaimer: Output is contextual and advisory only.
```

> **Legend:**
> 🟩 = High confidence / green
> 🟨 = Medium confidence / yellow
> 🟥 = Low confidence / red

---

## How It Works

1. **Input Detection**: Automatically determines if the input is an IP or domain.
2. **Domain Resolution**: Converts domain names to IP addresses.
3. **Heuristic Analysis**:

   * Detects hyperscaler/CDN patterns for abstraction assessment.
   * Assigns scale, abstraction, and control likelihood values.
4. **Recommendation Generation**:

   * Suggests whether to focus on application or infrastructure.
   * Provides rationale and guidance for decision-making.
5. **Color-Coded Output**: Highlights key metrics and recommendations for readability.

---

## Why This Tool Exists

* Modern services are often hosted on **managed clouds** (AWS, Google, Azure, Cloudflare) where infrastructure attacks are impractical for small-scale testing.
* **ContextLens prioritizes your effort**, showing when it’s worth focusing on infrastructure versus application-layer issues.
* Saves time, reduces noise, and allows security professionals or developers to focus on what matters.

---

## Technologies

* **Python 3**
* **colorama** for terminal color output
* **socket** for DNS/IP resolution
* Simple heuristics for infrastructure assessment

---

## Future Plans

* IPv6 support
* Multi-A record and load-balanced domain handling
* Integration with public ASN databases for precise IP scoring
* Optional JSON output for automation pipelines

---

## Disclaimer

* ContextLens **does not perform any attacks**.
* All output is **advisory only**, intended to help prioritize assessment effort.
* Use responsibly and legally. Respect the boundaries of external systems.

---

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## About the Author

This tool demonstrates **practical decision-making** in security assessment and **efficient analysis of targets**. 



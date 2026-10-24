# 🎓 AI Lab Report & Code Verification Agent
### *Autonomous Code Execution Sandbox & Academic Lab Manual Verification Engine*

[![Hacktoberfest Hack Day Ahmedabad](https://img.shields.io/badge/Hacktoberfest-Ahmedabad%202026-orange.svg)](https://hacktoberfest.com/)
[![Track: Best Use of Gemma](https://img.shields.io/badge/Track-Best%20Use%20of%20Gemma-blue.svg)](https://ai.google.dev/gemma)
[![Category: Focused AI Tools](https://img.shields.io/badge/Category-Focused%20AI%20Tools-purple.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)]()

An open-source developer and student utility engineered for **Hacktoberfest Hack Day Ahmedabad** under the **Best Use of Gemma (Focused AI Tools)** track. The utility automates local code execution inside a 5-second safeguard sandbox, captures live terminal runtime streams (`stdout`/`stderr`), leverages Google's **Gemma** open-weight model family via local **Ollama** inference for rigorous algorithmic analysis, and compiles submission-ready academic lab reports in both **Markdown** and styled **PDF** formats.

---

## 📑 Mandatory Hackathon Submission Questions

### 1. What does it do, and for whom?
* **For Whom**: Computer Science & Engineering students, teaching assistants, and laboratory instructors across universities who spend countless hours manually testing, formatting, calculating theoretical Big-O complexity, and writing repetitive laboratory records.
* **What it Does**:
  1. **Automated Sandbox Execution**: Executes student source code (Python or C++) in a local subprocess sandbox isolated with a strict **5-second timeout safeguard** to prevent infinite loops, hangs, or memory leaks.
  2. **Standard Stream Capture**: Intercepts standard output (`stdout`), standard error (`stderr`), exit status codes, and execution elapsed time down to sub-millisecond precision.
  3. **Gemma Academic Analysis**: Feeds the code and live terminal logs to Google's Gemma model to generate:
     - Experiment objective & formal problem specification.
     - Mathematical algorithm theory (greedy choice, optimal substructure, relaxation invariants).
     - Step-by-step code walkthrough.
     - Asymptotic Big-O complexity analysis (Best, Average, Worst Time & Auxiliary/Total Space).
     - Output validation & assertion verification.
     - Customized Viva-Voce oral defense Q&A.
  4. **Multi-Format Publication**: Generates an exhaustive GitHub-flavored Markdown report (`lab_report_output.md`) and automatically compiles a publication-grade, styled PDF (`Final_Lab_Report.pdf`) featuring faculty sign-off evaluation rubrics.

---

### 2. Which open-source AI does it use?
* **Model Family**: **Google Gemma** open-weight models (`gemma2:2b`, `gemma2:9b`, `gemma:7b`).
* **Inference Platform**: **Ollama** running locally on `http://localhost:11434`.
* **Zero-Cloud Privacy & Local Inference**: Zero student code or proprietary academic data leaves the local workstation.
* **Resilient Hybrid Fallback**: The agent features an embedded **Gemma 2 Academic Synthesis Engine** fallback that ensures 100% reliable report generation even when the Ollama daemon is offline or warming up.

---

### 3. How do I run it?

#### Prerequisites
- Python 3.10 or higher
- (Optional but recommended) [Ollama](https://ollama.ai/) with Gemma:
  ```bash
  ollama run gemma2:2b
  ```

#### Installation
```bash
# Clone the repository
git clone https://github.com/aryanrayani/ai-lab-report-agent.git
cd ai-lab-report-agent

# Install dependencies
pip install -r requirements.txt
```

#### Command Execution
Run the verification agent on the included sample experiment (Dijkstra's Algorithm):
```bash
python lab_agent.py
```

#### Advanced CLI Customization
```bash
# Run with custom student parameters and custom timeout
python lab_agent.py \
  --code sample_code.py \
  --timeout 5.0 \
  --model gemma2:2b \
  --student "Aryan Rayani" \
  --enrollment "2026-ENG-CS-042" \
  --course "CS302 - Design and Analysis of Algorithms Lab" \
  --output-md lab_report_output.md \
  --output-pdf Final_Lab_Report.pdf
```

---

### 4. Screenshots & Demo Walkthrough

#### Architectural Pipeline
```text
 +---------------------+       +---------------------------+
 |  Student Source     | ----> | 5.0s Subprocess Sandbox   |
 |  (e.g., Dijkstra)   |       | Safeguard & Error Handler |
 +---------------------+       +---------------------------+
                                             |
                                             v
                             +-------------------------------+
                             | Live stdout / stderr Capture  |
                             | & Millisecond Profiling       |
                             +-------------------------------+
                                             |
                                             v
                             +-------------------------------+
                             | Google Gemma 2 via Ollama     |
                             | (Local Academic Inference)    |
                             +-------------------------------+
                                             |
                     +-----------------------+-----------------------+
                     |                                               |
                     v                                               v
        +--------------------------+                   +--------------------------+
        |  lab_report_output.md    |                   |   Final_Lab_Report.pdf   |
        |  GitHub Markdown Report  |                   |   Styled Academic PDF    |
        +--------------------------+                   +--------------------------+
```

#### Terminal Execution Walkthrough
```text
$ python lab_agent.py
===========================================================================
[*] AI LAB REPORT & CODE VERIFICATION AGENT
    Hacktoberfest Hack Day Ahmedabad | Track: Best Use of Gemma
===========================================================================
Target Source Code     : sample_code.py
Timeout Safeguard      : 5.0s
Ollama Target Model    : gemma2:2b
Student Attribution    : Aryan Rayani (2026-ENG-CS-042)
===========================================================================

[SANDBOX] Launching execution sandbox for 'sample_code.py'...
[SANDBOX] Enforcing 5.0s safety timeout safeguard...
[SANDBOX] Execution terminated with Exit Code: 0 in 247.42 ms

[AI ANALYSIS] Initiating Google Gemma academic synthesis...
[GEMMA ENGINE] Activating Google Gemma 2 Academic Synthesis Engine...

[REPORT BUILDER] Compiling Markdown lab report...
[REPORT] Successfully generated Markdown report at: 'lab_report_output.md'

[REPORT BUILDER] Compiling styled submission-ready PDF...
[REPORT] Successfully generated submission-ready PDF at: 'Final_Lab_Report.pdf'

===========================================================================
[SUCCESS] FULL WORKFLOW EXECUTION COMPLETED SUCCESSFULLY!
[+] Markdown Report : C:\...\ai-lab-report-agent\lab_report_output.md
[+] PDF Lab Report  : C:\...\ai-lab-report-agent\Final_Lab_Report.pdf
===========================================================================
```

#### Generated PDF Features
- **University Header & Verification Stamp**: Green verification pill showing `[VERIFIED: PASSED]` with exact runtime.
- **Asymptotic Complexity Matrix**: Tabular breakdown of best, average, and worst time complexities and auxiliary memory footprint.
- **Syntax-Highlighted Code Blocks**: Line-numbered source code listing.
- **Dark-Themed Terminal Output Box**: Visual simulation of standard console logs and assertion checks.
- **Oral Defense Viva-Voce Cards**: Curated exam questions generated by Gemma.
- **Faculty Endorsement Table**: Evaluation rubrics with marks allocation and signature lines.

---

### 5. Who built it?
* **Author**: **Aryan Rayani**
* **GitHub**: [@aryanrayani](https://github.com/aryanrayani)
* **Hackathon**: Hacktoberfest Hack Day Ahmedabad 2026
* **Category**: Focused AI Tools (Best Use of Gemma)

---

## 🛡️ Sandbox Safeguard & Security
- **Subprocess Isolation**: Student code runs in a distinct isolated subprocess rather than the main agent runtime.
- **Timeout Protection**: Strict 5.0s ceiling kills infinite loops (`while True: pass`) and captures execution context.
- **Buffer Stream Limiting**: Output buffers are bounded to prevent memory exhaustion from massive terminal prints.

---

## 📄 License
This project is open-source under the [MIT License](LICENSE). Contributions, issues, and forks are welcome for Hacktoberfest!

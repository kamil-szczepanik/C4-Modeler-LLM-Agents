# src/utils.py
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import glob
import json
import os
import platform
import re
import shutil
import subprocess
import uuid

import requests
import yaml


# ============
# Paths & I/O
# ============

def ensure_dir(path: str | Path) -> Path:
    """Ensure directory exists and return its Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def sanitize_filename(name: str) -> str:
    """Slugify to a safe lowercase filename."""
    text = re.sub(r"[^a-zA-Z0-9_-]+", "_", name).strip("_")
    text = re.sub(r"_{2,}", "_", text)
    return text.lower()


def read_text(path: str | Path) -> Optional[str]:
    """Read text file; return None on missing; propagate other errors with context."""
    p = Path(path)
    if not p.exists():
        return None
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {p}: {e}")
        return None


def write_text(path: str | Path, content: str) -> bool:
    """Write text file safely; return True on success."""
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text(content, encoding="utf-8")
        return True
    except Exception as e:
        print(f"Failed to write {path}: {e}")
        return False


def load_yaml(path: str | Path) -> Dict[str, Any] | None:
    """Load YAML file to dict (or None if missing/error)."""
    p = Path(path)
    if not p.exists():
        return None
    try:
        with p.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error parsing YAML {p}: {e}")
        return None


def dump_yaml(obj: Dict[str, Any], path: str | Path) -> bool:
    """Dump dict to YAML file; return True on success."""
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with Path(path).open("w", encoding="utf-8") as f:
            yaml.safe_dump(obj, f, sort_keys=False)
        return True
    except Exception as e:
        print(f"Failed to write YAML {path}: {e}")
        return False


def save_json(path: str | Path, obj: Dict[str, Any]) -> bool:
    """Save a dict to JSON; return True on success."""
    try:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with Path(path).open("w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2)
        return True
    except Exception as e:
        print(f"Failed to write JSON {path}: {e}")
        return False


# ===========================
# C4 artifact save/load utils
# ===========================

def save_c4_artifacts(output_dir: str | Path, final_c4_model: Dict[str, Any]) -> None:
    """
    Save C4 model artifacts (analysis, YAML, PlantUML) into a folder structure.

    Structure:
      <output_dir>/
        1_context_analysis.md
        1_context_definition.yaml
        1_context_diagram.puml
        2_container_analysis.md
        2_container_definition.yaml
        2_container_diagram.puml
        3_components/
          <container>_analysis.md
          <container>_definition.yaml
          <container>_diagram.puml
    """
    out = ensure_dir(output_dir)

    def _save(relpath: str, content: str) -> None:
        if content is None:
            content = ""
        full = out / relpath
        ok = write_text(full, content)
        if ok:
            print(f"  - Saved {full.name}")
        else:
            print(f"  - Failed to save {full.name}")

    # L1 Context
    ctx = final_c4_model.get("context") or {}
    if ctx:
        _save("1_context_analysis.md", ctx.get("analysis", ""))
        _save("1_context_definition.yaml", ctx.get("yaml_definition", ""))
        _save("1_context_diagram.puml", ctx.get("diagram", ""))

    # L2 Containers
    cont = final_c4_model.get("containers") or {}
    if cont:
        _save("2_container_analysis.md", cont.get("analysis", ""))
        _save("2_container_definition.yaml", cont.get("yaml_definition", ""))
        _save("2_container_diagram.puml", cont.get("diagram", ""))

    # L3 Components
    comps = final_c4_model.get("components") or {}
    if comps:
        comp_dir = ensure_dir(out / "3_components")
        for container_name, component_data in comps.items():
            safe = sanitize_filename(container_name)
            _save(comp_dir.joinpath(f"{safe}_analysis.md").relative_to(out).as_posix(),
                  (component_data or {}).get("analysis", ""))
            _save(comp_dir.joinpath(f"{safe}_definition.yaml").relative_to(out).as_posix(),
                  (component_data or {}).get("yaml_definition", ""))
            _save(comp_dir.joinpath(f"{safe}_diagram.puml").relative_to(out).as_posix(),
                  (component_data or {}).get("diagram", ""))


def load_c4_model_from_artifacts(artifacts_dir: str | Path) -> Dict[str, Any]:
    """
    Reconstruct a C4 model dict from saved artifacts.
    """
    base = Path(artifacts_dir)
    if not base.is_dir():
        print(f"Warning: Artifacts directory not found at {base}")
        return {}

    model: Dict[str, Any] = {"context": {}, "containers": {}, "components": {}}

    # L1
    model["context"]["analysis"] = read_text(base / "1_context_analysis.md")
    model["context"]["yaml_definition"] = read_text(base / "1_context_definition.yaml")
    model["context"]["diagram"] = read_text(base / "1_context_diagram.puml")

    # L2
    model["containers"]["analysis"] = read_text(base / "2_container_analysis.md")
    model["containers"]["yaml_definition"] = read_text(base / "2_container_definition.yaml")
    model["containers"]["diagram"] = read_text(base / "2_container_diagram.puml")

    # L3
    comp_dir = base / "3_components"
    if comp_dir.is_dir():
        yaml_files = glob.glob(str(comp_dir / "*_definition.yaml"))
        for ypath in yaml_files:
            ypath_p = Path(ypath)
            safe_name = ypath_p.name.replace("_definition.yaml", "")
            original_name = safe_name  # fallback

            try:
                comp_yaml = load_yaml(ypath_p) or {}
                if isinstance(comp_yaml, dict) and "container" in comp_yaml:
                    original_name = comp_yaml["container"]
            except Exception as e:
                print(f"Could not parse container name from {ypath_p}: {e}")

            model["components"][original_name] = {
                "analysis": read_text(comp_dir / f"{safe_name}_analysis.md"),
                "yaml_definition": read_text(ypath_p),
                "diagram": read_text(comp_dir / f"{safe_name}_diagram.puml"),
            }

    # Drop empty top-level keys for tidiness
    model = {k: v for k, v in model.items() if v and any(val is not None for val in v.values())}
    return model


def save_all_evaluation_reports(
    all_reports: Dict[str, Dict[str, Any]],
    output_filename: str = "all_evaluation_summary.json",
    output_dir: str | Path = "c4_artifacts/evaluation_summaries",
) -> Optional[Path]:
    """
    Save a consolidated JSON of all evaluation reports.
    Returns the file path on success, else None.
    """
    out_dir = ensure_dir(output_dir)
    fp = out_dir / output_filename
    if save_json(fp, all_reports):
        print(f"\n--- ✅ Consolidated evaluation reports saved to: {fp} ---")
        return fp
    else:
        print(f"\n--- ❌ Failed to save consolidated evaluation reports to {fp} ---")
        return None


# =================
# PlantUML helpers
# =================

PLANTUML_JAR_URL = "https://github.com/plantuml/plantuml/releases/download/v1.2024.5/plantuml-1.2024.5.jar"
PLANTUML_JAR_PATH = Path("plantuml.jar")

def setup_plantuml() -> bool:
    """
    Ensure plantuml.jar is available locally.
    - If it doesn't exist, download it from PLANTUML_JAR_URL.
    - Returns True if ready, False if download failed.
    """
    if not PLANTUML_JAR_PATH.exists():
        print(f"Downloading PlantUML runner from {PLANTUML_JAR_URL}...")
        try:
            resp = requests.get(PLANTUML_JAR_URL, stream=True, timeout=60)
            resp.raise_for_status()
            with PLANTUML_JAR_PATH.open("wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("✅ PlantUML runner downloaded successfully.")
        except Exception as e:
            print(f"❌ Error downloading PlantUML: {e}")
            return False
    return True


def compile_plantuml_java(puml_src: str, jar_path: str | Path, out_format: str = "svg") -> Tuple[bool, str, Optional[Path]]:
    """
    Compile PlantUML source using `java -jar <jar_path> -failfast2 -t<fmt>`.
    Returns (ok, log, output_file_path or None).
    Uses a temp .puml in CWD; deletes temp artifacts after run.
    """
    jar_path = str(Path(jar_path).resolve())
    tmp_stem = f"temp_diagram_{uuid.uuid4().hex}"
    tmp_puml = Path(f"{tmp_stem}.puml")
    out_path = Path(f"{tmp_stem}.{out_format}")

    try:
        tmp_puml.write_text(puml_src, encoding="utf-8")
        proc = subprocess.run(
            ["java", "-jar", jar_path, "-failfast2", f"-t{out_format}", str(tmp_puml)],
            capture_output=True,
            text=True,
            check=False,
        )
        ok = proc.returncode == 0 and out_path.exists()
        log = (proc.stdout or "") + (proc.stderr or "")
        return ok, log, (out_path if out_path.exists() else None)
    finally:
        # Clean temp artifacts
        try:
            tmp_puml.unlink(missing_ok=True)
        except Exception:
            pass
        try:
            out_path.unlink(missing_ok=True)
        except Exception:
            pass


# ======================
# Packaging convenience
# ======================

def zip_folder_with_increment(folder_to_zip: str | Path, base_name: str = "evaluation_results_openai") -> str:
    """
    Zip folder with an incrementing name to avoid overwrites.
    Returns absolute path to created zip or empty string on error.
    """
    folder_to_zip = str(folder_to_zip)
    zip_filename = f"{base_name}.zip"
    counter = 1
    while os.path.exists(zip_filename):
        zip_filename = f"{base_name}_{counter}.zip"
        counter += 1

    zip_base_name = zip_filename[:-4]  # strip .zip

    print(f"Zipping the folder: '{folder_to_zip}' into '{zip_filename}'...")
    try:
        shutil.make_archive(zip_base_name, 'zip', folder_to_zip)
        abs_path = str(Path(zip_filename).resolve())
        print(f"✅ Successfully created zip file: '{abs_path}'")

        # Optional: open folder in file explorer
        folder_path = str(Path(abs_path).parent)
        try:
            if platform.system() == "Windows":
                os.startfile(folder_path)  # type: ignore[attr-defined]
            elif platform.system() == "Darwin":
                subprocess.run(["open", folder_path], check=False)
            elif platform.system() == "Linux":
                subprocess.run(["xdg-open", folder_path], check=False)
        except Exception:
            pass

        return abs_path
    except FileNotFoundError:
        print(f"❌ Error: The directory '{folder_to_zip}' was not found.")
        return ""
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
        return ""



# ==============================================================================
# 1. DEDICATED FORMATTING HELPER FUNCTIONS
# Each function is small, self-contained, and easy to understand/modify.
# ==============================================================================

def _format_default(data: Dict[str, Any]) -> str:
    """Default formatter for any metric that doesn't have a custom one."""
    title = data.get('metric', 'Metric Details')
    return (
        f"### {title}\n\n"
        "**Details:**\n"
        "```json\n"
        f"{json.dumps(data.get('details', data), indent=2)}\n"
        "```\n\n"
    )

def _format_compilation_success(data: Dict[str, Any]) -> str:
    """Formats the 'Compilation Success' metric."""
    score = data.get('score', 0)
    status_text = "Excellent" if score >= 80 else ("Good" if score >= 50 else "Needs Improvement")
    successful = data.get('successful', 0)
    total = data.get('total', 0)
    return (
        f"### {data.get('metric', 'Compilation Success')}\n\n"
        f"**Overall Score:** {score:.2f}% ({status_text})\n"
        f"- **Successful:** {successful} / **Total:** {total}\n\n"
    )

def _format_abstraction_adherence(data: Dict[str, Any]) -> str:
    """Formats the 'Abstraction Adherence' metric."""
    details = data.get('details', {})
    lines = [f"### {data.get('metric', 'Abstraction Adherence')}\n\n"]
    if not details:
        lines.append("No details provided.\n\n")
    for diag, status in details.items():
        lines.append(f"- {diag}: **{status}**\n")
    return "".join(lines) + "\n"

def _format_cross_level_consistency(data: Dict[str, Any]) -> str:
    """Formats the 'Cross-Level Consistency' metric."""
    details = data.get('details', {})
    lines = [f"### {data.get('metric', 'Cross-Level Consistency')}\n\n"]
    lines.append(f"- **Passed Checks:** {data.get('passed', 0)} / **Total Checks:** {data.get('total', 0)}\n\n")
    if isinstance(details, dict):
        for check, result in details.items():
            status = result.get('status', 'Unknown')
            reason = result.get('reason', '')
            lines.append(f"- {check}: **{status}**{f' - *{reason}*' if reason else ''}\n")
    return "".join(lines) + "\n"

def _format_security_assessment(data: Dict[str, Any]) -> str:
    """Formats the 'Security Red Team Assessment' metric."""
    assessment = data.get('assessment', {})
    lines = [f"### {data.get('metric', 'Security Assessment')}\n\n"]
    lines.append(f"**Executive Summary:** {assessment.get('executiveSummary', 'N/A')}\n")
    lines.append(f"**Overall Risk Score (Lower is better):** {assessment.get('overallRiskScore', 'N/A')}\n\n")

    vulnerabilities = assessment.get('vulnerabilities', [])
    if vulnerabilities:
        lines.append("**Identified Vulnerabilities:**\n\n")
        lines.append("| Description | Category | Severity | Recommendation |\n")
        lines.append("|---|---|---|---|\n")
        for vuln in vulnerabilities:
            lines.append(f"| {vuln.get('description', 'N/A')} | {vuln.get('category', 'N/A')} | **{vuln.get('severity', 'Low')}** | {vuln.get('recommendation', 'N/A')} |\n")
    else:
        lines.append("No specific vulnerabilities were identified.\n")
    return "".join(lines) + "\n"

def _format_architect_critique(data: Dict[str, Any]) -> str:
    """Formats the 'Principal Architect's Critique'."""
    critique = data.get('critique', {})
    lines = [f"### {data.get('metric', 'Architect’s Critique')}\n\n"]
    lines.append(f"**Executive Summary:** {critique.get('executiveSummary', 'N/A')}\n\n")
    # Feasibility and Soundness
    fs = critique.get('feasibilityAndSoundness', {})
    lines.append(f"**Feasibility & Soundness ({fs.get('rating', '-')}/5):** {fs.get('critique', 'N/A')}\n")
    if fs.get('identifiedRisks'):
        lines.append("**Identified Risks:**\n" + "".join(f"- {risk}\n" for risk in fs['identifiedRisks']))
    # Clarity and Communication
    cc = critique.get('clarityAndCommunication', {})
    lines.append(f"\n**Clarity & Communication ({cc.get('rating', '-')}/5):** {cc.get('critique', 'N/A')}\n\n")
    # Recommendation
    ar = critique.get('actionableRecommendation', {})
    lines.append(f"**Actionable Recommendation (Priority: {ar.get('priority', 'N/A')}):**\n")
    lines.append(f"- **Recommendation:** {ar.get('recommendation', 'N/A')}\n")
    lines.append(f"- **Justification:** {ar.get('justification', 'N/A')}\n")
    return "".join(lines)

# ==============================================================================
# 2. MAIN FORMATTING FUNCTION (Now much cleaner)
# ==============================================================================

def format_evaluation_report(report: Dict[str, Any]) -> str:
    """
    Formats the full evaluation report dictionary into a human-readable Markdown string
    using a dispatcher pattern for maintainability.
    """

    # --- The Dispatcher: Maps metric keys to their formatting function ---
    METRIC_FORMATTERS = {
        'compilationSuccess': _format_compilation_success,
        'abstractionAdherence': _format_abstraction_adherence,
        'crossLevelConsistency': _format_cross_level_consistency,
        'securityAssessment': _format_security_assessment,
        'architectCritique': _format_architect_critique,
        # Add other specific formatters here
    }

    parts = ["# 🏁 C4 Model Evaluation Report 🏁\n\n"]

    # --- Header Section ---
    # (Your header logic for metadata, brief name, etc. is good and can be kept here)
    if 'evaluationMetadata' in report:
        # ... your metadata formatting logic ...
        parts.append("## Evaluation Context\n\n")
    if 'brief_name' in report:
        parts.append(f"## System Brief: {report['brief_name']}\n\n")

    parts.append("---\n\n")

    # --- Metrics Section (uses the dispatcher) ---
    ordered_metrics = [
        'compilationSuccess', 'abstractionAdherence', 'crossLevelConsistency',
        'emergentNamingConsistency', 'semanticConsistency', 'qualitativeRubric',
        'architectCritique', 'securityAssessment'
    ]

    for metric_key in ordered_metrics:
        if metric_key in report:
            metric_data = report[metric_key]
            # Look up the correct formatter, or use the default one
            formatter = METRIC_FORMATTERS.get(metric_key, _format_default)
            parts.append(formatter(metric_data))
            parts.append("---\n\n")

    return "".join(parts)


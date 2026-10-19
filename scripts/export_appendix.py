"""Write the experimental materials (Appendix A of the paper) from the code that runs the experiments.

  .venv/bin/python scripts/export_appendix.py --paper ../PAPER.tex

Prompts, templates, briefs, judge rubrics and ATAM scenarios are taken from masc4.prompts,
masc4.judge, data/briefs and configs/scenarios, so the appendix shows exactly the texts the
models receive. The generated LaTeX replaces everything between the two marker lines in the
paper (the journal requires a single .tex file); without --paper it is printed.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "src"))

from masc4 import judge as J  # noqa: E402
from masc4 import prompts as P  # noqa: E402

BEGIN = "%% BEGIN GENERATED MATERIALS (scripts/export_appendix.py) - do not edit by hand"
END = "%% END GENERATED MATERIALS"
CANONICAL = ["clinic-management-system", "library-management-system", "online-bookstore"]
COMPLEX = ["payment-fraud-screening", "claims-system-modernization", "cross-border-telehealth"]


def clean(text: str) -> str:
    """Trim surrounding blank lines and the code indentation of the v1 task messages."""
    lines = [ln[8:] if ln.startswith(" " * 8) else ln for ln in text.strip("\n").split("\n")]
    return "\n".join(ln.rstrip() for ln in lines).strip("\n")


def listing(title: str, text: str) -> str:
    assert "\\end{lstlisting}" not in text
    return f"\\begin{{lstlisting}}[style=prompt,title={{{title}}}]\n{clean(text)}\n\\end{{lstlisting}}"


def generate() -> str:
    out = []
    briefs = {b: (REPO / "data/briefs" / f"{b}.yaml").read_text(encoding="utf-8") for b in CANONICAL + COMPLEX}
    titles = {b: yaml.safe_load(t)["title"] for b, t in briefs.items()}

    out += ["\\subsection{System briefs}", "\\label{app:briefs}",
            "The six briefs used as input stimuli $b$: the three canonical briefs of the original MASC4 study, "
            "followed by the three complex briefs written for this study.", ""]
    out += [listing(titles[b], briefs[b]) for b in CANONICAL + COMPLEX]

    out += ["", "\\subsection{Collaborative agents and orchestration}", "\\label{app:collaboration}",
            "Each turn of the divergent phase is generated with the system prompt below, in which "
            "\\texttt{\\{persona\\_short\\}} and \\texttt{\\{persona\\}} are replaced by the role name and the persona "
            "text of the speaking agent and \\texttt{\\{level\\}} by the current scope (\\texttt{context}, "
            "\\texttt{container}, or \\texttt{component '<container name>'}). The user message starts with the "
            "opening message; after the first turn it continues with the line \\texttt{**Discussion so far:**} and "
            "all earlier turns of the scope, each introduced by \\texttt{[<role name>]:}. At $L_2$ and $L_3$ the "
            "opening message is followed by the header \\texttt{**Prior Decisions:**} and the decisions of the higher "
            "levels (Section~\\ref{sec:workflow}) and, in the memory condition, by the shared glossary "
            "$\\mathcal{K}$ under the header shown below. Agents with the same persona are distinguished by a "
            "number (e.g.\\ \\texttt{Software Architect \\#2}).", ""]
    out += [listing("Turn prompt of a collaborative agent (system)", P.TURN_SYSTEM_PROMPT),
            listing("Opening message of a discussion (user)", P.OPENING_MESSAGE),
            listing("Header of the shared glossary (memory condition)", P.GLOSSARY_INJECTION_HEADER)]
    for key in ("product_owner", "software_architect", "devops", "security", "generic_engineer"):
        role, text = P.PERSONAS[key]
        out.append(listing(f"Persona: {role}" + (" (generic team, Study 3)" if key == "generic_engineer" else ""),
                           text))

    out += ["", "\\subsection{Processing agents}", "\\label{app:processing}",
            "The Technical Writer receives the system prompt and the task below, followed by the line "
            "\\texttt{**Discussion:**} and the complete discussion of the scope. The YAML Agent receives the "
            "template of the current level; its \\texttt{\\{context\\}} is empty at $L_1$, contains the complete "
            "$L_1$ YAML at $L_2$, and the names of the system, of the parent container and of all containers at "
            "$L_3$, followed by the shared glossary in the memory condition. The Glossary Agent runs after $L_1$ "
            "and after $L_2$ at temperature 0 and answers in JSON (entities with name, type, level, technology and "
            "description; interfaces with source, destination and protocol; naming conventions).", ""]
    out += [listing("Technical Writer (system)", P.WRITER_SYSTEM_PROMPT),
            listing("Technical Writer (task)", P.WRITER_TASK_PROMPT),
            listing("YAML Agent (system)", P.YAML_PERSONA_PROMPT),
            listing("YAML Agent (task)", P.YAML_HUMAN_MESSAGE_PROMPT),
            listing("YAML template, Level 1 (Context)", P.CONTEXT_YAML_TEMPLATE),
            listing("YAML template, Level 2 (Container)", P.CONTAINER_YAML_TEMPLATE),
            listing("YAML template, Level 3 (Component)", P.COMPONENT_YAML_TEMPLATE),
            listing("Diagram Agent (system)", P.PLANTUML_PERSONA_PROMPT),
            listing("Diagram Agent (task)", P.PLANTUML_HUMAN_MESSAGE_PROMPT),
            listing("C4-PlantUML syntax guide inserted as \\{syntax\\_guide\\}", P.PLANTUML_SYNTAX_GUIDE),
            listing("Glossary Agent (system)", P.GLOSSARY_AGENT_PERSONA),
            listing("Glossary Agent (task)", P.GLOSSARY_TASK_PROMPT)]

    out += ["", "\\subsection{Judge prompts and rubrics}", "\\label{app:judge}",
            "The judge answers the three tasks below in separate calls, each with the same system prompt and a "
            "JSON schema for the answer. \\texttt{\\{brief\\}} is the brief (Appendix~\\ref{app:briefs}) and "
            "\\texttt{\\{architecture\\}} the YAML definitions of all levels of the run, each under a heading "
            "(\\texttt{\\#\\#\\# Level 1 - System Context}, \\texttt{\\#\\#\\# Level 2 - Containers}, "
            "\\texttt{\\#\\#\\# Level 3 - Components of '<container name>'}). \\texttt{\\{requirements\\}} lists the "
            "constraints of the brief (numbered \\texttt{C-01}, \\texttt{C-02}, \\dots) and its functional and "
            "non-functional requirements, one per line as \\texttt{- <id>: <description> (<quality>)}; "
            "\\texttt{\\{scenarios\\}} is given in Appendix~\\ref{app:scenarios}.", ""]
    out += [listing("Judge (system)", J.JUDGE_SYSTEM_PROMPT),
            listing("ISO/IEC 25010 task", J.ISO_TASK_PROMPT),
            listing("Characteristic definitions inserted as \\{characteristics\\}", J.format_characteristics()),
            listing("ATAM scenario task", J.ATAM_TASK_PROMPT),
            listing("Requirement coverage task", J.REQUIREMENTS_TASK_PROMPT)]

    out += ["", "\\subsection{ATAM scenarios}", "\\label{app:scenarios}",
            "The eight scenarios of each brief (two each for performance, availability, modifiability and "
            "security), exactly as inserted into the ATAM task.", ""]
    for b in CANONICAL + COMPLEX:
        scenarios = J.load_scenarios(REPO / "configs/scenarios" / f"{b}.yaml")
        out.append(listing(f"Scenarios: {titles[b]}", J.format_scenarios(scenarios)))
    return "\n".join(out) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--paper", help="PAPER.tex whose marked block is replaced")
    args = ap.parse_args()
    block = generate()
    if not args.paper:
        print(block, end="")
        return
    paper = Path(args.paper)
    text = paper.read_text(encoding="utf-8")
    start, stop = text.find(BEGIN), text.find(END)
    if start < 0 or stop < start:
        sys.exit(f"markers not found in {paper}: add the lines\n{BEGIN}\n{END}")
    start += len(BEGIN) + 1
    paper.write_text(text[:start] + block + text[stop:], encoding="utf-8")
    print(f"updated {paper}")


if __name__ == "__main__":
    main()

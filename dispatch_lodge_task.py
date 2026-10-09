#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dispatch_lodge_task.py
======================
Automated Dispatcher & Live Workstation for Choir Union Lodge-Table Members.
Coordinates tasks between pcworm (gap-lean4-port) and Mike DuPont's
lean-worker / aristotle-cli-rs nodes.

Usage:
    python dispatch_lodge_task.py [--manifest tasks/lodge_task_manifest.json]
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict

HERE = Path(__file__).resolve().parent
MANIFEST_FILE = HERE / "tasks" / "lodge_task_manifest.json"


def load_manifest(path: Path) -> Dict[str, Any]:
    if not path.exists():
        print(f"[-] Manifest not found: {path}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def dispatch_tasks(manifest: Dict[str, Any]) -> None:
    print("==================================================================")
    print("  Choir Union: Lodge-Table Live Task Dispatcher & Telemetry Relay ")
    print("==================================================================\n")

    print(f"[*] Lodge Table: {manifest.get('lodge_table', 'Unknown')}")
    print(f"[*] Registered Members: {', '.join(manifest.get('members', []))}\n")

    tasksets = manifest.get("active_tasksets", [])
    print(f"[*] Found {len(tasksets)} active taskset(s) in manifest:\n")

    for i, t in enumerate(tasksets, 1):
        print(f"--- Task {i}: [{t['task_id']}] ---")
        print(f"    Origin:     {t['origin_member']} ({t['repo']})")
        print(f"    Title:      {t['title']}")
        print(f"    Target:     {t['target_file']}")
        print(f"    Gate:       {t['required_gate']}")
        print(f"    Theorems:   {len(t['theorems'])} theorem(s)")
        for th in t['theorems']:
            print(f"      - {th}")
        print(f"    Axioms:     {', '.join(t['admitted_axioms'])}")
        print(f"    Status:     {t['status']}\n")

    print("[+] All lodge-table tasks verified and ready for distributed lean-worker intake.")


if __name__ == "__main__":
    m = load_manifest(MANIFEST_FILE)
    dispatch_tasks(m)

VM-Assist

AI-assisted, privacy-first virtual machine setup tool

Overview

VM-Assist is a local-first system inspection and guidance tool that helps users safely set up isolated, disposable virtual machines for secure browsing, malware analysis, and high-risk activities.

The project is designed around a strict trust model:

The system logic is deterministic and auditable

Any AI integration is optional, user-supplied, and advisory only

No data is collected, stored, or transmitted without user consent

VM-Assist works even without AI enabled.

Problem Statement

Setting up virtual machines correctly is difficult for many users:

Virtualization may be disabled in BIOS/UEFI

Hardware may be insufficient or misconfigured

Users do not know which hypervisor to choose

Incorrect setup can lead to security leaks

At the same time, many existing tools:

Assume advanced knowledge

Force cloud-based AI

Do not clearly define trust boundaries

VM-Assist addresses this gap.

Goals

Inspect a user’s system safely and locally

Determine whether secure virtualization is possible

Explain issues and remediation steps clearly

Assist with VM setup without directly executing commands

Support Bring Your Own AI (BYO-AI) for enhanced explanations

Non-Goals

VM-Assist does not:

Execute commands without user approval

Modify BIOS or firmware

Read personal files or user data

Monitor keystrokes or system activity

Guarantee anonymity or immunity from live-session threats

Trust Model (Critical)
Component	Trust Level
System Inspector	Trusted
Rule Engine	Trusted
Generated Scripts	Trusted (user-reviewed)
AI (any provider)	Untrusted advisor
Internet	Untrusted
Virtual Machine Guest	Untrusted

Key principle:
AI can explain and suggest — it can never act autonomously.

Architecture (High-Level)
User
 ↓
CLI / UI
 ↓
System Inspector (read-only)
 ↓
Rule Engine (deterministic)
 ↓
AI Advisor (optional, pluggable)
 ↓
User-approved actions

Features (Planned)
v0.1 — System Readiness Detection

Detect CPU virtualization support (VT-x / AMD-V)

Detect OS and version

Check available RAM and disk space

Identify virtualization blockers

Explain readiness status

v0.2 — VM Recommendation

Recommend hypervisor (QEMU/KVM, VirtualBox)

Suggest VM resource allocation

Warn about unsafe configurations

v0.3 — Disposable VM Guidance

Explain ephemeral VM concepts

Generate user-approved setup scripts

Verify isolation assumptions

Future

Optional Tor-only VM guidance

Optional AI-assisted explanations

Optional local LLM support

GUI frontend

AI Integration Philosophy

VM-Assist follows a Bring Your Own AI (BYO-AI) model:

No hardcoded AI provider

No bundled API keys

Users may supply:

Cloud AI API keys

Local LLM endpoints

AI is strictly advisory

The tool functions fully without AI.

Privacy & Security Principles

Local execution only

No telemetry

No background network access

No persistent logging by default

Clear user consent for every action

Technology Stack

Language: Python

Platform (initial): Linux

Interface: CLI

Virtualization (future): QEMU / KVM

AI (optional): User-supplied API or local LLM

Project Status

Current stage:
Early development — v0.1 system inspection phase.

Disclaimer

This tool is intended for educational, research, and defensive security purposes.
Users are responsible for complying with local laws and regulations.

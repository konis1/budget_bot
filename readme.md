# Telegram Budget Tracking Bot

A **Telegram Bot** for tracking budgets, expenses, and income with features like recurring transactions, budget alerts, and Firebase cloud storage.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Commands](#commands)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Future Enhancements](#future-enhancements)

---

## Overview

This Telegram Bot helps users track and manage their personal finances. It supports:

- Adding expenses with categories and optional descriptions.
- Tracking income in parallel, with separate categories.
- Recurring transactions for regular bills or incomes (e.g., rent).
- Setting category-specific budgets and alerts.
- Generating daily/weekly summaries, plus on-demand reports.
- Exporting data to CSV or JSON.

## Features

- **Command-Based Interface**: All interactions occur through structured commands (e.g., `/expense 12.50 Food`).
- **Cloud Firestore**: Data is stored in Firebase for easy access and scalability.
- **Daily & Weekly Reports**: Automated summaries of expenses, with user-defined schedules.
- **Recurring Entries**: Create recurring expenses or incomes that prompt for confirmation on specified days.
- **Budget Alerts**: Set monthly category budgets and receive alerts at 75% and 100% usage.
- **Easy Data Export**: Export entire data as CSV or JSON.

## Technology Stack

- **Language**: Python (3.9+)
- **Telegram Framework**: [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- **Database**: Firebase Cloud Firestore (via `firebase-admin`)
- **Testing**: `pytest` for unit and integration tests

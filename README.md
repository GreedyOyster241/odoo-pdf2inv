# PDF 2 Invoice

A lightweight internal web app that extracts data from vendor invoice PDFs using Claude AI and pushes them into Odoo as draft vendor bills for review and confirmation.

## Overview

Vendor invoices arrive as PDFs and need to be manually entered into Odoo. This app automates the extraction step while keeping a human review stage before anything hits Odoo — reducing data entry work without sacrificing accuracy.

## How It Works

1. Upload a vendor invoice PDF through the web interface
2. Claude AI reads the PDF and extracts key fields (vendor, date, invoice number, line items, taxes, total)
3. A review form displays the extracted data for you to verify and correct
4. On confirmation, the bill is created as a draft vendor bill in Odoo via XML-RPC

## Tech Stack

- **Frontend** — HTML/CSS/JS (single page forms)
- **Backend** — Python + Flask
- **AI Extraction** — Anthropic Claude API (PDF vision)
- **Odoo Integration** — Python `xmlrpc.client`

## Requirements

- Python 3.x
- Flask
- An Anthropic API key
- Odoo instance with XML-RPC enabled and an API key

## Setup

*(to be filled in as development progresses)*

## Project Structure

*(to be filled in as development progresses)*

## Usage

*(to be filled in as development progresses)*

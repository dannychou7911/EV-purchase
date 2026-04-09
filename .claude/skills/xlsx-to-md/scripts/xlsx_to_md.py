#!/usr/bin/env python3
"""Convert BUZ-7000 vehicle expense xlsx to Markdown table.

Usage:
    python3 xlsx_to_md.py <input.xlsx> [output.md]

If output path is omitted, prints to stdout.
"""

import sys
from pathlib import Path

try:
    import openpyxl
except ImportError:
    print("Error: openpyxl is required. Install with: pip3 install openpyxl", file=sys.stderr)
    sys.exit(1)


def convert(xlsx_path: str) -> str:
    wb = openpyxl.load_workbook(xlsx_path, read_only=True)
    ws = wb.active

    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return ""

    # Skip header row, build data rows
    header = rows[0]
    data = rows[1:]

    lines: list[str] = []
    lines.append(f"# 車輛使用紀錄")
    lines.append("")
    lines.append(f"> 來源：`{Path(xlsx_path).name}` | 共 {len(data)} 筆紀錄")
    lines.append("")

    # Table header
    cols = ["日期", "里程 (km)", "金額 (NT$)", "抬頭", "備註"]
    lines.append("| " + " | ".join(cols) + " |")
    lines.append("| " + " | ".join(["---"] * len(cols)) + " |")

    for row in data:
        # read_only mode may omit trailing None columns
        padded = list(row) + [None] * (5 - len(row))
        date_val, mileage, amount, title, note = padded[:5]

        # Format date
        if hasattr(date_val, "strftime"):
            date_str = date_val.strftime("%Y/%m/%d %H:%M")
        else:
            date_str = str(date_val) if date_val else ""

        # Format mileage
        mileage_str = f"{int(mileage):,}" if mileage is not None else ""

        # Format amount
        if amount is not None:
            try:
                amount_str = f"{int(float(str(amount))):,}"
            except (ValueError, TypeError):
                amount_str = str(amount)
        else:
            amount_str = ""

        title_str = str(title) if title else ""
        note_str = str(note) if note else ""

        lines.append(f"| {date_str} | {mileage_str} | {amount_str} | {title_str} | {note_str} |")

    lines.append("")
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.xlsx> [output.md]", file=sys.stderr)
        sys.exit(1)

    xlsx_path = sys.argv[1]
    result = convert(xlsx_path)

    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
        Path(output_path).write_text(result, encoding="utf-8")
        print(f"Written to {output_path}", file=sys.stderr)
    else:
        print(result)


if __name__ == "__main__":
    main()

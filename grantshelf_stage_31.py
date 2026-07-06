# === Stage 31: Add compact table rendering for long lists ===
# Project: GrantShelf
def render_compact_table(rows, columns):
    """Render a compact table with word-wrapped cells for long lists."""
    widths = [max(len(str(row[i]) if row else 0) for row in rows) + 2 for i in range(len(columns))]
    separator = '+'.join('-' * (w + 2) for w in widths).replace('+', '|')
    lines = [separator]
    header_line = '| ' + ' | '.join(str(c) for c in columns) + ' |'
    lines.append(header_line)
    lines.append(separator)
    for row in rows:
        cell_line = '| ' + ' | '.join(str(cell) if cell else '' for cell in row) + ' |'
        lines.append(cell_line)
    return '\n'.join(lines)

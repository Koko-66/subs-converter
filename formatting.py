# https://realpython.com/openpyxl-excel-spreadsheets-python/
from openpyxl.styles import (Border,
                             Font,
                             NamedStyle,
                             PatternFill,
                             Side,)
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule

# Header styling
header = NamedStyle(name='header')
header.font = Font(bold=True, size=12)
header.border = Border(bottom=Side(border_style="medium"))
header.fill = PatternFill(
    fill_type="solid", start_color="00969696", end_color="00969696")


def format_header(ws):
    """Apply formatting to first row"""
    for cell in ws[1]:
        cell.style = header



# Conditional formatting
def apply_conditional_format(ws):
    """Highlight in red if text in column B is longer than in column A"""
    red_background = PatternFill(start_color="00FF8080", end_color="00FF8080")
    diff_style = DifferentialStyle(fill=red_background)
    rule = Rule(type="expression", dxf=diff_style)
    rule.formula = ['$E2="Too Long"']
    ws.conditional_formatting.add("A2:O100", rule)

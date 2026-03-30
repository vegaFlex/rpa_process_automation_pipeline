from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font


def generate_excel_report(dataframe, output_path: Path) -> None:
    workbook = Workbook()

    raw_sheet = workbook.active
    raw_sheet.title = "raw_data"

    headers = list(dataframe.columns)
    raw_sheet.append(headers)

    for row in dataframe.itertuples(index=False, name=None):
        raw_sheet.append(row)

    for cell in raw_sheet[1]:
        cell.font = Font(bold=True)

    summary_sheet = workbook.create_sheet(title="summary")
    summary_sheet["A1"] = "Metric"
    summary_sheet["B1"] = "Value"
    summary_sheet["A1"].font = Font(bold=True)
    summary_sheet["B1"].font = Font(bold=True)

    summary_sheet["A2"] = "Total Records"
    summary_sheet["B2"] = len(dataframe)

    summary_sheet["A3"] = "Successful Logins"
    summary_sheet["B3"] = int(dataframe["login_success"].sum())

    summary_sheet["A4"] = "Page Category"
    summary_sheet["B4"] = dataframe.loc[0, "page_category"]

    summary_sheet["A5"] = "Latest Page Heading"
    summary_sheet["B5"] = dataframe.loc[0, "page_heading"]

    workbook.save(output_path)

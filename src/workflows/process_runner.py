from datetime import datetime

from src.config import settings
from src.notifications.email_sender import EmailSender
from src.pages.login_page import LoginPage
from src.pages.report_page import ReportPage
from src.processing.data_processor import (
    load_raw_data,
    save_processed_data,
    save_raw_data,
    transform_session_data,
)
from src.reporting.excel_report import generate_excel_report


class ProcessRunner:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def run(self) -> None:
        self.logger.info("Starting login workflow.")

        login_page = LoginPage(self.driver)
        login_page.open(settings.BASE_URL)
        self.logger.info("Login page opened: %s", settings.BASE_URL)

        login_page.login(settings.LOGIN_USERNAME, settings.LOGIN_PASSWORD)
        self.logger.info("Login form submitted.")

        login_page.verify_login_success()
        self.logger.info("Login successful.")

        report_page = ReportPage(self.driver)
        report_page.verify_page_loaded()
        self.logger.info("Secure/report page loaded successfully.")

        extracted_data = {
            "execution_timestamp": datetime.now().isoformat(),
            "page_heading": report_page.get_page_heading(),
            "flash_message": report_page.get_flash_message(),
            "current_url": report_page.get_current_url(),
        }

        raw_output_path = settings.RAW_DATA_DIR / "session_data.json"
        save_raw_data(extracted_data, raw_output_path)
        self.logger.info("Raw data saved to: %s", raw_output_path)

        raw_payload = load_raw_data(raw_output_path)
        processed_df = transform_session_data(raw_payload)

        processed_output_path = settings.PROCESSED_DATA_DIR / "session_data_processed.csv"
        save_processed_data(processed_df, processed_output_path)
        self.logger.info("Processed data saved to: %s", processed_output_path)

        excel_output_path = settings.OUTPUT_DIR / "session_report.xlsx"
        generate_excel_report(processed_df, excel_output_path)
        self.logger.info("Excel report saved to: %s", excel_output_path)

        email_sender = EmailSender(self.logger)
        email_body = (
            "Hello,\n\n"
            "The automation process completed successfully.\n"
            "Please find the attached report.\n"
        )

        if settings.EMAIL_ENABLED:
            email_payload = email_sender.build_email_payload(
                recipient=settings.EMAIL_TO,
                subject=settings.EMAIL_SUBJECT,
                body=email_body,
                attachment_path=excel_output_path,
            )
            self.logger.info("Email payload ready: %s", email_payload)
            print("Email payload:", email_payload)
        else:
            self.logger.info("Email sending is disabled in settings.")

        print("Extracted data:", extracted_data)
        print(processed_df)
        print("Excel report:", excel_output_path)

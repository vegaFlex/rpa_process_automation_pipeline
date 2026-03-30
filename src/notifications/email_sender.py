from pathlib import Path


class EmailSender:
    def __init__(self, logger):
        self.logger = logger

    def build_email_payload(
        self,
        recipient: str,
        subject: str,
        body: str,
        attachment_path: Path,
    ) -> dict:
        if not attachment_path.exists():
            raise FileNotFoundError(f"Attachment not found: {attachment_path}")

        payload = {
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "attachment_path": str(attachment_path),
        }

        self.logger.info("Email payload prepared for: %s", recipient)
        return payload

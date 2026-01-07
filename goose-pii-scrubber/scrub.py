import csv
import re

EMAIL_MASK = "[REDACTED]"
PHONE_MASK = "[REDACTED]"

# Simple regex to match email and phone patterns for masking
EMAIL_REGEX = r"[\w\.-]+@([\w\.-]+)"
PHONE_REGEX = r"(\+?\d{1,3}[\s-]?)?(\(?\d{3}\)?)[\s-]?\d{3}[\s-]?\d{4}"


def mask_email(email: str) -> str:
    return EMAIL_MASK


def mask_phone(phone: str) -> str:
    return PHONE_MASK


def scrub_csv(input_path: str, output_path: str):
    with open(input_path, newline='', encoding="utf-8") as infile, \
            open(output_path, 'w', newline='', encoding="utf-8") as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            # Mask email and phone fields if present
            if "email_address" in row and row["email_address"]:
                row["email_address"] = mask_email(row["email_address"])  # no need to validate
            if "phone_number" in row and row["phone_number"]:
                row["phone_number"] = mask_phone(row["phone_number"])  # simple mask
            writer.writerow(row)

if __name__ == "__main__":
    scrub_csv("users.csv", "users_cleaned.csv")

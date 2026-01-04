#!/bin/bash
# setup_junk.sh
# Generates a mess of files for the Desktop Tidy-Up Agent to organize.

TARGET_DIR="test_downloads"
mkdir -p "$TARGET_DIR"

echo "🗑️ Creating junk in $TARGET_DIR..."

# 1. Finance/Invoice (Text)
cat <<EOF > "$TARGET_DIR/invoice_2024_01.txt"
INVOICE #1023
Date: 2024-01-15
To: John Doe
From: AWS Web Services
Amount: \$405.00
Service: EC2 Instances
Please remit payment by EOM.
EOF

# 2. Personal (Markdown)
cat <<EOF > "$TARGET_DIR/mom_letter.md"
# Dear Son,
Hope you are doing well at university.
The cat misses you effectively.
Love, Mom.
EOF

# 3. Work/Code (Python)
cat <<EOF > "$TARGET_DIR/deploy_script.py"
import os
def deploy():
    print("Deploying to production...")
    # TODO: Fix this
deploy()
EOF

# 4. Work/Meeting Notes (Text)
cat <<EOF > "$TARGET_DIR/meeting_2023_12.txt"
Meeting Minutes: Q4 Strategy
Attendees: Alice, Bob, Charlie
Action Items:
- Fix the bug in login
- Update the quarterly report
EOF

# 5. Archive/Binary (Empty files simulating binaries)
touch "$TARGET_DIR/installer_v2.dmg"
touch "$TARGET_DIR/backup.zip"
touch "$TARGET_DIR/old_photo.jpg"

echo "✅ Created 7 mixed files in $TARGET_DIR."
echo "Run the agent to organize them!"

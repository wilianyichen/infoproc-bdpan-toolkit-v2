"""Stable workflow policy constants."""

FIXED_REMOTE_ROOTS = {
    "text": "/开智/视频文本蒸馏/文本/录播文本",
    "final": "/开智/视频文本蒸馏/蒸馏/录播",
    "distill_subdir": "distill__md",
    "rank_subdir": "rank__md",
}

NO_VALID_TEXT_SKIP_TARGETS = ("text", "distill", "rank")

RETENTION_POLICY = {
    "keep": [
        "01_probe",
        "03_text_raw",
        "04_text_clean",
        "05_final",
        "_delivery",
        "_logs",
        "_manifests",
        "_flags",
        "_reports",
    ],
    "prune": [
        "00_source",
        "02_normalized",
    ],
}

# Empty Transcript Policy

A result is not considered a valid textual output just because later stages emitted markdown.

If the transcription layer yields no segments and both raw and clean text are empty:

- classify as `no_valid_text`
- exclude from upload to text/final output trees
- preserve the exception in audit artifacts
- only clear the exception after successful retranscription

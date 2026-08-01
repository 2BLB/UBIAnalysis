#AI suggested formAT

"""
normalize_educ_codebook.py

Reads the original education codebook and creates
educ_codebook_normalized.txt.

This is a one-time utility script and is not part
of the UBI analysis itself.
"""
educ_input = "educ_codebook.txt"
educ_output = "educ_codebook_normalized.txt"

with open(educ_input, "r", encoding="utf-8") as infile:
    lines = [line.strip() for line in infile if line.strip()]

# Remove header
if not lines[0].isdigit():
    lines = lines[1:]

normalized = []

for i in range(0, len(lines), 2):
    code = lines[i]
    description = lines[i + 1]

    # Check if code is a range (example: 010–014)
    if "–" in code:
        start, end = code.split("–")

        for num in range(int(start), int(end) + 1):
            normalized.append(f"{num:03d}")
            normalized.append(description)

    # Single code
    else:
        normalized.append(code)
        normalized.append(description)


# Write the new normalized file
with open(educ_output, "w", encoding="utf-8") as outfile:
    for line in normalized:
        outfile.write(line + "\n")

print("Normalized education codebook created!")

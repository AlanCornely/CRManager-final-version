
lines = []
with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check lines 55 and 56 (0-indexed, so 56-57 1-indexed)
print(f"Line 55: {lines[55]}")
print(f"Line 56: {lines[56]}")

# Fix
if "Faça login para" in lines[55]:
    lines[55] = lines[55].strip() + " " + lines[56].strip() + "\n"
    lines.pop(56)
    print("Fixed!")
else:
    print("Pattern not found where expected.")

with open('frontend/index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

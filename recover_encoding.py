import os

files = [
    "2024/reports/report10.html",
    "2024/reports/report20.html",
    "2024/reports/report30.html",
    "2024/reports/report40.html",
    "2024/reports/report60.html",
    "2024/reports/report70.html",
    "2025/reports/report01.html",
    "2025/reports/report02.html",
    "2025/reports/report03.html",
    "index.html"
]

encodings = ['utf-8-sig', 'utf-8', 'shift_jis', 'cp932', 'euc_jp']

def try_fix(filepath):
    print(f"Checking {filepath}...")
    try:
        with open(filepath, 'rb') as f:
            raw = f.read()
        
        # Try to find a valid encoding
        content = None
        for enc in encodings:
            try:
                content = raw.decode(enc)
                if '???' in content: # Often ? indicates lossy conversion
                    print(f"  {enc} worked but found placeholders.")
                    continue
                print(f"  Found valid encoding: {enc}")
                break
            except:
                continue
        
        if content:
            # Modernize header to UTF-8
            if '<meta charset=' in content:
                content = content.replace('charset="shift_jis"', 'charset="UTF-8"')
                content = content.replace('charset="Shift_JIS"', 'charset="UTF-8"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Successfully fixed and saved as UTF-8.")
        else:
            print(f"  Failed to detect valid encoding for {filepath}")
    except Exception as e:
        print(f"  Error processing {filepath}: {e}")

for f in files:
    if os.path.exists(f):
        try_fix(f)
    else:
        print(f"File not found: {f}")

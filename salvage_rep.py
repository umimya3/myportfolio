import os

files = [
    "2024/reports/rep01.html",
    "2024/reports/rep02.html",
    "2024/reports/rep03.html",
    "2024/reports/rep04.html",
    "2024/reports/rep05.html",
    "2024/reports/rep06.html",
    "2024/reports/rep20.html",
]

for f_path in files:
    if not os.path.exists(f_path):
        continue
    print(f"Reading {f_path}...")
    try:
        with open(f_path, 'rb') as f:
            raw = f.read()
        
        for enc in ['cp932', 'shift_jis', 'utf-8']:
            try:
                content = raw.decode(enc)
                print(f"  Success with {enc}! First 100 chars: {content[:100].strip()}")
                # Save as proper UTF-8
                with open(f_path + ".fixed.html", 'w', encoding='utf-8') as f_out:
                    f_out.write(content)
                break
            except:
                continue
    except Exception as e:
        print(f"  Error: {e}")

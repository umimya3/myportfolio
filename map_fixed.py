import os
import re

directory = "2024/reports/"
fixed_files = sorted([f for f in os.listdir(directory) if f.endswith(".fixed.html")])

print(f"--- MAPPING RESULTS ---")
for f_name in fixed_files:
    f_path = os.path.join(directory, f_name)
    try:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        h1 = re.search(r'<h1>(.*?)</h1>', content, re.IGNORECASE)
        
        t_text = title.group(1).strip() if title else "NONE"
        h_text = h1.group(1).strip() if h1 else "NONE"
        
        print(f"[{f_name}] -> Title: {t_text}, H1: {h_text}")
    except Exception as e:
        print(f"[{f_name}] Error: {e}")
print(f"--- END MAPPING ---")

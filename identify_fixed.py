import os
import re

directory = "2024/reports/"
fixed_files = [f for f in os.listdir(directory) if f.endswith(".fixed.html")]

for f_name in fixed_files:
    f_path = os.path.join(directory, f_name)
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    h1 = re.search(r'<h1>(.*?)</h1>', content, re.IGNORECASE)
    
    print(f"FILE: {f_name}")
    print(f"  Title: {title.group(1) if title else 'N/A'}")
    print(f"  H1: {h1.group(1) if h1 else 'N/A'}")
    print("-" * 20)

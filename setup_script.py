# Build script for Pulse Audio Store
import os, json

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as out:
        out.write(content)
    print(f'Wrote: {path}')

print('Script builder ready')

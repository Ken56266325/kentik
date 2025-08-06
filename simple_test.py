
import sys
sys.path.insert(0, '.')

try:
    import kentik
    print("SUCCESS: Import kentik OK")
except Exception as e:
    print(f"ERROR: {e}")

import os
import subprocess

# Paths to scripts
image_script = "scripts/image_grading.py"


print("🎬 Running Image Color Grading...")
subprocess.run(["python", image_script])


print("✅ All tasks completed! Check the output folder.")

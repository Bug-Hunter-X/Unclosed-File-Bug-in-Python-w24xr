# Unclosed File Bug in Python
This repository demonstrates a common error in Python: forgetting to close files after use.  The `bug.py` file shows the incorrect code, while `bugSolution.py` provides a corrected version.

**The Problem:** Failing to close files explicitly using `f.close()` can lead to resource leaks (the file remains locked) and potential data corruption.  This is particularly important when dealing with large files or writing operations.

**The Solution:** Always ensure you explicitly close files using `f.close()` or utilize context managers (`with open(...) as f:`).

"""
Quick script to test the full pipeline on a single PDF.
Run: python scripts/test_pipeline.py path/to/paper.pdf
"""
import sys

if __name__ == "__main__":
    pdf_path = sys.argv[1] if len(sys.argv) > 1 else "sample.pdf"
    print(f"Testing pipeline on: {pdf_path}")
    # TODO: call orchestrator.run_pipeline()

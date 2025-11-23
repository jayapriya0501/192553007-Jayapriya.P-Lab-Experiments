"""
Quick Test Runner for All Lab Programs
Runs all programs in sequence (visualization programs require closing windows to continue)
"""

import subprocess
import sys

programs = [
    ("Dataset Generator", "generate_datasets.py"),
    ("Program 1: Data Exploration", "program1_data_exploration.py"),
    ("Program 2: Analytics Types", "program2_analytics_types.py"),
    ("Program 3: Visualizations", "program3_visualizations.py"),
    ("Program 4: Root Cause Analysis", "program4_root_cause_analysis.py"),
]

def run_program(name, filename):
    """Run a single program"""
    print(f"\n{'='*70}")
    print(f"Running: {name}")
    print(f"File: {filename}")
    print(f"{'='*70}\n")
    
    try:
        result = subprocess.run(
            ["uv", "run", filename],
            capture_output=False,
            text=True,
            check=True
        )
        print(f"\n✅ {name} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ {name} failed with error code {e.returncode}")
        return False
    except Exception as e:
        print(f"\n❌ Error running {name}: {str(e)}")
        return False

def main():
    print("="*70)
    print("LAB ASSIGNMENT 4 - TEST RUNNER")
    print("="*70)
    print("\nThis script will run all lab programs in sequence.")
    print("For visualization programs (3 & 4), close the plot windows to continue.")
    print()
    
    input("Press ENTER to start...")
    
    results = {}
    
    for name, filename in programs:
        success = run_program(name, filename)
        results[name] = "✅ PASSED" if success else "❌ FAILED"
    
    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    for name, result in results.items():
        print(f"{result} - {name}")
    
    passed = sum(1 for r in results.values() if "PASSED" in r)
    total = len(results)
    
    print(f"\nTotal: {passed}/{total} programs passed")
    print("="*70)

if __name__ == "__main__":
    main()

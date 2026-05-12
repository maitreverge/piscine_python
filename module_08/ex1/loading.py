import importlib
import sys


def check_dependency(package_name: str) -> tuple[bool, str]:
    """Check if a package is installed and return its version."""
    try:
        module = importlib.import_module(package_name)
        version: str = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def check_all_dependencies() -> bool:
    """Check all required dependencies and display their status."""
    dependencies: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
    ]
    all_installed: bool = True
    for package_name, description in dependencies:
        installed, version = check_dependency(package_name)
        if installed:
            print(f"[OK] {package_name} ({version}) - {description}")
        else:
            print(f"[KO] {package_name} - MISSING")
            all_installed = False

    if not all_installed:
        print("\nInstall missing dependencies with one of:")
        print("  pip install -r requirements.txt")
        print("  poetry install")
    return all_installed


def compare_pip_poetry() -> None:
    """Show differences between pip and Poetry dependency management."""
    print("\nDependency manager comparison:")
    print("  pip    -> uses requirements.txt (flat list of packages)")
    print("  Poetry -> uses pyproject.toml   (resolver + lockfile)")
    print(f"  Python running: {sys.executable}\n")


def generate_matrix_analysis() -> None:
    """Generate simulated Matrix data and create a visualization."""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")
    data_points: int = 1000
    print(f"Processing {data_points} data points...")

    # numpy is the source of the dataset (required by the exercise)
    rng = np.random.default_rng(seed=42)
    print(f"RNG = {rng}")
    values = rng.normal(loc=50, scale=15, size=data_points)

    data_frame = pd.DataFrame(
        {
            "index": np.arange(data_points),
            "value": values,
        }
    )

    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(data_frame["index"], data_frame["value"], color="green")
    plt.title("Matrix Analysis")
    plt.xlabel("Data Point")
    plt.ylabel("Signal Value")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    if not check_all_dependencies():
        sys.exit(1)

    compare_pip_poetry()
    generate_matrix_analysis()


if __name__ == "__main__":
    main()

packages = {
    "numpy": "NumPy",
    "pandas": "Pandas",
    "matplotlib": "Matplotlib",
    "seaborn": "Seaborn",
    "scipy": "SciPy",
    "sklearn": "Scikit-learn",
    "statsmodels": "Statsmodels",
    "prophet": "Prophet (Optional)"
}

print(f"{'Library':<20} | {'Status':<10} | {'Version'}")
print("-" * 45)

for module_name, display_name in packages.items():
    try:
        mod = __import__(module_name)
        version = getattr(mod, "__version__", "Found (no __version__)")
        print(f"{display_name:<20} | PASS       | {version}")
    except ImportError:
        status = "OPTIONAL" if module_name == "prophet" else "FAIL"
        print(f"{display_name:<20} | {status:<10} | Not Installed")
# HAGIS: Heatmap-Aided Solving of Guarded System of Polynomial Equalities for Exact Invariant Synthesis

# HAGIS Installation.
Install python, cvxpy, z3 etc using pip.

# HAGIS: How to run?
1. Put the benchmarks you want to run in program_list.txt (The list of all available benchmarks is given in program_list_all.txt, and the correpsonding benchmark files are in configuration_files). 1 benchmark per line (no extra spaces).
2. Run python3 run.py (the output prints to terminal)

# HAGIS: Results
For each of the benchmark suites, the results of running HAGIS are given in Results_<benchmark_suite>.txt

# HAGIS Benchmark Suites
For people interested in just the benchmarks, this repository also contains all benchmark suites used in our paper neatly categorized in the HAGISBenchmarks folder:
- bigconstants
- highprec
- complexRationalFunc
- complexcoeff
- manyPaths
- RealLiveExamples
- highVars

These benchmarks are released solely for reproducibility of evaluation.



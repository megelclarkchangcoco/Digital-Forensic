# Python Forensic Coding Exercise Report

## Purpose
The purpose of this coding exercise is to develop practical skills in writing Python scripts for basic forensic tasks, such as data parsing and file analysis. Through this exercise, students will learn to automate forensic processes and analyze data more efficiently.

## Scope
This report covers the objectives, script development process, testing, and results of Python scripts designed for forensic tasks, including data parsing and file analysis.

## Objectives
1. **Objective 1**: Develop a Python script to parse specific data formats (e.g., CSV, JSON) for forensic analysis.
2. **Objective 2**: Write a Python script to analyze file metadata and content for potential forensic evidence.
3. **Objective 3**: Demonstrate understanding of Python libraries commonly used in digital forensics (e.g., `pandas`, `os`, `hashlib`).

## Script Development

### 3.1 Data Parsing Script
- **Script Purpose**: The script is designed to parse files (e.g., CSV, JSON) and extract relevant forensic data such as timestamps, IP addresses, and user activities.
- **Libraries Used**: `pandas`, `csv`, `json`
- **Script Explanation**: This script uses `pandas` to load and parse CSV data, then extracts specific columns.

### 3.2 File Analysis Script
- **Script Purpose**: The script analyzes file metadata and content to identify potential forensic evidence, such as file creation dates, last modified dates, and hash values for integrity verification.
- **Libraries Used**: `os`, `hashlib`
- **Script Explanation**: This script uses the `os` library to obtain file metadata and the `hashlib` library to calculate the SHA-256 hash of a file. This information is critical for verifying file integrity and tracking modifications.

## Testing and Results

### 4.1 Data Parsing Script Testing
- Describe the testing process and results for the data parsing script.

### 4.2 File Analysis Script Testing
- Describe the testing process and results for the file analysis script.

## Practice Dataset
The Practice Dataset folder is designed to provide data files essential for testing forensic scripts and simulating analysis tasks. This folder automatically generates two CSV files:

### 1. system_log_files_dataset.csv: Contains simulated system log data, including event timestamps, user activities, IP addresses, and system status indicators. This dataset supports the development and testing of data parsing scripts, helping students learn to extract and analyze system log information for forensic insights.

### 2. malware_analysis_dataset.csv: Provides a set of data entries relevant to malware analysis, including file paths, hash values, malware signatures, and threat levels. This dataset enables practice with identifying and verifying potential malware threats through automated analysis.

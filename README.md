# FILE-INTEGRITY-CHECKER-

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : SHABNAM SHARMA

*INTERN ID* : CT12WE04

*DOMAIN* : CYBER SECURITY & ETHICAL HACKING  

*DURATION* : 12 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR 

## DESCRIPTION OF THE TASK 

BUILD A TOOL TO MONITOR CHANGES IN FILES BY CALCULATING AND COMPARING HASH VALUES
A PYTHON SCRIPT USING LIBRARIES LIKE HASHLIB TO ENSURE FILE INTEGRITY 

Introduction

In today’s digital landscape, ensuring the integrity of files is crucial for data security, compliance, and system reliability. Files can be altered accidentally, due to unauthorized access, or because of malware infections, leading to data corruption, loss, or even security breaches. One of the most effective ways to detect file modifications is by using cryptographic hashing.

A hash function generates a unique fixed-size string (hash value) based on the contents of a file. Even a small change in the file results in a completely different hash value, making it a reliable method for detecting modifications. This project aims to build a tool that monitors file changes by calculating and comparing SHA-256 hash values over time.

By implementing this tool, users can determine whether a file has been modified, deleted, or remains unchanged. This is particularly useful in cybersecurity, auditing, and integrity verification tasks.

Main Features

1. File Change Detection
The tool monitors a specific file and detects any modifications, deletions, or additions by comparing current and previously stored hash values.

2. SHA-256 Hash Calculation
It uses the SHA-256 cryptographic hash function, which is widely trusted for ensuring file integrity. Even the slightest change in a file generates a completely different hash value.

 3. JSON-Based Storage
The tool maintains a record of previous hash values in a JSON file (file_hash.json). This allows it to detect changes over multiple runs.

4. Status Reporting
It provides clear status messages:

"No Changes" – The file remains the same.

"File Modified" – The file’s contents have been altered.

"File Deleted" – The file no longer exists.

"First Scan - File Added" – The file is newly scanned for the first time.

5. Error Handling
The tool gracefully handles issues such as missing files, permission errors, and JSON decoding errors.

6. Lightweight & Fast
Since it only reads and computes the hash of a single file at a time, it is efficient and consumes minimal system resources.

How Does It Work?
The tool operates in three main steps:

Step 1: Initial Scan
When the script runs for the first time, it calculates the SHA-256 hash of the target file.

The generated hash value is stored in a JSON file for future reference.

Since no previous hash exists, the tool considers this the first scan and reports "First Scan - File Added".

Step 2: Monitoring for Changes
On subsequent runs, the tool:

Recomputes the SHA-256 hash of the file.

Reads the previously stored hash from file_hash.json.

Compares the new hash with the old hash to determine if the file has changed.

Step 3: Updating the Stored Hash
If the file remains unchanged, the script simply reports "No Changes".

If the file has been modified, the hash will differ, and the tool reports "File Modified" before saving the new hash.

If the file has been deleted, the script detects its absence and reports "File Deleted" without updating the hash.

Limitations

Monitors Only One File at a Time
The current implementation is designed to track a single file. It does not scan entire folders or multiple files simultaneously.

1. Not a Real-Time Monitoring Tool
It does not run continuously in the background. Instead, users must execute the script manually or schedule it using automation tools like Task Scheduler (Windows) or Cron Jobs (Linux).

2. No Backup or Restoration Features
If a file is modified or deleted, the tool can detect the change but cannot recover or restore the original file.

3. Only Uses SHA-256 for Hashing
While SHA-256 is secure, some users may prefer alternative algorithms such as MD5, SHA-1, or SHA-3 for different purposes.

4. Limited to Local Files
It only works on local files and does not support monitoring files over network drives, cloud storage, or external devices.


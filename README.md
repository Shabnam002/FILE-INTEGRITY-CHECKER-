# FILE-INTEGRITY-CHECKER-

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : SHABNAM SHARMA

*INTERN ID* : CT12WE04

*DOMAIN* : CYBER SECURITY & ETHICAL HACKING  

*DURATION* : 12 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR 

## DESCRIPTION OF THE TASK 

#BUILD A TOOL TO MONITOR CHANGES IN FILES BY CALCULATING AND COMPARING HASH VALUES

A PYTHON SCRIPT USING LIBRARIES LIKE HASHLIB TO ENSURE FILE INTEGRITY 

#Introduction

In today’s digital landscape, ensuring the integrity of files is crucial for data security, compliance, and system
reliability. Files can be altered accidentally, due to unauthorized access, or because of malware infections, leading to data corruption, loss, or even security breaches. One of the most effective ways to detect file modifications is by using cryptographic hashing.

A hash function generates a unique fixed-size string (hash value) based on the contents of a file. Even a small change in the file results in a completely different hash value, making it a reliable method for detecting modifications. This project aims to build a tool that monitors file changes by calculating and comparing SHA-256 hash values over time.

By implementing this tool, users can determine whether a file has been modified, deleted, or remains unchanged. This is particularly useful in cybersecurity, auditing, and integrity verification tasks.

#Main Features

1. File Change Detection
The primary function of this tool is to detect changes in a specific file by computing its hash value and comparing it with previously stored hash records. It helps users identify unauthorized modifications, accidental changes, or deletions.

2. SHA-256 Hash Calculation
  It uses the SHA-256 cryptographic hash function, which is widely used for data integrity verification. Even the smallest change in a file results in a completely different hash, making it a reliable method for detecting alterations.

4. JSON-Based Storage
To maintain a history of file integrity, the tool stores hash values in a JSON file (file_hash.json). This enables it to detect modifications over multiple executions without requiring a database or complex storage system.

5. Status Reporting
To make the results clear and user-friendly, the tool provides four possible status messages when checking a file:

"No Changes" – The file remains unchanged since the last scan.

"File Modified" – The file’s contents have been altered.

"File Deleted" – The monitored file has been removed or is missing.

"First Scan - File Added" – The file is newly scanned for the first time.

5. Error Handling
The tool is designed to handle errors gracefully, including:

Missing files – If the monitored file is deleted or unavailable.

Permission issues – If the user lacks access rights.

Corrupt JSON records – If the stored hash file is damaged or improperly formatted.

6. Lightweight & Fast
Since the tool operates by calculating a single hash per execution, it is highly efficient and does not consume excessive system resources. This makes it ideal for quick integrity checks in any computing environment.

#How Does It Work?

The tool follows three key steps to monitor file changes:

Step 1: Initial Scan
When executed for the first time, the tool calculates the SHA-256 hash of the chosen file.

This hash is stored in file_hash.json for future reference.

Since this is the first scan, the tool reports: "First Scan - File Added."

Step 2: Monitoring for Changes
On subsequent executions, the tool recomputes the file's SHA-256 hash.

It then retrieves the previously stored hash from file_hash.json.

The new hash is compared with the stored hash:

If they are the same, it reports: "No Changes."

If they differ, it reports: "File Modified."

If the file no longer exists, it reports: "File Deleted."

Step 3: Updating the Stored Hash
If a modification is detected, the new hash is saved to file_hash.json for future comparisons.

This ensures that the tool always references the latest known file state in subsequent checks.

#Limitations

Monitors Only One File at a Time
Currently, this tool is designed to track a single file per execution. It does not support scanning entire folders or multiple files simultaneously.

2. Not a Real-Time Monitoring Tool
The tool does not continuously run in the background. Instead, users must manually execute the script or set up automated scheduling using:

Task Scheduler (Windows)

Cron Jobs (Linux/Mac)

 3. No Backup or Restoration Features
While the tool detects file modifications, it does not provide backup or recovery options. Users concerned about data integrity should maintain separate backups.

4. Only Uses SHA-256 for Hashing
The tool exclusively uses SHA-256, which is a secure and widely used hashing algorithm. However, some users may prefer other hashing methods:

MD5 – Faster but less secure (prone to collisions).

SHA-1 – Outdated and vulnerable to attacks.

SHA-3 – A newer alternative with different security properties.

5. Limited to Local Files
This tool only works on files stored locally on a user’s computer. It does not support monitoring files on:

Network drives

Cloud storage (Google Drive, Dropbox, etc.)

External USB devices or hard drives

Conclusion

The File Integrity Checker is a lightweight and effective solution for detecting file modifications using SHA-256 hashing. By providing accurate change detection, JSON-based storage, and clear status reporting, it is a valuable tool for anyone needing to track file integrity.

The tool is particularly useful for:

Security analysts monitoring critical system files.

Developers verifying software integrity.

System administrators ensuring that configuration files remain unchanged.

By continuously improving the project, future versions could include support for multiple files, real-time monitoring, and backup features. 

#OUTPUT

![Image](https://github.com/user-attachments/assets/29ec7517-4d95-4e8b-a5cd-28fa787925cc)

<img width="562" alt="Image" src="https://github.com/user-attachments/assets/fd501ed5-88c0-407a-bd9c-f84d03ddee4d" />

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
The primary function of this tool is to detect modifications, deletions, or additions of a specific file by comparing the current hash value with the previously stored hash. If any changes occur, the tool immediately reports them, making it easier to monitor sensitive files.

2. SHA-256 Hash Calculation
The tool employs the SHA-256 cryptographic hashing algorithm, which is widely regarded as a secure and reliable method for checking file integrity. Since SHA-256 produces a unique, fixed-size hash for any given file, even the smallest modification results in a completely different hash, ensuring accurate detection.

3. JSON-Based Storage
To maintain a record of previous file states, the tool stores hash values in a JSON file named file_hash.json. This makes it possible to check file integrity across multiple runs and allows users to track changes over time.

4. Status Reporting
The tool provides clear and easy-to-understand status messages:

"No Changes" – The file remains unchanged.

"File Modified" – The file has been altered since the last check.

"File Deleted" – The monitored file has been removed.

"First Scan - File Added" – The tool has detected the file for the first time and stored its hash.

5. Error Handling
The tool includes robust error handling to manage issues such as:

Missing files

Permission errors

JSON decoding errors

File read/write errors

These error-handling mechanisms ensure that the tool runs smoothly without unexpected crashes.

6. Lightweight & Fast
This tool is designed for efficiency. Since it only computes the hash of a single file at a time, it is extremely lightweight and consumes minimal system resources. This makes it suitable for use on any system without significant performance overhead.

#How Does It Work?

This tool operates in three main steps:

Step 1: Initial Scan
When the script runs for the first time:

It calculates the SHA-256 hash of the specified file.

The computed hash value is stored in the file_hash.json file for future reference.

Since there is no previous hash to compare, the tool reports "First Scan - File Added."

Step 2: Monitoring for Changes
On subsequent runs, the tool performs the following actions:

Recalculates the SHA-256 hash of the file.

Retrieves the previous hash value stored in file_hash.json.

Compares the two hash values:

If the hashes match, the tool reports "No Changes."

If the hashes differ, it means the file has been modified, and the tool reports "File Modified."

If the file is missing, the tool reports "File Deleted."

Step 3: Updating the Stored Hash
After each run, the tool updates file_hash.json to store the latest hash value.

If no changes are detected, the existing hash remains in the file.

If modifications occur, the new hash replaces the old one.

If the file is deleted, the tool retains the last known hash but warns the user of the deletion.

#Limitations

Monitors Only One File at a Time
Currently, the tool is designed to track a single file at a time. It does not scan entire directories or multiple files in one execution.

1. Not a Real-Time Monitoring Tool
The tool does not continuously run in the background. Users must manually execute the script or schedule it using automation tools like:

Task Scheduler (Windows)

Cron Jobs (Linux/Mac)

2. No Backup or Restoration Features
While the tool detects file changes, it does not provide any mechanisms to restore an earlier version of the file. If data integrity is a concern, users should maintain separate backups.

3. Only Uses SHA-256 for Hashing
The tool relies exclusively on SHA-256, which is strong but may not be suitable for all use cases. Some users may prefer alternative algorithms like:

MD5 (faster but less secure)

SHA-1 (outdated and insecure for cryptographic purposes)

SHA-3 (a newer alternative with different security properties)

4. Limited to Local Files
This tool only works with local files stored on a user's device. It does not support tracking changes in:

Network drives

Cloud storage (Google Drive, Dropbox, etc.)

USB or external hard drives


#OUTPUT

![Image](https://github.com/user-attachments/assets/29ec7517-4d95-4e8b-a5cd-28fa787925cc)

<img width="562" alt="Image" src="https://github.com/user-attachments/assets/fd501ed5-88c0-407a-bd9c-f84d03ddee4d" />



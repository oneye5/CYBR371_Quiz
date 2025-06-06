import random
import re
import os
import sys
import time

# Database of questions and answers extracted from the documents
questions_db = [
    {
        "question": "In the context of system security, the term 'system' refers to what?",
        "options": {
            "A": "Any combination of hardware, software, infrastructure, and processes that work together to perform specific functions or tasks",
            "B": "Only a computer's operating system",
            "C": "Only the software applications installed on a computer",
            "D": "Only the hardware components of a network"
        },
        "correct": "A"
    },
    {
        "question": "What is the primary goal of system security?",
        "options": {
            "A": "To protect a system’s resources from unauthorized access, modification, or corruption",
            "B": "To ensure a system operates at maximum speed",
            "C": "To update software regularly",
            "D": "To maintain only the hardware components"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following best defines Information Security",
        "options": {
            "A": "A well-informed sense of assurance that information risks and controls are in balance",
            "B": "The physical protection of computer hardware",
            "C": "The exclusive use of encryption to protect data",
            "D": "A process that only focuses on data backup"
        },
        "correct": "A"
    },
    {
        "question": "Which principle states that only the minimum necessary access should be granted to perform a task?",
        "options": {
            "A": "Least Privilege",
            "B": "Separation of Duties",
            "C": "Fail-Safe Defaults",
            "D": "Economy of Mechanism"
        },
        "correct": "A"
    },
    {
        "question": "What does the principle of 'Separation of Duties' require in a security context?",
        "options": {
            "A": "Dividing critical tasks among multiple individuals so that no single person controls all aspects of a process",
            "B": "Assigning all security responsibilities to one system administrator",
            "C": "Allowing users to perform any task if they are trusted",
            "D": "Enforcing the same privileges for every user"
        },
        "correct": "A"
    },
    {
        "question": "According to the Fail-Safe Defaults principle, what should be the default access setting in a secure system?",
        "options": {
            "A": "Access should be denied unless explicit permission is granted",
            "B": "Access should be allowed unless explicitly denied",
            "C": "Access should be granted temporarily during peak times",
            "D": "Access should be unrestricted by default"
        },
        "correct": "A"
    },
    {
        "question": "Which principle advises that security mechanisms should be as simple as possible?",
        "options": {
            "A": "Economy of Mechanism",
            "B": "Open Design",
            "C": "Complete Mediation",
            "D": "Psychological Acceptability"
        },
        "correct": "A"
    },
    {
        "question": "What is the core requirement of the 'Complete Mediation' principle?",
        "options": {
            "A": "Every access to system objects must be checked for authorization",
            "B": "Authorization is checked only once per session",
            "C": "Only high-risk operations require authorization",
            "D": "Cached permissions can be reused without re-checking"
        },
        "correct": "A"
    },
    {
        "question": "Which principle states that the security of a system should not depend on the secrecy of its design or implementation?",
        "options": {
            "A": "Open Design",
            "B": "Least Common Mechanism",
            "C": "Separation of Duties",
            "D": "Fail-Safe Defaults"
        },
        "correct": "A"
    },
    {
        "question": "What does the 'Least Common Mechanism' principle emphasize?",
        "options": {
            "A": "Minimizing the use of shared mechanisms among different users or processes",
            "B": "Maximizing shared resources to reduce costs",
            "C": "Ensuring all users share the same system privileges",
            "D": "Implementing one universal access mechanism for simplicity"
        },
        "correct": "A"
    },
    {
        "question": "Which principle ensures that security mechanisms are designed to be user-friendly so that they are not bypassed?",
        "options": {
            "A": "Psychological Acceptability",
            "B": "Least Privilege",
            "C": "Economy of Mechanism",
            "D": "Complete Mediation"
        },
        "correct": "A"
    },
    {
        "question": "The concept 'Secure the Weakest Link' implies that:",
        "options": {
            "A": "A system’s overall security is determined by its most vulnerable component",
            "B": "Only the strongest security measures are needed",
            "C": "Security is not necessary for minor components",
            "D": "The most secure part of the system can protect the whole system"
        },
        "correct": "A"
    },
    {
        "question": "How is a 'Threat' defined in the context of system security?",
        "options": {
            "A": "An object, person, or entity that represents a danger to an asset",
            "B": "A weakness in the system’s defenses",
            "C": "A safeguard to prevent unauthorized access",
            "D": "A method for encrypting data"
        },
        "correct": "A"
    },
    {
        "question": "Which statement best defines a 'Vulnerability' in a system?",
        "options": {
            "A": "A weakness or fault in a system that could be exploited by an attacker",
            "B": "A deliberate attack on a system",
            "C": "A security policy that is too strict",
            "D": "An advanced encryption algorithm"
        },
        "correct": "A"
    },
    {
        "question": "What is meant by an 'Attack' in system security terminology?",
        "options": {
            "A": "An act or action that exploits a vulnerability in a system",
            "B": "A preventive security measure",
            "C": "A regular update of the system software",
            "D": "A backup strategy to recover data"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following are considered the three main components of system security?",
        "options": {
            "A": "Policy, Mechanism, and Assurance",
            "B": "Hardware, Software, and Network",
            "C": "Confidentiality, Integrity, and Availability",
            "D": "Prevention, Detection, and Recovery"
        },
        "correct": "A"
    },
    {
        "question": "In a company's financial process, the 'Separation of Duties' principle ensures that:",
        "options": {
            "A": "Different individuals handle purchase requests, approvals, and payment processing",
            "B": "A single employee manages all steps to maintain consistency",
            "C": "Only the finance officer is responsible for all transaction processes",
            "D": "The same person who approves a purchase can also process the payment"
        },
        "correct": "A"
    },
    {
        "question": "The Squid web proxy configuration example demonstrates which security principle?",
        "options": {
            "A": "Fail-Safe Defaults",
            "B": "Least Privilege",
            "C": "Economy of Mechanism",
            "D": "Open Design"
        },
        "correct": "A"
    },
    {
        "question": "What does the C.I.A. triad stand for in the context of information security?",
        "options": {
            "A": "Confidentiality, Integrity, and Availability",
            "B": "Control, Isolation, and Authentication",
            "C": "Compliance, Integrity, and Accessibility",
            "D": "Confidentiality, Inspection, and Assurance"
        },
        "correct": "A"
    },
    {
        "question": "Which secure platform is primarily used in enterprise environments to perform cryptographic operations and manage keys?",
        "options": {
            "A": "Hardware Security Module (HSM)",
            "B": "Trusted Platform Module (TPM)",
            "C": "Secure Element (SE)",
            "D": "Trusted Execution Environment (TEE)"
        },
        "correct": "A"
    },
    {
        "question": "Which hardware component is typically used in PCs for secure boot, disk encryption, and system integrity?",
        "options": {
            "A": "Hardware Security Module (HSM)",
            "B": "Trusted Platform Module (TPM)",
            "C": "Secure Element (SE)",
            "D": "Physically Unclonable Function (PUF)"
        },
        "correct": "B"
    },
    {
        "question": "What is the primary function of a Secure Element (SE)?",
        "options": {
            "A": "To serve as a tamper-resistant chip for secure transactions and authentication",
            "B": "To manage user account privileges in enterprise systems",
            "C": "To implement software-based encryption algorithms",
            "D": "To provide high-performance computing for servers"
        },
        "correct": "A"
    },
    {
        "question": "Hardware support for software security primarily provides which three mechanisms?",
        "options": {
            "A": "Protection, Isolation, and Attestation",
            "B": "Encryption, Compression, and Data Storage",
            "C": "Authentication, Backup, and Recovery",
            "D": "Networking, Processing, and Memory Management"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following provides a completely isolated execution space within the main processor to prodect sensitive code and data?",
        "options": {
            "A": "Trusted Execution Environment (TEE)",
            "B": "Trusted Platform Module (TPM)",
            "C": "Hardware Security Module (HSM)",
            "D": "Secure Element (SE)"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following is an example of a Trusted Execution Environment (TEE)",
        "options": {
            "A": "ARM TrustZone",
            "B": "Thales Luna HSM",
            "C": "Infineon TPM",
            "D": "Secure Element in smartcards"
        },
        "correct": "A"
    },
    {
        "question": "What is the primary purpose of Secure Boot and Firmware Integrity in hardware security?",
        "options": {
            "A": "To ensure that a system boots only with trusted software by verifying each component in a chain of trust",
            "B": "To increase the boot speed of the system",
            "C": "To allow users to install any operating system without restrictions",
            "D": "To provide a user-friendly graphical interface during startup"
        },
        "correct": "A"
    },
    {
        "question": "Which attack exploits variations in power consumption and timing differences to extract cryptographic keys from a device?",
        "options": {
            "A": "Differential Power Analysis (DPA)",
            "B": "Buffer Overflow Attack",
            "C": "SQL Injection",
            "D": "Man-in-the-Middle Attack"
        },
        "correct": "A"
    },
    {
        "question": "What type of random number generator is based on physical phenomena like thermal noise?",
        "options": {
            "A": "True Random Number Generator (TRNG)",
            "B": "Pseudo-Random Number Generator (PRNG)",
            "C": "Deterministic Random Generator",
            "D": "Cryptographically Secure PRNG"
        },
        "correct": "A"
    },
    {
        "question": "What purpose do Physically Unclonable Functions (PUFs) serve in hardware security?",
        "options": {
            "A": "They generate unique, device-specific keys based on inherent silicon variations",
            "B": "They accelerate cryptographic computations in software",
            "C": "They provide backup storage for encryption keys",
            "D": "They monitor system performance and thermal levels"
        },
        "correct": "A"
    },
    {
        "question": "Which countermeasure ensures that cryptographic operations take the same amount of time regardless of input, preventing timing attacks?",
        "options": {
            "A": "Constant-Time Execution",
            "B": "Stack Canaries",
            "C": "Address Space Layout Randomization (ASLR)",
            "D": "Data Execution Prevention (DEP)"
        },
        "correct": "A"
    },
    {
        "question": "In the context of hardware security, what is the purpose of 'masking'?",
        "options": {
            "A": "To randomize intermediate values during cryptographic operations to protect against power analysis",
            "B": "To hide the physical appearance of the hardware device",
            "C": "To provide user authentication through facial recognition",
            "D": "To enable encryption of stored data at rest"
        },
        "correct": "A"
    },
    {
        "question": "What role do shielding and sensors play as countermeasures in hardware security?",
        "options": {
            "A": "They detect tampering attempts such as probing or heating, protecting sensitive hardware components",
            "B": "They provide additional processing power for cryptographic operations",
            "C": "They help in debugging hardware malfunctions during development",
            "D": "They enable faster data transfer between hardware components"
        },
        "correct": "A"
    },
    {
        "question": "One advantage of implementing cryptographic algorithms at the RTL level is that it allows designers to optimize for:",
        "options": {
            "A": "Power, area, and performance",
            "B": "Graphical user interface design",
            "C": "User accessibility and interaction",
            "D": "Network connectivity and latency"
        },
        "correct": "A"
    },
    {
        "question": "Which hardware platforms are mentioned as suitable for implementing cryptographic algorithms at the RTL level?",
        "options": {
            "A": "ASIC and FPGA",
            "B": "CPU and GPU",
            "C": "HSM and TPM",
            "D": "Smartcards and SIM cards"
        },
        "correct": "A"
    },
    {
        "question": "What is the primary difference between a True Random Number Generator (TRNG) and a Pseudo-Random Number Generator (PRNG)?",
        "options": {
            "A": "A TRNG is based on physical phenomena and provides non-deterministic outputs, while a PRNG is deterministic and requires a secure seed",
            "B": "A TRNG is used only for encryption, while a PRNG is used for compression",
            "C": "A TRNG is slower than a PRNG due to complex algorithms, while a PRNG is hardware-based",
            "D": "A TRNG is software-based and a PRNG is hardware-based"
        },
        "correct": "A"
    },
    {
        "question": "Why are hardware security measures considered essential in addition to software-only security approaches?",
        "options": {
            "A": "Because hardware measures protect against physical attacks and tampering that software alone cannot prevent",
            "B": "Because hardware measures are easier to implement than software measures",
            "C": "Because software security measures are no longer relevant in modern systems",
            "D": "Because hardware security measures reduce the need for user authentication"
        },
        "correct": "A"
    },
    {
        "question": "Which security principle is violated when authentication tokens are cached for too long?",
        "options": {
            "A": "Fail-safe Defaults",
            "B": "Complete Mediation",
            "C": "Economy of Mechanism",
            "D": "Least Privilege"
        },
        "correct": "B"
    },
    {
        "question": "Having the same team responsible for writing code, testing it, and deploying it to production violates which security principle?",
        "options": {
            "A": "Least Privilege",
            "B": "Complete Mediation",
            "C": "Economy of Mechanism",
            "D": "Segregation (separation) of Duties"
        },
        "correct": "D"
    },
    {
        "question": "Which of the following is NOT an example of multi-factor authentication?",
        "options": {
            "A": "Using a PIN number with your debit card at an ATM",
            "B": "Using a password and answering a security question",
            "C": "Using fingerprint scan with a security token",
            "D": "Using a verification code sent to your phone along with your password"
        },
        "correct": "B"
    },
    {
        "question": "In authentication systems, which type of error is more dangerous from a security perspective?",
        "options": {
            "A": "Type-I error (false rejection)",
            "B": "Type-II error (false acceptance)",
            "C": "Both are equally dangerous",
            "D": "Neither poses a security risk"
        },
        "correct": "B"
    },
    {
        "question": "The Ping-of-Death attack is an example of what type of security attack?",
        "options": {
            "A": "Man-in-the-Middle (MitM)",
            "B": "Denial of Service (DoS)",
            "C": "Spoofing",
            "D": "Sniffing"
        },
        "correct": "B"
    },
    {
        "question": "Which Oracle statement best demonstrates Discretionary Access Control (DAC)?",
        "options": {
            "A": "GRANT SELECT ON grades TO PUBLIC;",
            "B": "CREATE ROLE lecturer;",
            "C": "GRANT UPDATE ON grades TO lecturer;",
            "D": "GRANT INSERT ON grades TO alice WITH GRANT OPTION;"
        },
        "correct": "D"
    },
    {
        "question": "In Linux file permissions, what does the command 'umask 0022' result in for newly created files?",
        "options": {
            "A": "rw-r--r--",
            "B": "rwxr-xr-x",
            "C": "rw-rw-rw-",
            "D": "rwxrwxrwx"
        },
        "correct": "A"
    },
    {
        "question": "How do SYN cookies mitigate SYN flood attacks?",
        "options": {
            "A": "By blocking all SYN packets from unknown sources",
            "B": "By encoding information in the initial sequence number to avoid allocating resources for each connection attempt",
            "C": "By sending special cookies to verify legitimate browsers",
            "D": "By limiting the rate of incoming SYN packets"
        },
        "correct": "B"
    },
    {
        "question": "Which security principle is primarily concerned with keeping mechanisms shared between users to a minimum?",
        "options": {
            "A": "Economy of Mechanism",
            "B": "Complete Mediation",
            "C": "Least Common Mechanism",
            "D": "Psychological Acceptability"
        },
        "correct": "C"
    },
    {
        "question": "What type of security control is a firewall considered?",
        "options": {
            "A": "Detection control",
            "B": "Prevention control",
            "C": "Recovery control",
            "D": "Deterrent control"
        },
        "correct": "B"
    },
    {
        "question": "What is the primary operational mechanism of a honeypot as a security control?",
        "options": {
            "A": "Detection",
            "B": "Prevention",
            "C": "Recovery",
            "D": "Correction"
        },
        "correct": "A"
    },
    {
        "question": "Which of these is likely to be a set-uid program in Linux?",
        "options": {
            "A": "ls (list directory contents)",
            "B": "cd (change directory)",
            "C": "mount (attach a filesystem)",
            "D": "pwd (print working directory)"
        },
        "correct": "C"
    },
    {
        "question": "In a UDP Ping Pong Attack exploiting Echo (port 7) and CHARGEN (port 19) services, what would the attacker use as the source port in the spoofed packet?",
        "options": {
            "A": "Port 7 (Echo)",
            "B": "Port 19 (CHARGEN)",
            "C": "A random high port number",
            "D": "Port 80 (HTTP)"
        },
        "correct": "A"
    },
    {
        "question": "Which is NOT a valid defense against ARP spoofing attacks?",
        "options": {
            "A": "Using static ARP entries",
            "B": "Using a hub instead of a switch",
            "C": "Implementing port security on switches",
            "D": "Using tools like Arpwatch"
        },
        "correct": "B"
    },
    {
        "question": "Which principle relates to designing security systems that default to a secure state when failures occur?",
        "options": {
            "A": "Economy of Mechanism",
            "B": "Fail-safe Defaults",
            "C": "Complete Mediation",
            "D": "Open Design"
        },
        "correct": "B"
    },
    {
        "question": "What distinguishes Attribute-Based Access Control (ABAC) from Role-Based Access Control (RBAC)?",
        "options": {
            "A": "ABAC can make access decisions based on environmental conditions like time of day",
            "B": "ABAC is simpler to implement than RBAC",
            "C": "RBAC provides more granular control than ABAC",
            "D": "RBAC can handle more complex permission structures"
        },
        "correct": "A"
    },
    {
        "question": "Installing security patches as soon as they are released is primarily what type of security control?",
        "options": {
            "A": "Detection",
            "B": "Prevention",
            "C": "Recovery",
            "D": "Compensating"
        },
        "correct": "B"
    },
    {
        "question": "The 'Defense in Depth' security principle refers to:",
        "options": {
            "A": "Using the most complex security mechanisms possible",
            "B": "Implementing multiple layers of security controls",
            "C": "Focusing resources on defending the most critical assets",
            "D": "Training users to defend themselves against attacks"
        },
        "correct": "B"
    },
    {
        "question": "When Bob (member of groups tutors and staff) creates a file in a directory owned by Alice with permissions drwxrwxr-x, what will be the default group ownership of the file?",
        "options": {
            "A": "Alice's primary group",
            "B": "The same group as the directory (staff)",
            "C": "Bob's primary group (tutors)",
            "D": "The root group"
        },
        "correct": "C"
    },
    {
        "question": "Which access control model would be most appropriate for implementing a policy that restricts access based on the time of day and user location?",
        "options": {
            "A": "Discretionary Access Control (DAC)",
            "B": "Mandatory Access Control (MAC)",
            "C": "Role-Based Access Control (RBAC)",
            "D": "Attribute-Based Access Control (ABAC)"
        },
        "correct": "D"
    },
    {
        "question": "What Linux command would you use to view the extended ACLs of a file?",
        "options": {
            "A": "ls -l",
            "B": "getfacl",
            "C": "chmod",
            "D": "lsacl"
        },
        "correct": "B"
    },
    {
        "question": "Which TCP/IP protocol is used by the ARP spoofing attack?",
        "options": {
            "A": "TCP",
            "B": "UDP",
            "C": "ICMP",
            "D": "ARP"
        },
        "correct": "D"
    },
    {
        "question": "In a SYN flood attack, what TCP flag is set in the packets sent by the attacker?",
        "options": {
            "A": "ACK",
            "B": "SYN",
            "C": "FIN",
            "D": "RST"
        },
        "correct": "B"
    },
    {
        "question": "Which access control approach would be most appropriate for a military organization with strict hierarchical security classifications?",
        "options": {
            "A": "Discretionary Access Control (DAC)",
            "B": "Mandatory Access Control (MAC)",
            "C": "Role-Based Access Control (RBAC)",
            "D": "Attribute-Based Access Control (ABAC)"
        },
        "correct": "B"
    },
    {
        "question": "If an attacker wants to conduct a UDP Ping Pong attack between two victim servers, what service would they likely target as the destination in their spoofed packet?",
        "options": {
            "A": "DNS (port 53)",
            "B": "CHARGEN (port 19)",
            "C": "HTTP (port 80)",
            "D": "SMTP (port 25)"
        },
        "correct": "B"
    },
    {
        "question": "What effect does the SUID (Set User ID) permission have when applied to an executable file?",
        "options": {
            "A": "The file executes with the permissions of the file owner, not the user running it",
            "B": "The file executes normally, using the permissions of the user running it",
            "C": "The file can only be executed by the root user",
            "D": "The file cannot be executed at all"
        },
        "correct": "A"
    },
    {
        "question": "Which special permission allows executable files to run with the permissions of the group owner instead of the user running the file?",
        "options": {
            "A": "SGID (Set Group ID)",
            "B": "SUID (Set User ID)",
            "C": "Sticky Bit",
            "D": "Execute permission"
        },
        "correct": "A"
    },
    {
        "question": "What effect does the SGID (Set Group ID) permission have on directories?",
        "options": {
            "A": "New files created in the directory inherit the group ownership of the directory instead of the creating user's primary group",
            "B": "Only the group owner can delete files in the directory",
            "C": "The directory becomes executable by anyone",
            "D": "The directory is hidden from users who are not in the group"
        },
        "correct": "A"
    },
    {
        "question": "Which special permission prevents users from deleting files in a directory unless they own the file, even if they have write permissions on the directory?",
        "options": {
            "A": "Sticky Bit",
            "B": "SUID (Set User ID)",
            "C": "SGID (Set Group ID)",
            "D": "Execute permission"
        },
        "correct": "A"
    },
    {
        "question": "What is the primary function of the Sticky Bit when set on a directory?",
        "options": {
            "A": "Only the file owner, directory owner, or root can delete files inside the directory",
            "B": "Files created in the directory inherit the directory’s owner",
            "C": "Files inside the directory can only be executed, not modified",
            "D": "All files in the directory become read-only"
        },
        "correct": "A"
    },
    {
        "question": "What does execute permission (x) do when applied to a directory?",
        "options": {
            "A": "It allows users to enter (cd into) the directory",
            "B": "It allows users to create new files in the directory",
            "C": "It allows users to delete files inside the directory",
            "D": "It allows users to list the files in the directory"
        },
        "correct": "A"
    },
    {
        "question": "Which permission is required to list the contents of a directory?",
        "options": {
            "A": "Read (r)",
            "B": "Write (w)",
            "C": "Execute (x)",
            "D": "SUID (Set User ID)"
        },
        "correct": "A"
    },
    {
        "question": "What happens if a user has execute (x) permission on a directory but does not have read (r) permission?",
        "options": {
            "A": "The user can enter (cd into) the directory but cannot list its contents",
            "B": "The user can list the directory contents but cannot enter it",
            "C": "The user can create files in the directory but cannot execute files inside it",
            "D": "The user cannot access the directory at all"
        },
        "correct": "A"
    },
    {
        "question": "Which combination of permissions is required to delete a file inside a directory?",
        "options": {
            "A": "Write (w) and Execute (x) on the directory",
            "B": "Write (w) and Read (r) on the file",
            "C": "Execute (x) and Read (r) on the directory",
            "D": "Write (w) and Execute (x) on the file"
        },
        "correct": "A"
    },
    {
        "question": "If a user has write (w) permission on a file but does not have write permission on the containing directory, what happens when they try to delete the file?",
        "options": {
            "A": "The file cannot be deleted because deleting requires write permission on the directory",
            "B": "The file is deleted normally because the user has write permission on it",
            "C": "The file becomes hidden instead of being deleted",
            "D": "The file is moved to a temporary location before deletion"
        },
        "correct": "A"
    },
    {
        "question": "What happens if a file has the SUID bit set but does not have execute permissions?",
        "options": {
            "A": "The SUID bit has no effect because execute permission is required",
            "B": "The file executes with the owner’s permissions as intended",
            "C": "The file executes with the group’s permissions instead",
            "D": "The file is deleted automatically"
        },
        "correct": "A"
    },
    {
        "question": "How can a user remove the SUID bit from a file while keeping all other permissions unchanged?",
        "options": {
            "A": "chmod u-s filename",
            "B": "chmod g-s filename",
            "C": "chmod o-s filename",
            "D": "chmod -x filename"
        },
        "correct": "A"
    },
    {
        "question": "What happens if a directory has both the SGID and Sticky Bit set?",
        "options": {
            "A": "New files inherit the group ownership of the directory, and only file owners can delete their files",
            "B": "All users can delete files in the directory",
            "C": "Files in the directory cannot be executed",
            "D": "New files inherit the owner of the directory"
        },
        "correct": "A"
    },
    {
        "question": "What vulnerability does the Meltdown attack exploit?",
        "options": {
            "A": "Software bugs in operating systems",
            "B": "Flaws in hardware protection mechanisms in CPUs",
            "C": "Network protocol weaknesses",
            "D": "User authentication bypasses"
        },
        "correct": "B"
    },
    {
        "question": "Which side-channel technique is used in the Meltdown attack?",
        "options": {
            "A": "PRIME+PROBE",
            "B": "EVICT+TIME",
            "C": "FLUSH+RELOAD",
            "D": "DRAIN+CHECK"
        },
        "correct": "C"
    },
    {
        "question": "Why is accessing data from CPU cache faster than from main memory?",
        "options": {
            "A": "(A) The CPU cache is physically closer to the processor",
            "B": "(B) The cache uses faster memory technology",
            "C": "(C) The main memory is deliberately slowed down",
            "D": "Both A and B"
        },
        "correct": "D"
    },
    {
        "question": "What does the FLUSH+RELOAD technique primarily measure?",
        "options": {
            "A": "CPU temperature during operations",
            "B": "Memory access times to determine if data is cached",
            "C": "Power consumption variations",
            "D": "Clock cycles for arithmetic operations"
        },
        "correct": "B"
    },
    {
        "question": "Why is spacing of 4096 bytes used between array elements in the side channel attack?",
        "options": {
            "A": "To match the page size of virtual memory",
            "B": "To ensure elements are in different cache blocks",
            "C": "To simplify the array addressing calculations",
            "D": "To increase memory allocation efficiency"
        },
        "correct": "B"
    },
    {
        "question": "What CPU optimization technique is exploited in the Meltdown attack?",
        "options": {
            "A": "Out-of-order execution",
            "B": "Branch prediction",
            "C": "Hyperthreading",
            "D": "Register renaming"
        },
        "correct": "A"
    },
    {
        "question": "What happens when a user-level program attempts to directly access kernel memory?",
        "options": {
            "A": "The program gets elevated privileges",
            "B": "The kernel encrypts the data before providing it",
            "C": "An exception (SIGSEGV) is raised and the program typically crashes",
            "D": "The CPU automatically redirects to a virtual memory space"
        },
        "correct": "C"
    },
    {
        "question": "What function pair is used in the lab to implement exception handling in C?",
        "options": {
            "A": "try() and catch()",
            "B": "sigsetjmp() and siglongjmp()",
            "C": "setjmp() and longjmp()",
            "D": "try_except() and handle_except()"
        },
        "correct": "B"
    },
    {
        "question": "In the Meltdown attack, why is it important to have the target secret data cached?",
        "options": {
            "A": "To make the data encryption weaker",
            "B": "To speed up loading of the data into registers, allowing more out-of-order execution",
            "C": "To prevent the operating system from detecting the attack",
            "D": "To bypass virtual memory protection"
        },
        "correct": "B"
    },
    {
        "question": "What statistical technique is used to improve the accuracy of the Meltdown attack?",
        "options": {
            "A": "Bayesian probability calculations",
            "B": "Running the attack multiple times and keeping a frequency score for each possible value",
            "C": "Machine learning algorithms",
            "D": "Cryptographic hash comparisons"
        },
        "correct": "B"
    },
    {
        "question": "What operating system protection feature does Meltdown bypass?",
        "options": {
            "A": "User account permissions",
            "B": "File system access controls",
            "C": "Kernel memory isolation from user space",
            "D": "Network traffic encryption"
        },
        "correct": "C"
    },
    {
        "question": "Why does the CPU cache state remain affected even after out-of-order execution is discarded?",
        "options": {
            "A": "The cache is in a separate security domain",
            "B": "CPU designers forgot to clear cache effects when discarding speculative execution",
            "C": "Cache changes are permanent by design",
            "D": "The operating system requires it for performance reasons"
        },
        "correct": "B"
    },
    {
        "question": "What does the CACHE_HIT_THRESHOLD value represent in the lab code?",
        "options": {
            "A": "Maximum number of cache hits allowed",
            "B": "CPU temperature threshold during cache operations",
            "C": "Time threshold to distinguish between cache hits and misses",
            "D": "Maximum allowed memory allocation"
        },
        "correct": "C"
    },
    {
        "question": "Which type of computers would be immune to the Meltdown attack as described in the lab?",
        "options": {
            "A": "Computers running Linux",
            "B": "Computers with AMD processors",
            "C": "Computers with multiple CPU cores",
            "D": "Computers with encrypted memory"
        },
        "correct": "B"
    },
    {
        "question": "Which of the following statements accurately describes the scope and effect of the umask command when invoked?",
        "options": {
            "A": "It applies to all directories for the user issuing it, and the effect lasts for the duration of the current session",
            "B": "It applies per user, persists across sessions, and is not specific to any directory",
            "C": "It applies to all directories, globally for all users, and persists across future sessions",
            "D": "It applies to specific directories, but affects all users and lasts for the duration of the session"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following commands sets the default file creation permissions to readable and writable for the owner, readable for the group and no permissions for others?",
        "options": {
            "A": "umask 026",
            "B": "umask 740",
            "C": "umask 033",
            "D": "umask 020"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following is different from the others in terms of its main functionality?",
        "options": {
            "A": "nmap",
            "B": "wireshark",
            "C": "tcpdump",
            "D": "urlsnarf"
        },
        "correct": "A"
    },
    {
        "question": "(lab 2-3) Which of the following best describes promiscuous mode in network interfaces?",
        "options": {
            "A": "It enables a network interface to capture network traffic with any destination MAC address.",
            "B": "It enables a network interface to capture network traffic with any source MAC address, but with a destination MAC address that matches that of the interface.",
            "C": "It enables the interface to capture all broadcast packets.",
            "D": "It enables the interface to send packets with any (spoofed) source MAC address."
        },
        "correct": "A"
    },
    {
        "question": "(lab 2-3) Which one of the following Scapy instructions sends a spoofed ping request packet from 192.168.9.2 to 192.168.68.12 with a forged source IP of 3.1.7.0?",
        "options": {
            "A": "send(IP(src=\"3.1.7.0\", dst=\"192.168.68.12\")/ICMP())",
            "B": "send(IP(src=\"192.168.9.2\", dst=\"192.168.68.12\")/IP(src=\"3.1.7.0\")/UDP()/ICMP())",
            "C": "send(IP(src=\"192.168.9.2\", dst=\"192.168.68.12\")/IP(src=\"3.1.7.0\")/ICMP())",
            "D": "send(IP(src=\"3.1.7.0\", dst=\"192.168.68.12\")/UDP()/ICMP())"
        },
        "correct": "A"
    },
    {
        "question": "What is a type 1 error?",
        "options": {
            "A": "false acceptance",
            "B": "false rejection",
            "C": "true positive",
            "D": "true negitive"
        },
        "correct": "B"
    },
    {
        "question": "What is a type 2 error?",
        "options": {
            "A": "false acceptance",
            "B": "false rejection",
            "C": "true positive",
            "D": "true negitive"
        },
        "correct": "A"
    },
    {
        "question": "What best describes the Bell-LaPadula model",
        "options": {
            "A": "no read up, no write down",
            "B": "no write up, no read up",
            "C": "no read down, no read up",
            "D": "Mandatory access control"
        },
        "correct": "A"
    },
    {
        "question": "What best describes the Biba model",
        "options": {
            "A": "no read down, no write up",
            "B": "no write up, no execute down",
            "C": "no read down, no read up",
            "D": "Mandatory access control"
        },
        "correct": "A"
    },
    {
        "question": "What best describes the differences between the Biba model and the Bell-LaPadula",
        "options": {
            "A": "Biba model focuses on integrity preventing unauthorthorized modification where Bell-LaPudula focuses on preventing unauthorized access and disclosure of information",
            "B": "Bell-LaPudula model focuses on integrity preventing unauthorthorized modification where Biba focuses on preventing unauthorized access and disclosure of information",
            "C": "no read down, no read up",
            "D": "Both are very similar"
        },
        "correct": "A"
    },
    {
        "question": "What are some issues with MAC",
        "options": {
            "A": "Information tends to become over classified",
            "B": "No protection against violations that allow information flow through indirect means ( such as covert channels )",
            "C": "All are true",
            "D": "None are true"
        },
        "correct": "C"
    },
    {
        "question": "What does the following line do in the context of an Oracle database (ARMAN IS EVIL FOR THIS) - GRANT SELECT ON patient_info TO doctor;",
        "options": {
            "A": "It allows a user of role DOCTOR to read patient_info without being able to modify it",
            "B": "It allows a user of role DOCTOR to read and modify patient_info",
            "C": "It allows the user DOCTOR to read patient_info",
            "D": "It allows a user of role DOCTOR to read and modify patient_info but not delete"
        },
        "correct": "A"
    },
    {
        "question": "What does the following line do in the context of an Oracale database - GRANT CONNECT TO doctor;",
        "options": {
            "A": "It allows users of the role DOCTOR to be able to log in and create a session",
            "B": "It allows users of the role DOCTOR to be able to create new roles and permissions",
            "C": "It uhuauhuhuahahauauaaaaaaaaaahhhhh!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            "D": "None are true"
        },
        "correct": "A"
    },
    {
        "question": "What best describes what chown does",
        "options": {
            "A": "changes the ownership of a file, can also change the group ownership",
            "B": "changes the permissions of a file",
            "C": "changes the ACL of a file",
            "D": "None are true"
        },
        "correct": "A"
    },
    {
        "question": "Which is true in the context of converting special permissions to numeric representation",
        "options": {
            "A": "setuid = 4, setgid = 2, sticky bit = 1",
            "B": "setuid = 1, setgid = 2, sticky bit = 4",
            "C": "setuid = 2, setgid = 1, sticky bit = 4",
            "D": "None are true"
        },
        "correct": "A"
    },
    {
        "question": "What digit represents special permissions in 7777",
        "options": {
            "A": "first digit",
            "B": "seccond digit",
            "C": "last digit",
            "D": "sourdough"
        },
        "correct": "A"
    },
    {
        "question": "Which best describes the typical behaviour of TCP",
        "options": {
            "A": "the client sends a SYN packet, the host sends a SYN ACK packet, the client then sends an ACK packet. Either the host or the client then sends a FIN packet when communication is finnished.",
            "B": "the host sends a SYN packet, the host sends a SYN ACK packet, the client then sends an ACK packet. Host then sends a FIN packet when communication is finnished.",
            "C": "the client sends a SYN packet, the host sends a SYN ACK packet, the client then sends an ACK packet. Either the host or the client then sends a RST packet when communication is finnished.",
            "D": "sourdough"
        },
        "correct": "A"
    },
    {
        "question": "What is the goal of ARP spoofing",
        "options": {
            "A": "Session hijacking",
            "B": "DOS",
            "C": "MITM",
            "D": "All are true"
        },
        "correct": "D"
    },
    {
        "question": "Which of the following are valid defences for ARP spoofing (not detection)",
        "options": {
            "A": "Static ARP table and port security",
            "B": "Arpwatch",
            "C": "XARP",
            "D": "All are true"
        },
        "correct": "A"
    },
    {
        "question": "Which one of the following statements is correct?",
        "options": {
            "A": "An authentication method that has no type-I error rate at all but has 10% type-II error rate is more dangerous than an authentication method that has 10% type-I error rate but no typeII errors.",
            "B": "Different users that are successfully authenticated can be thought of as having the same level of authorisation.",
            "C": "Using your student ID card to tap and unlock a door on campus is an example of multi-factor authentication.",
            "D": " 2-factor authentication is more secure than single-factor authentication because it results in mutual authentication."
        },
        "correct": "A"
    },
    {
        "question": "What does GRANT INSERT ON grades TO alice WITH GRANT OPTION; do?",
        "options": {
            "A": "it means that alice can pass the INSERT privilege to other roles or users at their discretion",
            "B": "it means that alice can only insert new entries to grades",
            "C": "it means that alice can grant the role OPTION to other users",
            "D": "all are true"
        },
        "correct": "A"
    },
    {
        "question": "in the context of acl's how would you give the user user1 full permissions?",
        "options": {
            "A": "setfacl -m u:user1:rwx filename",
            "B": "setacl -l u:user1:rwx filename",
            "C": "setfacl u:user1:rwx filename",
            "D": "getfacl o:user1:rwx filename"
        },
        "correct": "A"
    },
    {
        "question": "in the context of acl's how would you remove an acl entry for user1 ( say setfacl -m was previously run on user1 )",
        "options": {
            "A": "setfacl -x u:user1 filename",
            "B": "setacl -l u:user1:rwx filename",
            "C": "setfacl -l u:user1:0 filename",
            "D": "getfacl o:user1:rwx filename"
        },
        "correct": "A"
    },
    {
        "question": "in the context of acl's how would you completly clear all acl entries",
        "options": {
            "A": "setfacl -b filename",
            "B": "setacl -m 0 filename",
            "C": "setfacl -l u:user1:0 filename",
            "D": "getfacl o:user1:rwx filename"
        },
        "correct": "A"
    },
    {
        "question": "Which one of the following attacks makes use of IP spoofing?",
        "options": {
            "A": "SYN Flood",
            "B": "Ping of Death",
            "C": "Reflected Cross-Site Scripting (XSS)",
            "D": "CAM Table Exhaustion"
        },
        "correct": "A"
    },
    {
        "question": "Which one of the following is NOT a way in which honeypots help defend against attacks?",
        "options": {
            "A": "Preventing data exfilteration",
            "B": "Vulnerability Identification",
            "C": "Decoy and Distraction",
            "D": "CAM Table Exhaustion"
        },
        "correct": "A"
    },
    {
        "question": "how good are you at gambling >:)",
        "options": {
            "A": "maybe this",
            "B": "maybe this",
            "C": "or this one",
            "D": "not this one"
        },
        "correct": "A"
    },
    {
        "question": "The result of the command ls -l on which one of the following files is most likely to show the permissions -rwsr-xr-x",
        "options": {
            "A": "/bin/chown",
            "B": "/etc/passwd",
            "C": "/bin/passwd",
            "D": "/bin/useradd"
        },
        "correct": "C"
    },
    {
        "question": "Suppose you have read write and execute perms on a directory, which one of the following operations are you not guaranteed to be able to perform",
        "options": {
            "A": "Rename the directory",
            "B": "Create a file inside the directory",
            "C": "Create a subdirectory inside the directory",
            "D": "List the contents of the directory"
        },
        "correct": "A"
    },
    {
        "question": "Which one of the following is NOT a defence against ARP spoofing",
        "options": {
            "A": "Configuring devices to ignore all broadcast ARP requests for IP to MAC resolution",
            "B": "Dropping unsolicited ARP replies at the switch",
            "C": "Dropping ARP replies taht do not match DCHCP assigned IP MAC bindings",
            "D": "Restricting the set of allowed MAC addresses on an interface of a switch"
        },
        "correct": "A"
    },
    {
        "question": "What best describes reflection and amplification attacks",
        "options": {
            "A": "An unwilling intermediary is used to deliver the attack traffic",
            "B": "DNS is almost always used for DDOS attacks",
            "C": "The intermediary will deliver a response which will go to the attacker",
            "D": "Reflectors respond to the attacker"
        },
        "correct": "A"
    },
    {
        "question": "What best describes NTP",
        "options": {
            "A": "It redirects a particular payload to a victim",
            "B": "It is used to synchronize clocks each other",
            "C": "It is used for file transfer",
            "D": "It is an outdated protocol that is rarely used anymore"
        },
        "correct": "B"
    },
    {
        "question": "What best describes DNS",
        "options": {
            "A": "It translates human readable domain names to IP addresses",
            "B": "It is used for file transfer",
            "C": "It is used for google search",
            "D": "It is an outdated protocol that is rarely used anymore"
        },
        "correct": "A"
    },
    {
        "question": "What best describes SNMP",
        "options": {
            "A": "It is used for monitoring and managing network devices",
            "B": "There are many different versions of SNMP that are all widely used",
            "C": "It is used to convert IP addresses to MAC addresses at the router",
            "D": "SNMP is used for file transfer"
        },
        "correct": "A"
    },
    {
        "question": "What best describes SSDP",
        "options": {
            "A": "It is a text based protocol based on HTTPU",
            "B": "It is impossible to use for DDOS attacks",
            "C": "It usually opperates on port 80",
            "D": "It is used for monitoring network devices"
        },
        "correct": "A"
    },
    {
        "question": "What is the monlist command assosiated with",
        "options": {
            "A": "NTP",
            "B": "FTP",
            "C": "DNS",
            "D": "SNMP"
        },
        "correct": "A"
    },
    {
        "question": "What are potential countermeasures to NTP amplification attacks",
        "options": {
            "A": "Filter port 123 on the client",
            "B": "Filter port 80 on the client",
            "C": "Monitor DNS traffic",
            "D": "Get Arman to set up an NTP server, nobody will be able to use it :)"
        },
        "correct": "A"
    },
    {
        "question": "What does TLD stand for",
        "options": {
            "A": "Top level domain",
            "B": "Transmission line driver",
            "C": "Trusted logic daemon",
            "D": "Thread locking directive"
        },
        "correct": "A"
    },
    {
        "question": "Are firewalls useful for web application security",
        "options": {
            "A": "No, as almost all applications use port 80/443",
            "B": "No, HTTPS is enough",
            "C": "Yes, web application deals with layer 7 of the OSI model",
            "D": "Yes, firewalls are always useful"
        },
        "correct": "A"
    },
    {
        "question": "What is an example of a web application vulnerability",
        "options": {
            "A": "XSS",
            "B": "DOS",
            "C": "FTP",
            "D": "DNS"
        },
        "correct": "A"
    },
    {
        "question": "What best describes reflected XSS",
        "options": {
            "A": "An XSS payload it inserted into the URL that a victim clicks on",
            "B": "Like the Samy worm, a payload is executed on the loading of a specific page",
            "C": "An attacker uses some form of MITM attack in order to replace a legit http request with a malicious one",
            "D": "Arman"
        },
        "correct": "A"
    },
    {
        "question": "What can an externally facing firewall not protect against",
        "options": {
            "A": "Malicious insiders",
            "B": "Connections that do not pass through the firewall",
            "C": "Attacks that happen within the LAN",
            "D": "All of the above and below"
        },
        "correct": "D"
    },
    {
        "question": "What are the core functions of a firewall",
        "options": {
            "A": "Filtering",
            "B": "Proxying",
            "C": "Logging",
            "D": "All of the above and below"
        },
        "correct": "D"
    },
    {
        "question": "What is in most cases a stronger kind of firewall",
        "options": {
            "A": "A stateful firewall",
            "B": "A stateless firewall",
            "C": "or this one",
            "D": "not this one"
        },
        "correct": "A"
    },
    {
        "question": "When implementing a DMZ multiple firewalls are usually used, which of the following is true",
        "options": {
            "A": "Each firewall should be configured identically and use the same software",
            "B": "One firewall is responsible for controlling traffic between the DMZ and the internet",
            "C": "Second firewall controls traffic between protected network and the DMZ",
            "D": "All of the above and below"
        },
        "correct": "D"
    },
    {
        "question": "What best describes a reverse firewall",
        "options": {
            "A": "It protects an external network from attacks originating from within",
            "B": "Protects web servers from attacks",
            "C": "ISP's use reverse firewalls to prevent customers from attacking the ISP",
            "D": "All of the above and below"
        },
        "correct": "A"
    },
    {
        "question": "What best describes firewall policies",
        "options": {
            "A": "SYSSP",
            "B": "FWP",
            "C": "SFWP",
            "D": "OWASP"
        },
        "correct": "A"
    },
    {
        "question": "Which is true",
        "options": {
            "A": "Regular users should be able to connect to a firewall",
            "B": "Nobody but administrators should be able to connect to the firewall",
            "C": "Firewalls should allow for direct access from the internet to any computer behind the firewall",
            "D": "Let Arman set up the firewall, this will prevent all potential hacks because the firewall wont let any traffic through"
        },
        "correct": "B"
    },
    {
        "question": "Which is true",
        "options": {
            "A": "Firewalls should keep the list of rules as short as possible around 30, no more than 50",
            "B": "Regular users should be able to connect to a firewall",
            "C": "Firewalls should allow for direct access from the internet to any computer behind the firewall",
            "D": "Firewalls protect external networks from attacks originating from within"
        },
        "correct": "A"
    },
    {
        "question": "What is not a capability of iptables",
        "options": {
            "A": "Stateful inspection",
            "B": "Time quota and connection rate based filtering and restrictions",
            "C": "Packet forwarding",
            "D": "High performance for high volume, iptables is designed to handle large amounts of traffic"
        },
        "correct": "D"
    },
    {
        "question": "Which keyword for iptables stops further processing and hands the packet over to the application it is meant for",
        "options": {
            "A": "ACCEPT",
            "B": "DROP",
            "C": "SNAT",
            "D": "MASQUERADE"
        },
        "correct": "A"
    },
    {
        "question": "Which keyword for iptables stops further processing and blocks the packet",
        "options": {
            "A": "DROP",
            "B": "LOG",
            "C": "REJECT",
            "D": "SNAT"
        },
        "correct": "A"
    },
    {
        "question": "Which iptables keyword drops the packet but performs further actions upon receiving",
        "options": {
            "A": "REJECT",
            "B": "DROP",
            "C": "LOG",
            "D": "DNAT"
        },
        "correct": "A"
    },
    {
        "question": "Which iptables keyword modifys the source IP address of the outgoing packet",
        "options": {
            "A": "SNAT",
            "B": "MASQUERADE",
            "C": "Both options",
            "D": "None of these"
        },
        "correct": "A"
    },
    {
        "question": "What are the goals of an IDPS",
        "options": {
            "A": "Monitoring an logging",
            "B": "Response",
            "C": "Accountability",
            "D": "All"
        },
        "correct": "D"
    },
    {
        "question": "Are IDPSs stateless",
        "options": {
            "A": "No",
            "B": "Yes",
            "C": "",
            "D": ""
        },
        "correct": "A"
    },
    {
        "question": "What are some different aproaches IDPS takes",
        "options": {
            "A": "Traffic rate monitoring",
            "B": "IP packet reassembly",
            "C": "Protocol state tracking",
            "D": "All"
        },
        "correct": "D"
    },
    {
        "question": "What does NDR stand for",
        "options": {
            "A": "Network detection and response",
            "B": "Network data recorder",
            "C": "Network device registry",
            "D": "All"
        },
        "correct": "A"
    },
    {
        "question": "What does IDPS stand for",
        "options": {
            "A": "Intrusion detection and prevention system",
            "B": "Intelligent data processing system",
            "C": "Indexed database partitioning system",
            "D": "Isotopic density preiction software"
        },
        "correct": "A"
    },
    {
        "question": "What does EDR stand for",
        "options": {
            "A": "Endpoint detection and response",
            "B": "Enhanced data replication",
            "C": "Event driven response",
            "D": "Enterprise data router"
        },
        "correct": "A"
    },
    {
        "question": "What does HIDPS stand for",
        "options": {
            "A": "Host based intrusion detection and prevention system",
            "B": "Hybrid intrusion detection and prevention system",
            "C": "Hydrodynamic impact dissipation prediction system",
            "D": "Insert Arman slander"
        },
        "correct": "A"
    },
    {
        "question": "What is tripwire",
        "options": {
            "A": "It is a tool focused on file integrity monitoring (FIM) and security configuration management (SCM)",
            "B": "It is responsible for setting firewall policies",
            "C": "Arman sourdough",
            "D": "A tool for testing tdijfj  jif arman uhh arman"
        },
        "correct": "A"
    },
    {
        "question": "What is a honeypot",
        "options": {
            "A": "Honeyports are real or emulated vulnerable systems ready to be attacked",
            "B": "A network optimisation tool that dynamically reroutes excess traffic to idle servers to reduce latency during peak usage hours",
            "C": "Armans vm",
            "D": "pooh"
        },
        "correct": "A"
    },
    {
        "question": "What are some of the benefits of honeypots",
        "options": {
            "A": "After identification of attacker all data captured can be used in a legal procedure",
            "B": "Improves overall network speed by offloading background traffic to decoy systems",
            "C": "Reduces the need for endpoint protection software on real systems",
            "D": "All of these are true"
        },
        "correct": "A"
    },
    {
        "question": "What are some of the benefits of honeypots",
        "options": {
            "A": "Identification and classification of attacks",
            "B": "detailed information of attack tools and strategies",
            "C": "A honeypot deployed in a productive environment may lure an attacker away from the real production systems",
            "D": "All"
        },
        "correct": "D"
    },
    {
        "question": "Which of the following is true for a client honeypot",
        "options": {
            "A": "None of these",
            "B": "arman",
            "C": "Honeypot is accesable to the internet",
            "D": "Simulate server-side services"
        },
        "correct": "A"
    },
    {
        "question": "Which of the following is true for a server honeypot",
        "options": {
            "A": "None of these",
            "B": "ARman",
            "C": "Honey initiates and interacts with servers",
            "D": "Simulate client browser"
        },
        "correct": "A"
    },
    {
        "question": "What are some attributes and actions assosiated with low interaction honeypots",
        "options": {
            "A": "Attacker activity is limited to the level of emulation by the honeypot",
            "B": "Nothing is emulated. Real services applications and OS's",
            "C": "Capture extensive information, but high risk and time intensive to maintain",
            "D": "ar man"
        },
        "correct": "A"
    },
    {
        "question": "What are some attributes and actions assosiated with high interaction honeypots",
        "options": {
            "A": "Nothing is emulated, real services applications and OS's",
            "B": "Emulates services applications and OS's",
            "C": "Low risk, easy to deploy / maintain but capture limited information",
            "D": "Attacker activity is limited to the level of emulation by the honeypot"
        },
        "correct": "A"
    },
    {
        "question": "What are some attributes and actions assosiated with production honeypots",
        "options": {
            "A": "All of these",
            "B": "Mainly used by companies / corporations",
            "C": "Placed inside production network with other servers",
            "D": "Usually low interaction"
        },
        "correct": "A"
    },
    {
        "question": "What are some attributes and actions assosiated with research honeypots",
        "options": {
            "A": "All of these",
            "B": "Complex to maintain / deploy",
            "C": "Capture extensive information",
            "D": "Primarily used for research, military, or government organisations"
        },
        "correct": "A"
    },
    {
        "question": "What are some plausable locations for a honeypot",
        "options": {
            "A": "In front of the firewall",
            "B": "DMZ",
            "C": "Behind the firewall (Intranet)",
            "D": "All of these are plausable"
        },
        "correct": "D"
    },
    {
        "question": "What one of these are true regarding honeypots",
        "options": {
            "A": "None of these",
            "B": "All of these",
            "C": "The location of the honeypot does not matter as long as an attacker gets 'funneled' toward it",
            "D": "They are identical to a vulnerable system"
        },
        "correct": "A"
    },
    {
        "question": "What is a network telescope",
        "options": {
            "A": "A network telescope observes traffic targeting unused address space of the network",
            "B": "A tool used to scan the internet for open ports and services",
            "C": "A DNS query accelerator that uses idle subnets to boost response time",
            "D": "A distributed system for redirecting excess network load during peak usage"
        },
        "correct": "A"
    },
    {
        "question": "What are honeytokens",
        "options": {
            "A": "Honeytokens are honeypots but in the form of software or data, such as a fake account, a database entry, etc",
            "B": "Honeytokens are honeypots but instead of existing as a single machine, it exists as a virtual machine contained inside of a production server",
            "C": "Honeytokens is a third party tool, used by organisations as a one size fits all software solution to installing and maintaining honeypots",
            "D": "None of these options are true"
        },
        "correct": "A"
    },
    {
        "question": "Are honeypots likely to produce false positives",
        "options": {
            "A": "No",
            "B": "Yes",
            "C": "",
            "D": ""
        },
        "correct": "A"
    },
    {
        "question": "What is a bastion host",
        "options": {
            "A": "A device that sits on the network perimeter. Has hardened security.",
            "B": "A bastion host is a load balancing server used to distribute traffic",
            "C": "A bastion host is a hardened firewall appliance that automatically blocks suspicious IP addresses before they reach the internal network",
            "D": "A device that acts as an internal monitoring node that inpects all outbound traffic for data exfiltration attempts."
        },
        "correct": "A"
    },
    {
        "question": "On a linux system, where can we view important logs",
        "options": {
            "A": "/var/log/",
            "B": "/shadow/log/syslog/",
            "C": "/shadow/log",
            "D": "/etc/bin/log/"
        },
        "correct": "A"
    },
    {
        "question": "What command can you use to find out what process is using port 80 for example",
        "options": {
            "A": "netstat -an | grep ':80'",
            "B": "netcat -p 80",
            "C": "nmap -v -p 80",
            "D": "tcpdump -in *.*.*.*:80"
        },
        "correct": "A"
    },
    {
        "question": "Is it acceptable to have users be able to log in as root",
        "options": {
            "A": "No, even system admins should not be able to directly log in as root, instead should use su",
            "B": "Yes, only system admins however should be able to log in as root",
            "C": "Yes, however only high level employees at the organisation should be able to",
            "D": "No, because it does not violate prinsiple of least privilege"
        },
        "correct": "A"
    },
    {
        "question": "What is iptables",
        "options": {
            "A": "CLI utility for setting up and maintaining packet filtering rules",
            "B": "It is a tool that makes use of the hardware firewall attatched to your system",
            "C": "It is a table of IP's",
            "D": "Arman, is it really beneficial to learn about a long deprecated and outdated tool? like, what are we doing here? what is the point of any of this? -1k I guess"
        },
        "correct": "A"
    },
    {
        "question": "",
        "options": {
            "A": "",
            "B": "",
            "C": "",
            "D": ""
        },
        "correct": "A"
    },
]


def shuffle(items):
    shuffled = []
    list_copy = list(items)
    while len(list_copy) > 0:
        shuffled.append(list_copy.pop(random.randint(0, len(list_copy) - 1)))
    return shuffled

def clear_screen():
    """Clear the console screen based on operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_question(q_data, q_num, q_count):
    """Display a question and its options"""
    print(f"\nQuestion {q_num} of {q_count}:")
    print(q_data["question"])
    print()
    q_data_shuffled = shuffle(q_data["options"].items())
    i = 0
    for key, value in q_data_shuffled:
        print(f"{['A', 'B', 'C', 'D'][i]}. {value}")
        i += 1
    print()
    return q_data_shuffled

def get_user_answer():
    """Get and validate user input"""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def run_quiz():
    """Main function to run the quiz"""
    score = 0
    total_questions = 0
    incorrect_questions = []
    
    try:
        clear_screen()
        print("======================================")
        print("CYBR371 PRACTICE QUIZ")
        print("======================================")
        print("Test your knowledge with randomly selected questions from past exams and lecture slides")
        print("Answer each question by typing A, B, C, or D.")
        print("Press Ctrl+C at any time to exit the quiz.")
        print("The majority of question answer pairs are generated by AI from resources taken from the course, if you spot any errors please let me know :)")
        print("Do note, I like to take a better safe than sorry aproach when it comes to study, so if there are questions that MIGHT be contained in the test, I will include them despite it being potentially unlikely to be covered in the test")
        print()
        input("Press Enter to begin...")
        
        shuffled_questions = shuffle(questions_db)
        
        for question in shuffled_questions:
            total_questions += 1
            
            clear_screen()
            answer_order = display_question(question, total_questions, len(shuffled_questions))
            user_answer = get_user_answer()
            
            # Check if answer is correct
            i = 0
            for item in answer_order:
                if item[0] == question["correct"]:
                    correct_answer = ['A', 'B', 'C', 'D'][i]
                i += 1
            is_correct = user_answer == correct_answer
            
            if is_correct:
                print("\n✓ Correct! Well done!")
                score += 1
            else:
                print(f"\n✗ Incorrect. The correct answer is {correct_answer}.")
                explanation = question['options'][question["correct"]]
                print(f"Explanation: {explanation}")
                incorrect_questions.append(f"Q: {question['question']}\nYour Answer: {user_answer}\nCorrect: {correct_answer}\nExplanation: {question['options'][correct_answer]}")
                input("Press enter to continue")
            
            print(f"\nCurrent score: {score}/{total_questions} ({score/total_questions*100:.1f}%)")
            
            time.sleep(2)
            
            
    except KeyboardInterrupt:
        clear_screen()
        print("\nQuiz interrupted.")
    
    finally:
        # Display final score
        if total_questions > 0:
            clear_screen()
            print("\n======================================")
            print("QUIZ COMPLETED")
            print("======================================")
            print(f"Final Score: {score}/{total_questions} ({score/total_questions*100:.1f}%)")
            
            if score/total_questions >= 0.9:
                print("Excellent! You're well prepared for the test!")
            elif score/total_questions >= 0.6:
                print("Good job! With a bit more study, you'll be well prepared.")
            elif score/total_questions >= 0.2:
                print("You might need some more study time to prepare for the test.")
            else:
                print("L.")


if __name__ == "__main__":
    run_quiz()

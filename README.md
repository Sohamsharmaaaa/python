# Python Practical Programs

A collection of **35 Python practical programs** organised assignment-wise. The programs move from core
Python fundamentals through data structures, file handling and data analysis, and into practical
networking, web and cryptography tasks — so the set doubles as a gentle **Python-for-cybersecurity**
practical course.

All programs are plain, single-file scripts written for the standard CPython interpreter (3.10+).

---

## Repository structure

```
python/
├── Assignment-1/   Python fundamentals (conditionals, functions, NumPy matrices)
├── Assignment-2/   Data structures & exception handling
├── Assignment-3/   File handling, serialization & data analysis (pandas / matplotlib)
├── Assignment-4/   Networking & web (requests, BeautifulSoup, Scapy, nmap)
├── Assignment-5/   Hashing & cryptography (hashlib, PBKDF2, Fernet)
├── requirements.txt
└── README.md
```

> Programs are grouped by the assignment number in each filename (`AssN_...`). The numbering inside an
> assignment (e.g. `02`, `04`, `05`) follows the original practical list and is kept intact, so some
> numbers are intentionally skipped.

---

## Quick start

```bash
# 1. Clone the repository
git clone https://github.com/Sohamsharmaaaa/python.git
cd python

# 2. (Recommended) create a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
source .venv/bin/activate

# 3. Install the third-party libraries used by some programs
pip install -r requirements.txt

# 4. Run any program
python Assignment-1/Ass1_07_password_strength_score.py
```

Most programs are interactive and read input from the keyboard. A few programs expect a data file or a
running local server — those have per-program notes in the tables below (and inside the scripts).

---

## Assignment 1 — Python fundamentals

| Program | What it does |
|---|---|
| `Ass1_04_public_private_ip_check.py` | Splits an IPv4 string and reports whether it is a **private** or **public** address. |
| `Ass1_05_file_extension_warning.py` | Reads a filename and uses `match`/`case` to print a message for its extension (exe, txt, pdf, …). |
| `Ass1_06_role_based_access_control.py` | Simple **RBAC** check — grants, restricts or denies access based on the user's role and authentication state. |
| `Ass1_07_password_strength_score.py` | Scores a password on length, case, digits and symbols, then classifies it **weak / medium / strong**. |
| `Ass1_09_matrix_operations.py` | Menu-driven NumPy matrix tool — addition, multiplication, upper/lower-triangular and symmetric checks. |
| `Ass1_10_matrix_inverse_check.py` | Accepts two matrices and checks whether the second is the **inverse** of the first (`A·B == I`). |

## Assignment 2 — Data structures & exception handling

| Program | What it does |
|---|---|
| `Ass2_02_constant_time_password_comparison.py` | Constant-time string compare to resist **timing attacks** on passwords / API keys. |
| `Ass2_04_search_number_in_list.py` | Reads `n` values into a list and searches for a user-supplied value. |
| `Ass2_05_unique_even_length_strings.py` | Collects unique strings in a `set` and prints the even-length ones. |
| `Ass2_06_mixed_type_list_operations.py` | Builds a mixed-type list, inserts at a position, slices a subset and prints each value's type. |
| `Ass2_07_tuple_operations.py` | Demonstrates iterating, inserting into and sorting a tuple. |
| `Ass2_08_set_operations.py` | Create / add / discard / pop operations on a `set`. |
| `Ass2_09_compare_server_ports_with_sets.py` | Uses set algebra (union, intersection, difference, symmetric diff) to compare two servers' open ports. |
| `Ass2_10_word_frequency_counter.py` | Counts word frequency in a sentence with a dictionary and reports the most frequent word(s). |
| `Ass2_11_failed_login_ip_frequency.py` | Generates fake failed-login IPs with **Faker** and flags IPs with more than 3 attempts as suspicious. |
| `Ass2_12_list_index_error_handling.py` | Reads 5 integers and handles `IndexError` / `ValueError` when accessing a position. |
| `Ass2_13_network_port_validation.py` | `parse_port()` validates a port (1–65535) using `try/except/finally`. |
| `Ass2_14_authentication_log_analysis.py` | Parses an auth log, validates IPs/timestamps, counts failed logins per IP and logs skipped lines. *(Takes a log file path as an argument; sample log is shown in the file.)* |

## Assignment 3 — File handling & data analysis

| Program | What it does |
|---|---|
| `Ass3_01_malicious_word_search.py` | Scans a file for suspicious keywords and reports the line numbers where each appears. |
| `Ass3_02_dictionary_text_compression.py` | Replaces repeated words with symbols to produce a compressed file plus a dictionary legend. |
| `Ass3_03_student_records_pickle.py` | Stores student records in a binary file with **pickle**, then displays and searches them. |
| `Ass3_06_fake_login_records_csv.py` | Generates 50 fake login records with **Faker** and writes them to `login_records.csv` (shown via pandas). |
| `Ass3_07_top_failed_login_ips_chart.py` | Finds the top-5 IPs by failed logins and saves a **bar chart**. *(Run `Ass3_06` first.)* |
| `Ass3_08_failed_logins_by_hour_chart.py` | Finds the busiest hour for failed logins and saves a **line chart**. *(Run `Ass3_06` first.)* |

## Assignment 4 — Networking & web

| Program | What it does |
|---|---|
| `Ass4_prog01_fetch_web_page_metadata.py` | Fetches a page with **requests** and prints status code, headers and page size. *(See the in-file note to start `python -m http.server`.)* |
| `Ass4_prog02_extract_html_title_and_links.py` | Uses **BeautifulSoup** to extract a page's title and all hyperlinks. |
| `Ass4_prog04_send_icmp_echo_request.py` | Builds and sends an ICMP echo request to `127.0.0.1` with **Scapy** (`.show()` prints the layers). *(Needs admin/root.)* |
| `Ass4_prog06_extract_emails_and_form_fields.py` | Extracts emails (regex) and form input names (BeautifulSoup) from a local HTML page → `output.csv`. |
| `Ass4_prog07_scan_host_port_range_to_report.py` | Validates a host + port range and scans with **python-nmap**, writing a report file. *(Requires the `nmap` binary installed.)* |
| `Ass4_prog08_scan_localhost_tcp_syn_ports.py` | Sends TCP **SYN** packets to ports 20–30 of localhost with Scapy and reports open ports. *(Needs admin/root.)* |

## Assignment 5 — Hashing & cryptography

| Program | What it does |
|---|---|
| `Ass5_prog01_string_hashes_md5_sha1_sha256.py` | Prints the MD5, SHA-1 and SHA-256 hashes of a string with `hashlib`. |
| `Ass5_prog02_fernet_message_encryption_decryption.py` | Encrypts and decrypts a message with **Fernet** (symmetric encryption). |
| `Ass5_prog03_store_salted_password_hash.py` | Generates a random salt and stores a password as a **PBKDF2-HMAC-SHA256** hash. |
| `Ass5_prog04_verify_salted_password_hash.py` | Verifies a password against the stored salt + hash. *(Run `Ass5_prog03` first.)* |
| `Ass5_prog06_fernet_file_encryption_decryption.py` | Encrypts/decrypts a file with Fernet and shows that a wrong key fails to decrypt. |

---

## Requirements

Standard-library modules (`hashlib`, `os`, `pickle`, `re`, `csv`, `string`, `ipaddress`, `datetime`,
`collections`, `socket`, `sys`) need no installation.

The third-party libraries used by some programs are listed in [`requirements.txt`](requirements.txt):

| Library | Used by |
|---|---|
| `numpy` | Assignment 1 (matrices) |
| `faker` | `Ass2_11`, `Ass3_06` |
| `pandas` | `Ass3_06`, `Ass3_07`, `Ass3_08` |
| `matplotlib` | `Ass3_07`, `Ass3_08` |
| `requests` | `Ass4_prog01`, `Ass4_prog02` |
| `beautifulsoup4` | `Ass4_prog02`, `Ass4_prog06` |
| `scapy` | `Ass4_prog04`, `Ass4_prog08` |
| `python-nmap` | `Ass4_prog07` (also needs the `nmap` program installed) |
| `cryptography` | `Ass5_prog02`, `Ass5_prog06` |

Install everything with:

```bash
pip install -r requirements.txt
```

---

## Notes

- The programs that craft or send raw packets (`Ass4_prog04`, `Ass4_prog08`) require **administrator /
  root** privileges and are intended for use against your own machine (`127.0.0.1`) in a lab setting.
- Scripts that read or write data files (CSV, `.dat`, `.key`, `.enc`, charts, etc.) create those files in
  the current working directory; generated artifacts are excluded from version control via `.gitignore`.
- Source files are kept exactly as submitted, including their original comments and sample inputs.

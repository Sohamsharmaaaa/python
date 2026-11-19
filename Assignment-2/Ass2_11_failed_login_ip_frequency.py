# write a python program that generates a list of IP address (with repetitions) of failed login attempts using faker and uses a dictionary to diaplay the number of attempts per IP. display IPs having more than 3 attempts as 'suspicious'.

import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)


def generate_failed_logins(num_ips=6, total_attempts=25):
    # generate a list of IPs with repetitions using faker. create a small pool of unique fake IP then sample from it with repetition so that some IPs appear manytimes.
    ip_pool = [fake.ipv4() for _ in range(num_ips)]
    return random.choices(ip_pool, k=total_attempts)


def count_attempts(ip_list):
    # return a dictionary mapping each IP to its number of failed attempts.
    attempts = {}
    for ip in ip_list:
        attempts[ip] = attempts.get(ip, 0) + 1
    return attempts


failed_logins = generate_failed_logins()
print("Generated failed login attempts: ")
print(failed_logins)

attempts = count_attempts(failed_logins)

print("\nFailed login attempts per  IP: ")
for ip, count in sorted(attempts.items(), key=lambda item: item[1], reverse=True):
    status = "SUSPICIOUS" if count > 3 else ""
    print(f"{ip:<16} : {count:>2} attempt(s) {status}")

print("\nSuspicious IPs (more than 3 attempts) : ")
suspicious = {ip: count for ip, count in attempts.items() if count > 3}
if suspicious:
    for ip, count in suspicious.items():
        print(f" {ip} -> {count} attempts")
else:
    print("None")

# to install faker ---- pip install faker --break-system-packages

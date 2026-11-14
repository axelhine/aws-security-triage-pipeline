
import ipaddress


def validate_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True

    except (ValueError, TypeError):
        return False


# Test cases
print(validate_ip("192.0.2.10"))
print(validate_ip("999.999.999.999"))
print(validate_ip("198.51.100.25"))
print(validate_ip("hello.world"))
print(validate_ip(""))

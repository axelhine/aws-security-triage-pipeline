
import ipaddress


def validate_ip(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True

    except (ValueError, TypeError):
        return False

def classify_ip(ip):
    # First, check whether the IPv4 address is valid
    if not validate_ip(ip):
        return "INVALID"

    # Convert the string into an IPv4Address object
    address = ipaddress.IPv4Address(ip)

    # Check whether the address is loopback
    if address.is_loopback:
        return "LOOPBACK"

    # Check whether the address is private
    elif address in ipaddress.IPv4Network("10.0.0.0/8"):
        return "PRIVATE"

    elif address in ipaddress.IPv4Network("172.16.0.0/12"):
        return "PRIVATE"

    elif address in ipaddress.IPv4Network("192.168.0.0/16"):
        return "PRIVATE"

    # Check the documentation ranges
    elif any(address in network for network in [
        ipaddress.IPv4Network("192.0.2.0/24"),
        ipaddress.IPv4Network("198.51.100.0/24"),
        ipaddress.IPv4Network("203.0.113.0/24")
    ]):
        return "DOCUMENTATION"

    # Check whether the address is globally reachable
    elif address.is_global:
        return "GLOBAL"

    # Other special-use addresses
    else:
        return "SPECIAL_USE"


# Test cases

if __name__ == "__main__":
    print(validate_ip("192.0.2.10"))
    print(validate_ip("999.999.999.999"))
    print(validate_ip("198.51.100.25"))
    print(validate_ip("hello.world"))
    print(validate_ip(""))

    print("\n=== IP CLASSIFICATION TESTS ===")
    print(classify_ip("192.168.1.10"))
    print(classify_ip("8.8.8.8"))
    print(classify_ip("127.0.0.1"))
    print(classify_ip("192.0.2.10"))
    print(classify_ip("999.999.999.999"))



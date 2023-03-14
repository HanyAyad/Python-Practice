def remove_whitespace(ip):
    return ip.replace(" ", "").replace("\n", "")
def main():
    ip1= "192.20.246.138:\n 6666"
    ip2="206.130.99.82:\n8080"
    print(remove_whitespace(ip1))
    print(remove_whitespace(ip2))


if __name__ == "__main__":
    main() 
from pathlib import Path


def encrypt_file(input_file, output_file, key):
    data = Path(input_file).read_bytes()
    encrypted = bytes(byte ^ key for byte in data)
    Path(output_file).write_bytes(encrypted)


def decrypt_file(input_file, output_file, key):
    data = Path(input_file).read_bytes()
    decrypted = bytes(byte ^ key for byte in data)
    Path(output_file).write_bytes(decrypted)


def main():
    print("Secure File Encryption Tool")
    print("---------------------------")

    filename = input("Enter a file path: ").strip()

    if not Path(filename).is_file():
        print("File not found.")
        return

    key = 23

    encrypted_file = filename + ".enc"
    decrypted_file = filename + ".dec"

    encrypt_file(filename, encrypted_file, key)
    print(f"\nEncrypted file created: {encrypted_file}")

    decrypt_file(encrypted_file, decrypted_file, key)
    print(f"Decrypted file created: {decrypted_file}")


if __name__ == "__main__":
    main()

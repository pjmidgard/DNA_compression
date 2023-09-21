import struct
#@Author Jurijus Pacalovas

# Function to compress binary data with a 2^24-byte buffer
def compress_data(data):
    chunk_size = 2**24  # 16 MB buffer size
    compressed_chunks = []
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        compressed_chunk = struct.pack('I', len(chunk)) + chunk  # Prefix with chunk size
        compressed_chunks.append(compressed_chunk)
    return b''.join(compressed_chunks)

# Function to extract compressed binary data
def extract_data(compressed_data):
    extracted_chunks = []
    offset = 0
    while offset < len(compressed_data):
        chunk_size = struct.unpack('I', compressed_data[offset:offset + 4])[0]
        offset += 4
        chunk = compressed_data[offset:offset + chunk_size]
        extracted_chunks.append(chunk)
        offset += chunk_size
    return b''.join(extracted_chunks)

# Ask the user whether to compress or extract
operation = input("Enter 'C' for compression or 'E' for extraction: ").strip().lower()

if operation == 'c':
    # Get the name of the file to compress and output file from the user
    input_filename = input("Enter the name of the input file to compress: ")
    output_filename = input("Enter the name of the output compressed file: ")

    # Read the binary data from the input file
    try:
        with open(input_filename, 'rb') as file:
            data_to_compress = file.read()
    except FileNotFoundError:
        print(f"File '{input_filename}' not found. Exiting.")
        exit(1)

    # Compress the data
    compressed_data = compress_data(data_to_compress)

    # Save the compressed data to the output file
    with open(output_filename, 'wb') as file:
        file.write(compressed_data)

    print(f"Compression completed. Compressed data saved to '{output_filename}'.")

elif operation == 'e':
    # Get the name of the compressed file and output file from the user
    input_filename = input("Enter the name of the compressed file: ")
    output_filename = input("Enter the name of the output extracted file: ")

    # Read the compressed data from the input file
    try:
        with open(input_filename, 'rb') as file:
            compressed_data = file.read()
    except FileNotFoundError:
        print(f"File '{input_filename}' not found. Exiting.")
        exit(1)

    # Extract the compressed data
    extracted_data = extract_data(compressed_data)

    # Save the extracted data to the output file
    with open(output_filename, 'wb') as file:
        file.write(extracted_data)

    print(f"Extraction completed. Extracted data saved to '{output_filename}'.")
else:
    print("Invalid choice. Please enter 'C' for compression or 'E' for extraction.")

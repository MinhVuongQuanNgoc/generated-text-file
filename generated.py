import os

# Target size(MB)
TARGET_MB = 5.5

TARGET_BYTES = int(TARGET_MB * 1024 * 1024)

# Define content.
CHARACTER = 'A'
CHUNK_SIZE = 1024 * 1024 

file_name = "oversized.txt"

print(f"Generating file: {file_name}")
print(f"Target size: {TARGET_MB}({TARGET_BYTES})")

try:
    with open(file_name, 'w') as f:
        bytes_written = 0
        
        # Write chunks until the target is reached
        while bytes_written < TARGET_BYTES:
            
            # How much to write in this chunk
            remaining_bytes = TARGET_BYTES - bytes_written
            bytes_to_write = min(CHUNK_SIZE, remaining_bytes)
            
            # Create the string to write
            content = CHARACTER * bytes_to_write
            
            # Write the conten
            f.write(content)
            
            # Update the count
            bytes_written += len(content.encode('utf-8'))
            
            # Print progress
            print(f"  Written: {bytes_written / (1024*1024):.2f} MB", end='\r')

    print(f"\nSuccessfully created {file_name} with size {os.path.getsize(file_name) / (1024*1024):.2f} MB.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
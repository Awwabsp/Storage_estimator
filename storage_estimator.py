# Storage Estimator
# Converts storage values to bytes and gigabytes

mb = float(input("Enter storage in Megabytes (MB): "))
bytes_val = mb * 1024 * 1024
gb_val = mb / 1024

print(f"Storage in Bytes: {bytes_val:,.0f} Bytes")
print(f"Storage in Gigabytes: {gb_val:.2f} GB")
import shutil

def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if there's enough free space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return False
    return True

if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space.")
else:
    print("Everything is OK.")

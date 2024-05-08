import uuid

def generate_unique_vendor_number():
    prefix = "VE"
    unique_id = uuid.uuid4().hex[:8].upper() 
    po_number = f"{prefix}-{unique_id}"

    return po_number


# Note: It can be adjusted as per the business need
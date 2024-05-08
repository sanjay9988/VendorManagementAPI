import uuid
from datetime import datetime

def generate_unique_po_number():
    prefix = "PO"
    # timestamp = datetime.now().strftime("%Y%m%d%H%M%S") 
    unique_id = uuid.uuid4().hex[:8].upper() 
    po_number = f"{prefix}-{unique_id}"

    return po_number


# Note: It can be adjusted as per the business need
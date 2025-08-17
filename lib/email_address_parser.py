# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        addresses = re.split(r'[,\s]+', self.email_addresses)
        email_pattern = re.compile(r'^[\w\.-]+@[\w-]+\.[\w\.-]+$')
        valid_emails = []
        
        for addr in addresses:
            addr = addr.strip()
            if addr and email_pattern.fullmatch(addr):
                valid_emails.append(addr)
        
        # Get unique addresses and sort alphabetically
        unique_sorted = sorted(list(set(valid_emails)))
        
        return unique_sorted   
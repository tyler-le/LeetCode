class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        hmap = set()
        
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            hmap.add(local+ "@" + domain)

        return len(hmap)
    
    
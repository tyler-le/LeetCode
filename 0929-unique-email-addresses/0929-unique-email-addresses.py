class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            ret.add(local+"@"+domain)
            
        return len(ret)
        
            
# https://leetcode.com/problems/unique-email-addresses/
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            femail = self.formatEmail(email)
            unique.add(femail)
        return len(unique)

    def formatEmail(self, email):
        local, domain = email.split('@')
        local = local.replace('.', '', -1)
        plus = local.find('+')
        if plus != -1:
            local = local[:plus]
        return local + '@' + domain
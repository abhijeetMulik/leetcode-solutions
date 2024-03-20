class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mySet = set()
        for email in emails:
            a = email.split('@')
            b = a[0].split('+')
            c = b[0].replace('.','')
            d = c + '@'+ a[1]
            mySet.add(d)
        return len(mySet)
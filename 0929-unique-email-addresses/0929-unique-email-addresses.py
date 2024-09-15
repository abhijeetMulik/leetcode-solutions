class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for e in emails:
            email = e.split('@')
            em = email[0].replace('.', '')
            if '+' in em:
                em = em[:em.index('+')]
            print(em)
            ans.add(em + '@' +email[1])
            print(ans)

        return len(ans)
        
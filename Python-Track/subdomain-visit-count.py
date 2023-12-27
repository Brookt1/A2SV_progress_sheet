class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic,res={},[]
        for domains in cpdomains:
            domains=domains.split()
            all_domains=list(reversed(domains[1].split('.')))
            sub_domain=''
            for domain in all_domains:
                sub_domain=domain+'.'+sub_domain if sub_domain else domain
                if sub_domain in dic:
                    dic[sub_domain]+=int(domains[0])
                else:
                    dic[sub_domain]=int(domains[0])

        for key,val in dic.items():
            res.append(str(val)+' '+key)
        return res
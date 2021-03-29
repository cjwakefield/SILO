from pyhunter import PyHunter
hunter = PyHunter('a769e22412908c05f8f686cd090b3a1c283afb80')
out = hunter.domain_search(company='ntst.com', limit=5, offset=2, emails_type='personal')
print(out)
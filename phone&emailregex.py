import re, pyperclip

# Regex for phone number
phoneRegex = re.compile(r'''
 #445-232-0010, 232-0010, (415) 555-0000, 555-0000 ext 1234, ext.1234, x1234
(
((\d\d\d)|(\(\d\d\d\)))?  # area code (optional=>?) first grp or second grp
(\s|-)                    # first seperator
\d\d\d                    # first 3 digits
 -                        # seperator
\d\d\d\d                  # last 4 digits
(((ext(\.)?\s)|x)         # entension-word part
 (\d{2,5}))?              # extn 2-5 digits long
 )                        # All in 1 grp so printing is easy
''', re.VERBOSE)
# Regex for email id
emailRegex = re.compile(r'''
#some.+_thing@(\d{})).com  # .or+or_ in email
[a-zA-Z0-9+._]+            # name part, +=> 1or more
@                          # @ symbol
[a-zA-Z0-9+._]+            # domain name

''', re.VERBOSE)
#Get the text off of Clipboard
text = pyperclip.paste()

#Extract phone number or email from text
extractedPhone= phoneRegex.findall(text)
extractedEmail= emailRegex.findall(text)

allPhonenum=[]
for phone in extractedPhone:
    allPhonenum.append(phone[0])

result= '\n'.join(allPhonenum)+'\n'+'\n'.join(extractedEmail)
# print(result)
# Write the result to text file
with open('writefile.txt', 'w') as resultfile:
    resultfile.write(result)

# wfile= open('writefile.txt','w')
# wfile.write(result)
# wfile.close()
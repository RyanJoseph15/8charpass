import subprocess, sys, optparse, os, signal

parser = optparse.OptionParser()
parser.add_option("-a", "--address", dest="address", default=None, help="the address that you're trying to get into")
parser.add_option("-c", "--charset", dest="charset", default="ab12", help="the string of characters you're sampling from. example: 'abc123'")
parser.add_option("-r", "--repeats", dest="repeats", default=0, help="if your charset is 'abc', -r 1 will allow a to be repeated once")
parser.add_option("-g", "--gethpth", dest="gethpth", default=None, help="the absolute path to your geth program")
parser.add_option("-l", "--pwlngth", dest="pwlngth", default=0, help="exact number of characters your password holds")
parser.add_option("-f", "--paramfl", dest="paramfl", default=None, help="file containing all the params in param=value format")
(options, args) = parser.parse_args()
params = {
    "address": options.address,
    "charset": options.charset,
    "repeats": options.repeats,
    "gethpth": options.gethpth,
    "pwlngth": options.pwlngth
}
paramfl = options.paramfl.strip()

paramFile = open(paramfl, 'rU')
if paramFile != None:
    for line in paramFile:
        varValArray = line.split("=")
        attrName = varValArray[0]
        attrVal = varValArray[1].rstrip()
        params[attrName] = int(attrVal) if (attrName == "repeats") | (attrName == "pwlngth") else attrVal

charsetsLength = len(params["charset"])

def append(string, times):
    for char in params["charset"]:
        charCount = string.count(char)
        if (charCount <= params["repeats"]):
            newString = string + char
            if (times == params["pwlngth"]):
                args = [params["gethpth"], "account", "update", params["address"]]
                proc = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
                child_pid = proc.pid
                myStdout = proc.communicate(input=str.encode(newString + '\n'))[0]
                output = myStdout.decode()
                if (("Attempt 2/3" in str(output)) | ("MAC mismatch" in str(output)) | ("Fatal: EOF" in str(output))):
                    proc.kill()
                print(newString)
                if "unlocked" in str(output):
                    sys.exit()
            if (times < params["pwlngth"]):
                append(newString, times + 1)

append('', 1)
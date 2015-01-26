import robotparser
def listRestricted():
    """ Return the restricted folders from a webpage based on the robots.txt file. """
    sites = ['www.google.com','www.coventry.ac.uk', 'www.yahoo.com']
    
    def getDenies(site):
        """ Create a new robotparser instance and read the site's robots file"""
        paths =[]
        robot = robotparser.RobotFileParser()
        robot.set_url("http://"+site+"/robots.txt")
        robot.read()

        #print robot.default_entry
        
        # For each entry, look at the rule lines and add the path to paths if disallowed.
        for line in robot.default_entry.rulelines:
            #for line in entry.rulelines:
                not line.allowance and paths.append(line.path)
        return set(paths)

    for site in sites:
        print "Denies for"+site
        print "\t" + "\n\t".join(getDenies(site))
        

listRestricted()

# -*- coding: utf-8 -*-

from module.plugins.Hook import Hook
import re

class XFileSharingPro(Hook):
    __name__ = "XFileSharingPro"
    __version__ = "0.01"
    __type__ = "hook"
    __config__ = [ ("activated", "bool", "Activated" , "True"),
                   ("loadDefault", "bool", "Load default hoster list" , "True"),
                   ("includeList", "str", "Include hosters (comma separated)", ""),
                   ("excludeList", "str", "Exclude hosters (comma separated)", "")]
    __description__ = """MultiShare.cz hook plugin"""
    __author_name__ = ("zoidberg")
    __author_mail__ = ("zoidberg@mujmail.cz")    
    
    def coreReady(self):
        hosterList = self.getConfigSet('includeList')
        excludeList = self.getConfigSet('excludeList')         
        
        if self.getConfig('loadDefault'):        
            hosterList |= set((
            #WORKING HOSTERS:
            #NOT TESTED:
            "aieshare\.com", "amonshare\.com", "asixfiles\.com", "azsharing\.com", "banashare\.com", "batubia\.com", 
            "bebasupload\.com", "boosterking\.com", "buckshare\.com", "bulletupload\.com", "crocshare\.com", "ddlanime\.com", "divxme\.com", 
            "dopeshare\.com", "downupload\.com", "eyesfile\.com", "eyvx\.com", "fik1\.com", "file4safe\.com", "file4sharing\.com", 
            "fileband\.com", "filebeep\.com", "filebit\.com", "filebox\.com", "filedove\.com", "fileforth\.com", 
            "filemade\.com", "filemak\.com", "fileplanet\.com", "fileplaygroud\.com", "filerace\.com", "filerio\.com", "filestrack\.com", 
            "fileupper\.com", "filevelocity\.com", "fooget\.com", "4bytez\.com", "freefilessharing\.com", "glumbouploads\.com", "grupload\.com", 
            "heftyfile\.com", "hipfile\.com", "host4desi\.com", "hulkshare\.com", "idupin\.com", "imageporter\.com", "isharefast\.com", 
            "jalurcepat\.com", "kingsupload\.com", "laoupload\.com", "linkzhost\.com", "loombo\.com", "maknyos\.com", "migahost\.com", 
            "mlfat4arab\.com", "movreel\.com", "netuploaded\.com", "ok2upload\.com", "180upload\.com", "1hostclick\.com", "ovfile\.com", 
            "putshare\.com", "pyramidfiles\.com", "q4share\.com", "queenshare\.com", "ravishare\.com", "rockdizfile\.com", "sendmyway\.com", 
            "share76\.com", "sharebeast\.com", "sharehut\.com", "sharerun\.com", "shareswift\.com", "sharingonline\.com", "6ybh-upload\.com", 
            "skipfile\.com", "spaadyshare\.com", "space4file\.com", "speedoshare\.com", "uploadbaz\.com", "uploadboost\.com", "uploadc\.com", 
            "uploaddot\.com", "uploadfloor\.com", "uploadic\.com", "uploadville\.com", "uptobox\.com", "vidbull\.com", "zalaa\.com", 
            "zomgupload\\.com\.com", "kupload\.org", "movbay\.org", "multishare\.org", "omegave\.org", "toucansharing\.org", "uflinq\.org",
            "banicrazy\.info", "flowhot\.info", "upbrasil\.info", "shareyourfilez\.biz", "bzlink\.us", "cloudcache\.cc", "fileserver\.cc"
            "farshare\.to", "kingshare\.to", "filemaze\.ws", "filehost\.ws", "goldfile\.eu", "xfileshare\.eu", "filestock\.ru", "moidisk\.ru"
            "4up\.me", "kfiles\.kz", "odsiebie\.pl", "upchi\.co\.il", "upit\.in", "verzend\.be"
            ))
            
            #NOT WORKING:
            """
            """                
              
        hosterList -= (excludeList)
        hosterList -= set(('', u''))
        
        if not hosterList:
            self.logError("Hoster list is empty" % len(hosterList))
            return
                                            
        regexp = r"http://(?:[^./]/.)*?(%s)/\w{12}" % "|".join(hosterList)
        self.logDebug("Added %d hosters" % len(hosterList))
        self.logDebug(regexp)
        
        dict = self.core.pluginManager.hosterPlugins['XFileSharingPro']
        dict["pattern"] = regexp
        dict["re"] = re.compile(regexp)
        
    def getConfigSet(self, option):
        s = self.getConfig(option).lower().replace('|',',').replace(';',',').replace('.','\.')
        return set([x.strip() for x in s.split('|')])
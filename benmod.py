# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup

boss = LineClient('seksolo919@gmail.com','Aa1234')
ki = LineClient('itwatchala@gmail.com','Aa1234')
kk = LineClient('')
kc = LineClient('')



poll = LinePoll(boss)
call = boss
creator = ["u874a7502c02896b2edbb3445c2615d35"]
owner = ["u874a7502c02896b2edbb3445c2615d35"]
admin = ["u874a7502c02896b2edbb3445c2615d35"]
staff = ["u874a7502c02896b2edbb3445c2615d35"]
mid = boss.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
KAC = [boss,ki,kk,kc]
ABC = [ki,kk,kc]
Bots = [mid,Amid,Bmid,Cmid]
Madzs = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []

welcome = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

MadzsProfile = boss.getProfile()
myProfile["displayName"] = MadzsProfile.displayName
myProfile["statusMessage"] = MadzsProfile.statusMessage
myProfile["pictureStatus"] = MadzsProfile.pictureStatus

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items            

def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@boss "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    boss.sendMessage(to, textx, {'AGENT_NAME':'@boss1 on Instagram', 'AGENT_LINK': 'https://www.instagram.com/boss1', 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + boss.getProfile().picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMessageFooter(to, text, name, url, iconlink):
        contentMetadata = {
            'AGENT_NAME': name,
            'AGENT_LINK': url,
            'AGENT_ICON': iconlink
        }
        return boss.sendMessage(to, text, contentMetadata, 0)
    

def sendMessageWithFooter(to, text):
 boss.reissueUserTicket()
 madzs = boss.getProfile()
 ticket = "http://line.me/ti/p/"+boss.getUserTicket().id
 pict = "http://dl.profile.line-cdn.net/"+boss.pictureStatus
 name = "??? boss ???"
 boss = {"AGENT_ICON": pict,
     "AGENT_NAME": name,
     "AGENT_LINK": ticket
 }
 boss.sendMessage(to, text, contentMetadata=boss)

def sendMentionV10(to, text,name, url, iconlink):
    boss.sendMessage(to, text, {'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink })

def mentionMembers(to, mid,name,url,iconlink):
    try:
        arrData = ""
        ginfo = boss.getGroup(to)
        textx = "    ?????????Mention Members?????????\n\n???1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "???{}. ".format(str(no))
            else:
                textx += "\nTotal: {} members".format(str(len(mid)))
        boss.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),'AGENT_NAME': name,'AGENT_LINK': url,'AGENT_ICON': iconlink },0)
    except Exception as error:
        boss.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ??????????????????????????????????????????????????????????????????????????? \n????????????????????????  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boss.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\ : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n  ?????????[ {} ]".format(str(boss.getGroup(to).name))
                except:
                    no = "\n  ?????????[ Success ]"
        boss.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boss.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Keluar???{}???\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = boss.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n  ?????????[ {} ]".format(str(boss.getGroup(to).name))
                except:
                    no = "\n  ?????????[ Success ]"
        boss.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boss.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = boss.getAllContactIds()
        gid = boss.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"???? Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n???? Group : "+str(len(gid))+"\n???? Teman : "+str(len(teman))+"\n???? Version : http://github.com/boss/Protect4\n???? Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n???? Runtime : \n???? ??? "+bot
        boss.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        boss.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "????????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? boss ????????????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "?????????????????????? Help Message ??????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????????????????????????? List Menu ????????????????????????" + "\n" + \
                  "??????? " + key + "Cctv???on/off???\n" + \
				  "??????? " + key + "Creator\n" + \
				  "??????? " + key + "Cyduk\n" + \
				  "??????? " + key + "Help admin\n" + \
				  "??????? " + key + "Help blacklist\n" + \
				  "??????? " + key + "Help bot\n" + \
                  "??????? " + key + "Help creator\n" + \
				  "??????? " + key + "Help setting\n" + \
                  "??????? " + key + "Listbot\n" + \
                  "??????? " + key + "Listadmin\n" + \
				  "??????? " + key + "Status\n" + \
				  "?????????????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage
    
    

def helpcreator():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "??????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "????????????????????????? boss ????????????????????????" + "\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "????????????????????????? Help BOT ?????????????????????" + "\n" + \
                  "?????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "????????????????????????? List Menu ??????????????????" + "\n" + \
                  "??????? " + key + "Cek spam\n" + \
                  "??????? " + key + "Cek pesan\n" + \
                  "??????? " + key + "Cek respon\n" + \
                  "??????? " + key + "Cek welcome\n" + \
                  "??????? " + key + "Cek leave\n" + \
                  "??????? " + key + "Set spam:???Text???\n" + \
                  "??????? " + key + "Set pesan:???Text???\n" + \
                  "??????? " + key + "Set respon:???Text???\n" + \
                  "??????? " + key + "Set welcome:???Text???\n" + \
                  "??????? " + key + "Set leave:???Text???\n" + \
                  "??????? " + key + "Ditname:???Name???\n" + \
                  "??????? " + key + "Dit1name:???Name???\n" + \
                  "??????? " + key + "Dit2name:???Name???\n" + \
                  "??????? " + key + "Ditname:???Name???\n" + \
				  "??????? " + key + "Dit3name:???Name???\n" + \
                  "??????? " + key + "Dit1up???Foto???\n" + \
                  "??????? " + key + "Dit2up???Foto???\n" + \
                  "??????? " + key + "Dit3up???Foto???\n" + \
				  "??????? " + key + "Dit4up???Foto???\n" + \
                  "??????? " + key + "Gift:???Mid??????Jumlah???\n" + \
                  "??????? " + key + "Spam:???Mid??????Jumlah???\n" + \
				  "??????? " + key + "Spamtag:???jumlahnya???\n" + \
                  "??????? " + key + "Spamtag???@???\n" + \
                  "??????? " + key + "Spamcall:???jumlahnya???\n" + \
                  "??????? " + key + "Spamcall\n" + \
                  "??????? " + key + "Broadcast:???Text???\n" + \
                  "??????? " + key + "Setkey???New Key???\n" + \
                  "??????? " + key + "Mykey\n" + \
                  "??????? " + key + "Resetkey\n" + \
				  "??????? " + key + "Self???on/off???\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage1

def helpblacklist():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage3 = "?????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? boss ????????????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "?????????????????????? Help Blacklist ??????????????????" + "\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? List Menu ?????????????????????" + "\n" + \
                  "??????? " + key + "Banlist\n" + \
				  "??????? " + key + "Ban:on\n" + \
                  "??????? " + key + "Blc\n" + \
				  "??????? " + key + "Clearban\n" + \
				  "??????? " + key + "Refresh\n" + \
				  "??????? " + key + "Unban???@???\n" + \
				  "??????? " + key + "Unban:on\n" + \
				  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage3

def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage4 = "?????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? boss ????????????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "?????????????????????? Help Admin ??????????????????" + "\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? List Menu ?????????????????????" + "\n" + \
                  "??????? " + key + "Admin:on\n" + \
                  "??????? " + key + "Admin:repeat\n" + \
                  "??????? " + key + "Adminadd???@???\n" + \
                  "??????? " + key + "Admindell???@???\n" + \
				  "??????? " + key + "Bot:on\n" + \
                  "??????? " + key + "Bot:repeat\n" + \
				  "??????? " + key + "Botadd???@???\n" + \
                  "??????? " + key + "Botdell???@???\n" + \
				  "??????? " + key + "Refresh\n" + \
				  "??????? " + key + "Staff:on\n" + \
                  "??????? " + key + "Staff:repeat\n" + \
                  "??????? " + key + "Staffadd???@???\n" + \
                  "??????? " + key + "Staffdell???@???\n" + \
                  "??????????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage4
    	
def helpsetting():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage5 = "?????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? boss ????????????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "?????????????????????? Help Setting ??????????????????" + "\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? List Menu ?????????????????????" + "\n" + \
                  "??????? " + key + "Autoadd???on/off???\n" + \
				  "??????? " + key + "Autojoin???on/off???\n" + \
				  "??????? " + key + "Autoleave???on/off???\n" + \
				  "??????? " + key + "Contact???on/off???\n" + \
				  "??????? " + key + "Jointicket???on/off???\n" + \
				  "??????? " + key + "Respon???on/off???\n" + \
				  "??????? " + key + "Unsend???on/off???\n" + \
                  "??????? " + key + "Welcome???on/off???\n" + \
                  "??????????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage5
    
def helpprotect():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage6 = "?????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? boss ????????????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "?????????????????????? Help Protect ??????????????????" + "\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? List Menu ?????????????????????" + "\n" + \
				  "??????? " + key + "Join dit\n" + \
				  "??????? " + key + "Ditpro ???on/off???\n" + \
                  "??????? " + key + "Notag???on/off???\n" + \
                  "??????? " + key + "Protecturl???on/off???\n" + \
                  "??????? " + key + "Protectjoin???on/off???\n" + \
                  "??????? " + key + "Protectkick???on/off???\n" + \
                  "??????? " + key + "Protectcancel???on/off???\n" + \
                  "??????? " + key + "Protectinvite???on/off???\n" + \
				  "??????????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage6
	
def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage8 = "?????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? boss ????????????????????????" + "\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "?????????????????????? Help BOT ??????????????????" + "\n" + \
                  "????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "???????????????????????????? List Menu ?????????????????????" + "\n" + \
                  "??????? " + key + "About\n" + \
				  "??????? " + key + "Close\n" + \
				  "??????? " + key + "Ginfo\n" + \
				  "??????? " + key + "Gruplist\n" + \
				  "??????? " + key + "Info ???@???\n" + \
				  "??????? " + key + "???@???Kick\n" + \
				  "??????? " + key + "Me\n" + \
                  "??????? " + key + "Mid???@???\n" + \
				  "??????? " + key + "Mybot\n" + \
                  "??????? " + key + "Mymid\n" + \
				  "??????? " + key + "Open\n" + \
				  "??????? " + key + "Respon\n" + \
				  "??????? " + key + "Restart\n" + \
				  "??????? " + key + "Runtime\n" + \
				  "??????? " + key + "Speed/Sp\n" + \
                  "??????? " + key + "Sprespon\n" + \
				  "??????? " + key + "Stealname???@???\n" + \
                  "??????? " + key + "Stealbio???@???\n" + \
                  "??????? " + key + "Stealcover???@???\n" + \
				  "??????? " + key + "Stealpicture???@???\n" + \
                  "??????? " + key + "Stealvideoprofile???@???\n" + \
                  "??????? " + key + "Tagall\n" + \
                  "???????????????????????????????????????????????????????????????????????????????????" + "\n" + \
                  "??????????? http://line.me/ti/p/~adit_cmct" + "\n" + \
                  "?????????????????? CREATOR: ??boss???"
    return helpMessage8

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if boss.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            boss.reissueGroupTicket(op.param1)
                            X = boss.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            boss.updateGroup(X)
                            boss.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                boss.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    boss.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        boss.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if boss.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            boss.reissueGroupTicket(op.param1)
                                            X = boss.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            boss.updateGroup(X)
                                            boss.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.updateGroup(X)
                                                boss.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boss.acceptGroupInvitation(op.param1)
                        ginfo = boss.getGroup(op.param1)
                        boss.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        boss.leaveGroup(op.param1)
                    else:
                        boss.acceptGroupInvitation(op.param1)
                        ginfo = boss.getGroup(op.param1)
                        boss.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        boss.acceptGroupInvitation(op.param1)
                        ginfo = boss.getGroup(op.param1)
                        boss.sendMessage(op.param1,"Haii, salken yaa ^^")
                    else:
                        boss.acceptGroupInvitation(op.param1)
                        ginfo = boss.getGroup(op.param1)
                        boss.sendMessage(op.param1,"Haii, salken yaa ^^")
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = boss.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = boss.getGroup(op.param1)
                contact = boss.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                boss.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = boss.getGroup(op.param1)
                contact = boss.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                boss.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        boss.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        boss.sendMessage(op.param1, wait["message"])

#================================================================================
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass             

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[Zmid])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[Zmid])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[Zmid])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                boss.kickoutFromGroup(op.param1,[op.param2])
                                                boss.inviteIntoGroup(op.param1,[Zmid])
                                        except:
                                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        boss.acceptGroupInvitation(op.param1)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            boss.acceptGroupInvitation(op.param1)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                boss.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    boss.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.kickoutFromGroup(op.param1,[op.param2])                                    
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        boss.acceptGroupInvitation(op.param1)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            boss.acceptGroupInvitation(op.param1)
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                boss.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                boss.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    boss.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            boss.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            boss.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    boss.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        boss.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        boss.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    G = boss.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    boss.updateGroup(G)
                                    Ticket = boss.reissueGroupTicket(op.param1)
                                    boss.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    boss.kickoutFromGroup(op.param1,[op.param2])
                                    G = boss.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    boss.updateGroup(G)
                                    Ticket = boss.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        boss.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        boss.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        boss.findAndAddContactsByMid(op.param1,admin)
                        boss.inviteIntoGroup(op.param1,admin)
                        boss.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["bossreadPoint"]:
                   if op.param2 in Setmain["bossreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["bossreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = boss.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = boss.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        boss.sendImageWithURL(op.param1, image)                        
                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = boss.getGroup(at)
                                boss = boss.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "??? Gambar Dihapus ???\n??? Pengirim : "
                                ret_ = "??? Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n??? Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(boss.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':boss.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                boss.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                boss.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = boss.getGroup(at)
                                boss = boss.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "??? Pesan Dihapus ???\n"
                                ret_ += "??? Pengirim : {}".format(str(boss.displayName))
                                ret_ += "\n??? Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n??? Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n??? Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                boss.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = boss.getGroup(at)
                                boss = boss.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "??? Sticker Dihapus ???\n"
                                ret_ += "??? Pengirim : {}".format(str(boss.displayName))
                                ret_ += "\n??? Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n??? Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                boss.sendMessage(at, str(ret_))
                                boss.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26 or op.type == 25:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"21715710","STKPKGID":"9662","STKVER":"2"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           cl.sendMessage(msg.to, "Ye ngetag ngetag, lu minta digift ya? cek PersonalChat bos, udah gue gift tuh. Jangan lupa bilang makasih yak!")
                           cl.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"???Cek ID Sticker???\n???? STKID : " + msg.contentMetadata["STKID"] + "\n???? STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n???? STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n???Link Sticker???" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"??? Nama: " + msg.contentMetadata["displayName"] + "\n??? MID: " + msg.contentMetadata["mid"] + "\n??? Status: " + contact.statusMessage + "\n??? Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = boss.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n??? Sticker Info ???"
                   ret_ += "\n??? Sticker ID : {}".format(stk_id)
                   ret_ += "\n??? Sticker Version : {}".format(stk_ver)
                   ret_ += "\n??? Sticker Package : {}".format(pkg_id)
                   ret_ += "\n??? Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = boss.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    boss.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n???Link Sticker???" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    boss.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = boss.getContact(msg.contentMetadata["mid"])
                        path = boss.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        boss.sendMessage(msg.to,"???? Nama : " + msg.contentMetadata["displayName"] + "\n???? MID : " + msg.contentMetadata["mid"] + "\n???? Status Msg : " + contact.statusMessage + "\n???? Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        boss.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        boss.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        boss.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        boss.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        boss.sendMessage(msg.to,"Contact itu bukan anggota bot boss")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        boss.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        boss.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        boss.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        boss.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        boss.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        boss.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        boss.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        boss.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        boss.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        boss.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        boss.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        boss.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = boss.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            boss.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = boss.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     boss.updateGroupPicture(msg.to, path)
                     boss.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["bossfoto"]:
                            path = boss.downloadObjectMsg(msg_id)
                            del Setmain["bossfoto"][mid]
                            boss.updateProfilePicture(path)
                            boss.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["bossfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["bossfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["bossfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["bossfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["bossfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["bossfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        boss.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               boss.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                boss.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                boss.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help creator":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpcreator()
                               ma = boss.getProfile()
                               name = "Help Creator Message"
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(ma.pictureStatus))
                               sendMentionV10(msg.to, str(helpMessage1), str(name), str(url), str(iconlink))

                        elif cmd == "help admin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage4 = helpadmin()
                               ma = boss.getProfile()
                               name = "Help Admin Message"
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(ma.pictureStatus))
                               sendMentionV10(msg.to, str(helpMessage4), str(name), str(url), str(iconlink))
                               
                        elif cmd == "help setting":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage5 = helpsetting()
                               ma = boss.getProfile()
                               name = "Help Settings Message"
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(ma.pictureStatus))
                               sendMentionV10(msg.to, str(helpMessage5), str(name), str(url), str(iconlink))                      

                        elif cmd == "help protect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage6 = helpprotect()
                               ma = boss.getProfile()
                               name = "Help Protect Message"
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(ma.pictureStatus))
                               sendMentionV10(msg.to, str(helpMessage6), str(name), str(url), str(iconlink))

                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage8 = helpbot()
                               ma = boss.getProfile()
                               name = "Help Bot Message"
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(ma.pictureStatus))
                               sendMentionV10(msg.to, str(helpMessage8), str(name), str(url), str(iconlink))

                        elif cmd == "help blacklist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage3 = helpblacklist()
                               ma = boss.getProfile()
                               name = "Help Bot Message"
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(ma.pictureStatus))
                               sendMentionV10(msg.to, str(helpMessage3), str(name), str(url), str(iconlink))

                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                boss.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                boss.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "???????????????????????????????????? STATUS ??????????????????????????????????????????\n"
                                if wait["unsend"] == True: md+="??????? ?????? Unsend???ON???\n"
                                else: md+="??????? ??? Unsend???OFF???\n"                                
                                if wait["Mentionkick"] == True: md+="??????? ?????? Notag???ON???\n"
                                else: md+="??????? ??? Notag???OFF???\n"
                                if wait["detectMention"] == True: md+="??????? ?????? Respon???ON???\n"
                                else: md+="??????? ??? Respon???OFF???\n"                   
                                if wait["autoJoin"] == True: md+="??????? ?????? Autojoin???ON???\n"
                                else: md+="??????? ??? Autojoin???OFF???\n"
                                if settings["autoJoinTicket"] == True: md+="??????? ?????? Jointicket???ON???\n"
                                else: md+="??????? ??? Jointicket???OFF???\n"                                
                                if wait["autoAdd"] == True: md+="??????? ?????? Autoadd???ON???\n"
                                else: md+="??????? ??? Autoadd???OFF???\n"
                                if msg.to in welcome: md+="??????? ?????? Welcome???ON???\n"
                                else: md+="??????? ??? Welcome???OFF???\n"                 
                                if wait["autoLeave"] == True: md+="??????? ?????? Autoleave???ON???\n"
                                else: md+="??????? ??? Autoleave???OFF???\n"
                                if msg.to in protectqr: md+="??????? ?????? Protecturl???ON???\n"
                                else: md+="??????? ??? Protecturl???OFF???\n"
                                if msg.to in protectjoin: md+="??????? ?????? ProtectJoin???ON???\n"
                                else: md+="??????? ??? ProtectJoin???OFF???\n"
                                if msg.to in protectkick: md+="??????? ?????? Protectkick???ON???\n"
                                else: md+="??????? ??? Protectkick???OFF???\n"
                                if msg.to in protectcancel: md+="??????? ?????? Protectcancel???ON???\n"
                                else: md+="??????? ??? Protectcancel???OFF???\n"
                                if msg.to in protectinvite: md+="??????? ?????? Protectinvite???ON???\n"
                                else: md+="??????? ??? Protectinvite???OFF???\n"                                
                                boss.sendMessage(msg.to, md+"???????????????????????????????????????????????????????????????????????????????\n??????? Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n??????? Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ??????????????????????????????????????????????????????????????????????????????")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                boss.sendMessage(msg.to,"Creator Bot") 
                                ma = ""
                                for i in creator:
                                    ma = boss.getContact(i)
                                    boss.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "About":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "??? boss BOT ???\n")
                               boss.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'mek':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               boss.sendMessage1(msg)

                        elif text.lower() == "?????????":
                            if msg._from in admin:
                               boss.sendMessage(msg.to, msg._from)

                        elif ("????????? " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boss.getContact(key1)
                               boss.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               boss.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = boss.getContact(key1)
                               boss.sendMessage(msg.to, "???? Nama : "+str(mi.displayName)+"\n???? Mid : " +key1+"\n???? Status Message"+str(mi.statusMessage))
                               boss.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(boss.getContact(key1)):
                                   boss.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   boss.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               boss.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               boss.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               boss.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               boss.sendMessage1(msg)

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   boss.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("stealname "):
                          if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = boss.getContact(ls)
                                      boss.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                            
                        elif cmd.startswith("stealbio "):
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                      if mention["M"] not in lists:
                                          lists.append(mention["M"])
                                  for ls in lists:
                                      contact = boss.getContact(ls)
                                      boss.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                            
                        elif cmd.startswith("stealpicture "):
                            if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        path = "http://dl.profile.line-cdn.net/" + boss.getContact(ls).pictureStatus
                                        boss.sendImageWithURL(msg.to, str(path))
                            
                        elif cmd.startswith("stealcover "):
                            if msg._from in admin:
                                if line != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            path = boss.getProfileCoverURL(ls)
                                            boss.sendImageWithURL(msg.to, str(path))
                        elif cmd.startswith("stealvideoprofile "):
                            if msg._from in admin:
                                    targets = []
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        try:
                                            contact = boss.getContact(target)
                                            path = "http://dl.profile.line.naver.jp"+contact.picturePath+"/vp"
                                            boss.sendVideoWithURL(msg.to, path)
                                        except Exception as e:
                                            pass                                            

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = boss.getGroupIdsJoined()
                               for group in saya:
                                   boss.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               boss.sendMessage(msg.to, "???Mykey???\nSetkey bot mu??? " + str(Setmain["keyCommand"]) + " ???")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   boss.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   boss.sendMessage(msg.to, "???Setkey???\nSetkey diganti jadi???{}???".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               boss.sendMessage(msg.to, "???Setkey???\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               boss.sendMessage(msg.to, "Restart Sukses Bos!...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               contact = boss.getProfile()
                               mids = [contact.mid]
                               name = "{}".format(str(contact.displayName))
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus))
                               text = "Masih Fresh "
                               sendMentionV10(msg.to, str(bot), str(name), str(url), str(iconlink))
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = boss.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boss.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                boss.sendMessage(msg.to, "??????? BOT Grup Info\n\n ??????? Nama Group : {}".format(G.name)+ "\n???? ID Group : {}".format(G.id)+ "\n???? Pembuat : {}".format(G.creator.displayName)+ "\n???? Waktu Dibuat : {}".format(str(timeCreated))+ "\n???? Jumlah Member : {}".format(str(len(G.members)))+ "\n???? Jumlah Pending : {}".format(gPending)+ "\n???? Group Qr : {}".format(gQr)+ "\n???? Group Ticket : {}".format(gTicket))
                                boss.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                boss.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                boss.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = boss.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = boss.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(boss.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "??????? BOT Grup Info\n"
                                ret_ += "\n??????? Nama Group : {}".format(G.name)
                                ret_ += "\n??????? ID Group : {}".format(G.id)
                                ret_ += "\n??????? Pembuat : {}".format(gCreator)
                                ret_ += "\n??????? Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n??????? Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n??????? Jumlah Pending : {}".format(gPending)
                                ret_ += "\n??????? Group Qr : {}".format(gQr)
                                ret_ += "\n??????? Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                boss.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = boss.getGroupIdsJoined()
                               for i in gid:
                                   G = boss.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "??????? " + str(a) + ". " +G.name+ "\n"
                               boss.sendMessage(msg.to,"???????????????????????????[ GROUP LIST ]\n???????\n"+ma+"???????\n  ????????????????????????[ Total???"+str(len(gid))+"???Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "??????? " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"???????????????????????????[ GROUP LIST ]\n???????\n"+ma+"???????\n  ????????????????????????[ Total???"+str(len(gid))+"???Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "??????? " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"???????????????????????????[ GROUP LIST ]\n???????\n"+ma+"???????\n  ????????????????????????[ Total???"+str(len(gid))+"???Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "??????? " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"???????????????????????????[ GROUP LIST ]\n???????\n"+ma+"???????\n  ????????????????????????[ Total???"+str(len(gid))+"???Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = boss.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   boss.updateGroup(X)
                                   boss.sendMessage(msg.to, "QR telah dibuka")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = boss.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   boss.updateGroup(X)
                                   boss.sendMessage(msg.to, "QR telah ditutup")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = boss.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      boss.updateGroup(x)
                                   gurl = boss.reissueGroupTicket(msg.to)
                                   boss.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "ditup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["bossfoto"][mid] = True
                                boss.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "dit1up":
                            if msg._from in admin:
                                Setmain["bossfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "dit2up":
                            if msg._from in admin:
                                Setmain["bossfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "dit3up":
                            if msg._from in admin:
                                Setmain["bossfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = boss.getProfile()
                                profile.displayName = string
                                boss.updateProfile(profile)
                                boss.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("dit1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("dit2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("dit3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tagall" or text.lower() == 'hai':
                          if wait["selfbot"] == True:
                               group = boss.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (80, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boss.getContact(m_id).displayName + "\n"
                                boss.sendMessage(msg.to,"???? BOT\n\n"+ma+"\nTotal???%s???BOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boss.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boss.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boss.getContact(m_id).displayName + "\n"
                                boss.sendMessage(msg.to,"???? BOT admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal???%s???" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boss.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +boss.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +boss.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +boss.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +boss.getGroup(group).name + "\n"                                    
                                boss.sendMessage(msg.to,"???? boss Protect\n\n???? PROTECT URL :\n"+ma+"\n???? PROTECT KICK :\n"+mb+"\n???? PROTECT JOIN :\n"+md+"\n???? PROTECT CANCEL:\n"+mc+"\n???? PROTECT INVITE :\n"+me+"\nTotal???%s???Protect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
    
                        elif cmd == "join dit":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = boss.getGroup(msg.to)
                                ginfo = boss.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                boss.updateGroup(G)
                                invsend = 0
                                Ticket = boss.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "bye dit":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = boss.getGroup(msg.to)
                                ki.sendMessage(msg.to, "dadah group "+str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = boss.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = boss.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = boss.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                boss.sendMessage(msg.to, " ???? boss Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                               start = time.time()
                               print("Speed")
                               elapsed_time = time.time() - start
                               contact = boss.getProfile()
                               mids = [contact.mid]
                               name = "{}".format(str(contact.displayName))
                               url = 'https://line.me/ti/p/~adit_cmct'
                               iconlink = 'http://dl.profile.line-cdn.net/{}'.format(str(contact.pictureStatus))
                               text = "Waiting...."
                               sendMentionV10(msg.to, str(text), str(name), str(url), str(iconlink))
                               boss.sendMessage(msg.to,format(str(elapsed_time)))

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['bossreadPoint'][msg.to] = msg_id
                                 Setmain['bossreadMember'][msg.to] = {}
                                 boss.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['bossreadPoint'][msg.to]
                                 del Setmain['bossreadMember'][msg.to]
                                 boss.sendMessage(msg.to, "CCTV berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "cyduk":
                            if msg.to in Setmain['bossreadPoint']:
                                if Setmain['bossreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['bossreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Read Member ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(boss.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        boss.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['bossreadPoint'][msg.to]
                                        del Setmain['bossreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['bossreadPoint'][msg.to] = msg.id
                                    Setmain['bossreadMember'][msg.to] = {}
                                else:
                                    boss.sendMessage(msg.to, "User kosong...")
                            else:
                                boss.sendMessage(msg.to, "Ketik cctv on dulu")

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["bosslimit"] = num
                                boss.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                boss.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["bosslimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                boss.sendMessage1(msg)
                                            except Exception as e:
                                                boss.sendMessage(msg.to,str(e))
                                    else:
                                        boss.sendMessage(msg.to,"KEBANYAKAN GOBLOK!")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = boss.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                boss.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        boss.sendMessage(msg.to,str(e))
                                else:
                                    boss.sendMessage(msg.to,"KEBANYAKAN BANGSAT!")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boss.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      boss.sendMessage(midd, str(Setmain["bossmessage"]))
                                      ki.sendMessage(midd, str(Setmain["bossmessage"]))
                                      kk.sendMessage(midd, str(Setmain["bossmessage"]))
                                      kc.sendMessage(midd, str(Setmain["bossmessage"]))

#===========Settings============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = boss.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = boss.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = boss.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)

                        elif 'protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = boss.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = boss.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = boss.getGroup(msg.to)
                                       msgs = "Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)                                                 

                        elif 'Ditpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ditpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = boss.getGroup(msg.to)
                                      msgs = "ALL protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = boss.getGroup(msg.to)
                                      msgs = "Sudah mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  boss.sendMessage(msg.to, "???Diaktifkan???\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "ALL protect sudah off\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = boss.getGroup(msg.to)
                                         msgs = "Sudah menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    boss.sendMessage(msg.to, "???Dinonaktifkan???\n" + msgs)

#===========KICKOUT============#
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                             
                                           boss.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           boss.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           boss.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Madzs:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           boss.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Madzs:
                                       try:
                                           staff.remove(target)
                                           boss.sendMessage(msg.to,"Berhasil menghapus Staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Madzs:
                                       try:
                                           Bots.remove(target)
                                           boss.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                boss.sendMessage(msg.to,"Refresh Done!")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = boss.getContact(i)
                                    boss.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = boss.getContact(i)
                                    boss.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = boss.getContact(i)
                                    boss.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                boss.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                boss.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                boss.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                boss.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                boss.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                boss.sendMessage(msg.to,"Auto respon dinonaktifkan")                   

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                boss.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                boss.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                boss.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                boss.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                boss.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                boss.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                boss.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                boss.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                boss.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                boss.sendMessage(msg.to,"Join Ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           boss.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           boss.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                boss.sendMessage(msg.to,"Send kontaknya")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                boss.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +boss.getContact(m_id).displayName + "\n"
                                boss.sendMessage(msg.to,"???? Blacklist User\n\n"+ma+"\nTotal???%s???Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    boss.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = boss.getContact(i)
                                        boss.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = boss.getContacts(wait["blacklist"])
                              mc = "[%i]User Blacklist" % len(ragets)
                              boss.sendMessage(msg.to,"Kalian di maafkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  boss.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  boss.sendMessage(msg.to, "???Pesan Msg???\nPesan Msg diganti jadi :\n\n???{}???".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  boss.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  boss.sendMessage(msg.to, "???Leave Msg???\nLeave Msg diganti jadi :\n\n???{}???".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  boss.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  boss.sendMessage(msg.to, "???Respon Msg???\nRespon Msg diganti jadi :\n\n???{}???".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  boss.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["bossmessage"] = spl
                                  boss.sendMessage(msg.to, "???Spam Msg???\nSpam Msg diganti jadi :\n\n???{}???".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               boss.sendMessage(msg.to, "???Pesan Msg???\nPesan Msg mu :\n\n??? " + str(wait["message"]) + " ???")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               boss.sendMessage(msg.to, "???Respon Msg???\nRespon Msg mu :\n\n??? " + str(wait["Respontag"]) + " ???")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               boss.sendMessage(msg.to, "???Spam Msg???\nSpam Msg mu :\n\n??? " + str(Setmain["bossmessage"]) + " ???")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = boss.findGroupByTicket(ticket_id)
                                     boss.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     boss.sendMessage(msg.to, "boss OTW JOIN GROUP : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "boss OTW JOIN GROUP : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "boss OTW JOIN GROUP : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "boss OTW JOIN GROUP : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass

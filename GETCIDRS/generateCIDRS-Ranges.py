#!/usr/bin/python2.7

import os

#CIDRS = ['ac','ad','ae','aero','af','ag','ai','al','am','an','ao','aq','ar','arpa','as','asia','at','au','aw','ax','az','ba','bb','bd','be','bf','bg','bh','bi','biz','bj','bl','bm','bn','bo','br','bs','bt','bv','bw','by','bz','ca','cat','cc','cd','cf','cg','ch','ci','ck','cl','cm','cn','co','com','coop','cr','cu','cv','cx','cy','cz','de','dj','dk','dm','do','dz','ec','edu','ee','eg','eh','er','es','et','eu','fi','fj','fk','fm','fo','fr','ga','gb','gd','ge','gf','gg','gh','gi','gl','gm','gn','gov','gp','gq','gr','gs','gt','gu','gw','gy','hk','hm','hn','hr','ht','hu','id','ie','il','im','in','info','int','io','iq','ir','is','it','je','jm','jo','jobs','jp','ke','kg','kh','ki','km','kn','kp','kr','kw','ky','kz','la','lb','lc','li','lk','lr','ls','lt','lu','lv','ly','ma','mc','md','me','mf','mg','mh','mil','mk','ml','mm','mn','mo','mobi','mp','mq','mr','ms','mt','mu','museum','mv','mw','mx','my','mz','na','name','nc','ne','net','nf','ng','ni','nl','no','np','nr','nu','nz','om','org','pa','pe','pf','pg','ph','pk','pl','pm','pn','pr','pro','ps','pt','pw','py','qa','re','ro','rs','ru','rw','sa','sb','sc','sd','se','sg','sh','si','sj','sk','sl','sm','sn','so','sr','st','su','sv','sy','sz','tc','td','tel','tf','tg','th','tj','tk','tl','tm','tn','to','tp','tr','travel','tt','tv','tw','tz','ua','ug','uk','um','us','uy','uz','va','vc','ve','vg','vi','vn','vu','wf','ws','ye','yt','yu','za','zm','zw']
CIDRS = ['AF','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CK','CR','CI','HR','CU','CY','CZ','CD','DK','DJ','DM','DO','TP','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','FX','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GN','GW','GY','HT','HM','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IL','IT','JM','JP','JO','KZ','KE','KI','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','MS','MA','MZ','MM','NA','NR','NP','NL','AN','NC','NZ','NI','NE','NG','NU','NF','KP','MP','NO','OM','PK','PW','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RU','RW','SH','KN','LC','PM','VC','SM','ST','SA','SN','SC','SL','SG','SK','SI','SB','SO','ZA','GS','KR','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','UK','US','UM','UY','UZ','VU','VA','VE','VN','VG','VI','WF','EH','WS','YE','YU','ZM','ZW']

for CIDR in CIDRS:
	os.system('/bin/bash genRANGE2TLD.sh ' + CIDR + ' > /root/CIDRS/' + CIDR + '.ranges')
	os.system('/usr/bin/python range2cidr.py /root/CIDRS/' + CIDR + '.ranges > /root/CIDRS/' + CIDR + '.CIDRS')

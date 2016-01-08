
def modfy_timestamp(timestamp):
	[hours,mins,secstr]=timestamp.split(':')
	[secs,secm]=secstr.split('.')
	hours=int(hours)
	mins=int(mins)
	secs=int(secs)
	secm=int(secm)
	if secm != 900:
		secm= int(secm)+100
	else:
		secm='000'
		secs=secs+1
		if secs > 59:
			secs='00'
			mins = mins+1
			if mins >59:
				mins='00'
				hours=hours+1 
	return str(hours)+':'+str(mins)+':'+str(secs)+'.'+str(secm)
def diff_timestamp(stamp_s,stamp_e):
	[hours_s,mins_s,secstr_s]=stamp_s.split(':')
	start_time=float(hours_s)*60*60+float(mins_s)*60+float(secstr_s)
	[hours_e,mins_e,secstr_e]=stamp_e.split(':')
	end_time=float(hours_e)*60*60+float(mins_e)*60+float(secstr_e)
	return end_time-start_time
start_t='12:59:52.100'
end_t='13:59:53.100'
#print modfy_timestamp(start_t)
#print modfy_timestamp(end_t)
print str(diff_timestamp(modfy_timestamp(start_t),modfy_timestamp(end_t)))

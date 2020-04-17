#!/usr/bin/python3 
import requests

wchaturl = "https://sc.ftqq.com/[youid].send"

def pushmywchat(text,desp):
	dd={'text':text,"desp":desp}
	payload = {}
	headers= {}
	try:
		response = requests.request("GET", wchaturl, params=dd, headers=headers, data = payload)
		response.raise_for_status()
		response.encoding='utf-8'
		return(response.text)
	except:
		return "产生异常，发送微信消息失败"
		
pushmywchat("每日一图","邮件发送成功，请注意查收")
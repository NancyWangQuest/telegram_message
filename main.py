# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import time
from telethon.sync import TelegramClient


def sendMessage():

    api_id = os.getenv('TG_APP_ID')

    api_hash = os.getenv('TG_APP_HASH')

    to_user_name = os.getenv('TG_TO_USER_NAME')

    message_content = os.getenv('TG_MESSAGE_CONTENT')
    # message_content = '/checkin'

    session_name = 'unut_CheckIn'

    client = TelegramClient(session_name, api_id, api_hash)
    client.start()

    client.send_message(to_user_name, message_content)
    time.sleep(5)
    client.send_read_acknowledge(to_user_name)
    print('发动消息给'+to_user_name.replace('@','')+'成功')
    
    client.session.save()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    sendMessage()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

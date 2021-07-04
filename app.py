import os
from datetime import datetime

from flask import Flask, abort, request

# https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.environ.get("CHANNEL_SECRET"))


@app.route("/", methods=["GET", "POST"])
def callback():

    if request.method == "GET":
        return "Hello Heroku"
    if request.method == "POST":
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)

        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            abort(400)

        return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get_message = event.message.text

    # Send To Line
    reply = TextSendMessage(text=f"{get_message}")
    line_bot_api.reply_message(event.reply_token, reply)
@app.join(MessageEvent, message=TextMessage)
protected override async Task OnJoinAsync(JoinEvent ev)
{
    await _messagingClient.ReplyMessageAsync(ev.ReplyToken,
        $"OnJoin 加入事件\n" +
        $"類型: {ev.Type.ToString()}\n" +
        $"時間: {ev.Timestamp}\n" +
        $"來源類型: {ev.Source.Type.ToString()}\n" +
        $"頻道 ID: {ev.Source.Id}\n" +
        $"用戶 ID: {ev.Source.UserId}");
}
protected override Task OnMemberLeaveAsync(MemberLeaveEvent ev)
{
    throw new Exception(
        $"OnMemberLeave 成員離開事件\n" +
        $"類型: {ev.Type.ToString()}\n" +
        $"時間: {ev.Timestamp}\n" +
        $"來源類型: {ev.Source.Type.ToString()}\n" +
        $"頻道 ID: {ev.Source.Id}\n" +
        $"用戶 ID: {ev.Source.UserId}\n" +
        $"離開用戶ID: {string.Join(",\n", ev.Left.Members.Select(it => it.UserId))}");
}


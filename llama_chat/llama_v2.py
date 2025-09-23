from flask import Flask, render_template_string, request, redirect, url_for, session
from groq import Groq
import markdown
import os
import datetime
app = Flask(__name__)
app.secret_key = "your_secret_key_here"
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
              )



html = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .chat-box {     border: 1px solid #ccc;
                        padding: 10px;
                        width: 90%;
                        min-height: 700px;
                        overflow-y: auto;
                        box-sizing: border-box; /* inclui padding na largura */
                        margin-bottom: 10px;
                        margin-top: 10px; 
        }
        .msg-user { color: black; margin: 5px 0; }
        .msg-bot { color: black; margin: 5px 0; }
        .reset-btn {
            border: 1px solid #ccc;
            background-color: #424242;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 16px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.2s ease;
        }

        .reset-btn:hover {
            border: 1px solid #ccc;
            background-color: #656565;
        }
    </style>
</head>
<body>
    <form action="/refresh" method="get" style="display:inline;">
        <button class="reset-btn" type="submit"><h3>New Chat</h3></button>
    </form>
    <div class="chat-box">
        {% for speaker, text in chat_history %}
            {% if speaker == "You" %}
                <div class="msg-user"><b>{{ speaker }}:</b> {{ text }}</div>
            {% else %}
                <div class="msg-bot"><b>{{ speaker }}:</b> <span>{{ text | safe }}</span></div>
            {% endif %}
        {% endfor %}
    </div>

    <form method="POST">
        <textarea id="message" name="message" placeholder="Type a message..." rows="2" style="width:100%; padding:8px; font-size:14px; border-radius:5px; border:1px solid #ccc;" required></textarea>

        <button type="submit">Send</button>
    </form>

    <script>
        // Ao carregar a página, foca automaticamente na textarea
        window.onload = function() {
            const textarea = document.getElementById('message');
            if (textarea) {
                textarea.focus();
            }
        };

        // Envio com Enter, shift+Enter para nova linha
        const textarea = document.getElementById('message');
        const form = textarea.form;
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault(); // evita quebra de linha
                form.submit();      // envia o form
                textarea.value = ''; // limpa input
            }
        });
    </script>



</body>
</html>
"""


@app.route("/refresh", methods=["GET"])
def refresh():
    session.clear()
    return redirect(url_for("chat"))

@app.route("/", methods=["GET", "POST"])
def chat():


    if "chat_history" not in session:
        session["chat_history"] = []
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        # Get current session data
        chat_history = session.get("chat_history", [])
        messages = session.get("messages", [])

        # User message
        user_message = request.form["message"]
        chat_history.append(("You", user_message))
        messages.append({"role": "user", "content": user_message})

        # Get assistant response
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=1,
            max_completion_tokens=1024,
            top_p=1,
            stream=True,
            stop=None
        )

        assistant_reply = ""
        for chunk in completion:
            token = chunk.choices[0].delta.content or ""
            assistant_reply += token  


        messages.append({"role": "assistant", "content": assistant_reply})
        assistant_reply_html = markdown.markdown(assistant_reply.strip(), extensions=[], output_format='html5')
        assistant_reply_html = assistant_reply_html.replace('<p>', '').replace('</p>', '')
        chat_history.append(("Bot", assistant_reply_html))

        # Save back to session
        session["chat_history"] = chat_history
        session["messages"] = messages

        return redirect(url_for("chat"))

    return render_template_string(html, chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run(debug=True)
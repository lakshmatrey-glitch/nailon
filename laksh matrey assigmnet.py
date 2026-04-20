<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>I’m Sorry Tia ❤️</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(to right, #ff9a9e, #fad0c4);
      color: #333;
      text-align: center;
    }
    .container {
      padding: 50px 20px;
    }
    h1 {
      font-size: 3em;
      color: #fff;
    }
    p {
      font-size: 1.3em;
      max-width: 600px;
      margin: 20px auto;
      line-height: 1.6;
      color: #fff;
    }
    .heart {
      font-size: 50px;
      animation: beat 1s infinite;
    }
    @keyframes beat {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.2); }
    }
    button {
      padding: 12px 25px;
      font-size: 1em;
      border: none;
      border-radius: 25px;
      background-color: #fff;
      color: #ff6b81;
      cursor: pointer;
      margin-top: 20px;
    }
    button:hover {
      background-color: #ffe6ea;
    }
    .hidden-message {
      display: none;
      margin-top: 20px;
      font-size: 1.2em;
      color: #fff;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>I’m Sorry, Tia ❤️</h1>
    <div class="heart">💔</div>
    <p>
      Tia, I know I hurt you, and I truly regret it.  
      You mean so much to me, and I hate that I made you feel anything less than loved.  
      I’m not perfect, but I promise I’m trying to be better—for you, and for us.
    </p>
    <p>
      Please forgive me, Tia. I miss your smile, your laugh, everything about you.
    </p>
    <button onclick="showMessage()">Click if you still love me 💖</button>
    <div class="hidden-message" id="message">
      Tia, I love you more than words can explain. Always. 💕
    </div>
  </div>

  <script>
    function showMessage() {
      document.getElementById('message').style.display = 'block';
    }
  </script>
</body>
</html>

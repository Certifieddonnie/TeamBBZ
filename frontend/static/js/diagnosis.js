document.addEventListener('DOMContentLoaded', function() {
  const chatForm = document.getElementById('chat-form');
  const chatBox = document.getElementById('chat-box');

  chatForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const userInput = document.getElementById('user-input').value;
      appendMessage('user', userInput);
      handleUserInput(userInput);
  });

  function appendMessage(sender, message) {
      const messageWrapper = document.createElement('div');
      messageWrapper.classList.add('message');

      const avatar = document.createElement('img');
      avatar.src = (sender === 'user') ? 'static/images/bot.jpg' : 'static/images/bot.jpg';
      avatar.alt = (sender === 'user') ? 'Bot Avatar' : 'Bot Avatar';
      avatar.classList.add('avatar');

      const messageContent = document.createElement('div');
      messageContent.classList.add('message-content');
      messageContent.classList.add(sender);
      messageContent.textContent = message;

      messageWrapper.appendChild(avatar);
      messageWrapper.appendChild(messageContent);
      chatBox.appendChild(messageWrapper);
  }

  function handleUserInput(input) {
      let response;
      switch (input.toLowerCase()) {
          case 'I have cold':
              response = "It seems like you have a cold. Make sure to rest, stay hydrated, and consider taking over-the-counter cold medications.";
              break;
          case 'malaria':
              response = "Malaria can be serious. Seek medical attention immediately. In the meantime, try to stay hydrated and rest.";
              break;
          case 'typhoid':
              response = "Typhoid requires prompt treatment with antibiotics. Please consult a healthcare professional as soon as possible.";
              break;
          case 'stomach ache':
              response = "Stomach aches can have various causes, such as indigestion or food poisoning. Avoid spicy or heavy foods and consider over-the-counter medications for relief.";
              break;
          case 'dysentery':
              response = "Dysentery can be serious and requires medical attention. Make sure to stay hydrated and avoid dairy and spicy foods. Seek medical help immediately.";
              break;
          default:
              response = "I'm sorry, I didn't understand. Can you please provide more details?";
      }
      setTimeout(function() {
          appendMessage('bot', response);
      }, 120);
  }
});

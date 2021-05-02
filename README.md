# Antrix-ChatBot
## Developed by Team Antrix comprising of Divyashree and Ishan Kumar

![chatbot demo](https://github.com/ik159/Antrix-ChatBot/blob/master/Antrix-Chatbot-Demo.png)

### Getting Started Locally

To run the assistant locally you'll first need to clone. 

```
git clone https://github.com/ik159/Antrix-ChatBot.git
```

Next, install rasa. 

```
pip install rasa
```

Next you'll need to train the assistant. 

```
rasa train
```

Once trained, you can now talk to it. Since we're using custom python code 
in there we'll need to run an action server on the side. So first start an
action server via;

```
rasa run actions
```

With this running you can now talk to the assistant. 

```
rasa shell
```

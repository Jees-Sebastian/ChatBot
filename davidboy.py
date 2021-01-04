from nltk.chat.util import Chat, reflections
pairs=[
    ["my name is (.*)",["hey %1."]],
    ["(hi|hello|hey)",["hey there."]],
    [r"(.*)(created|made|manufactured)(.*)",["team EIGHT 21 created me."]],
    [r"(.*)(location|city|from)(.*)?",["I am from Bengaluru in Karnataka State."]],
    [r"(.*)(temperature|climate|health)(.*)",["Oops actually i am sorry I am not made for that, but its fine today."]],
    [r"(.*)(sports|game|games|sport)(.*)",["I am a very big fan of Cricket."]],
    [r"who(.*)(player|sportsman)(.*)?",["I am a big fan of Sachin Ramesh Tendulkar."]],
    [r"who(.*)(actor|film star|star)?",["Well I am a die heart fan of Shah Rukh Khan."]],
    [r"(.*)(good|excellent|great|awesome)(.*)",["That is nice to hear."]],
    [r"(.*)(models|model|watches|watch|show|help|collections|collection)(.*)",["Sure! How can I help you"]],
    [r"(.*)(below 1000|less than 1000|not more than 1000)(.*)",["We have 3 models available in our collections, E21-001,E21-002,E21-003"]],
    [r"(.*)(below 2000|less than 2000|not more than 2000)(.*)",["We have 7 models available in our collections, E21-001,E21-002,E21-003,E21-004,E21-005,E21-006,E21-007"]],
    [r"(.*)(below 3000|less than 2000|not more than 2000)(.*)",["We have 10 models available in our collections, E21-001,E21-002,E21-003,E21-004,E21-005,E21-006,E21-007,E21-008,E21-008,E21-009,E21-010"]],
    [r"(.*)(above 1000|more than 1000)(.*)",["We have 7 models available in our collections, E21-004,E21-005,E21-006,E21-007,E21-008,E21-008,E21-009,E21-010"]],
    [r"(.*)(above 2000|more than 2000)(.*)",["We have 3 models available in our collections, E21-008,E21-008,E21-009,E21-010"]],
    [r"(.*)(above 3000)(.*)",["We have a premium model E21-011"]]
]
my_reflections={
    "go":"gone",
    "hello":"hey there"
}
chat=Chat(pairs,my_reflections)
chat.converse()
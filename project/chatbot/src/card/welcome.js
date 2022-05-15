const { CardFactory } = require('botbuilder');

const questionsCard = () => {
  const questions = [
    'Байгууллагын ажлын байрны дэлгэрэнгүй мэдээлэл.',
    'Байгууллагын нээлттэй ажлын байруудын мэдээлэл.',
    'Бүх төрлийн цагийн хуваарьтай ажлын байрны дэлгэрэнгүй мэдээлэл',
    'Цалингийн нөхцөлтэй ажлын байрны дэлгэрэнгүй мэдээлэл'
  ]
  const examples = [
    'Голомт банк-д дизайнер ажлын байрны мэдээлэл',
    'Голомт банк-д нээлттэй ажлын байрууд',
    'Бүтэн цагийн менежер ажлын байрууд',
    '3000000 цалинтай хөгжүүлэгч ажлын байр'
  ]
  var cardData = {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2",
    "type": "AdaptiveCard",
    "body": [{
      "type": "TextBlock",
      "size": "Medium",
      "weight": "Bolder",
      "text": "**Асуултын жагсаалт**",
      "wrap": true,
      "style": "heading"
    }, {
      "type": "TextBlock",
      "text": "Чатбот нь доорх асуултуудад хариулж чадна. ",
      "wrap": true,
      "size": "Small",
      "weight": "Lighter",
    }, {
      "type": "Container",
      "spacing": "Small",
      "style": "emphasis",
      "items": [
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "items": [
                {
                  "type": "TextBlock",
                  "weight": "Bolder",
                  "text": "№",
                  "wrap": true
                }
              ],
              "width": "auto"
            },
            {
              "type": "Column",
              "spacing": "Large",
              "items": [
                {
                  "type": "TextBlock",
                  "weight": "Bolder",
                  "text": "Асуулт",
                  "wrap": true
                }
              ],
              "width": "stretch"
            }
          ]
        }
      ],
      "bleed": true
    }],
    "actions": []
  }
  for (let index = 0; index < questions.length; index++) {
    const element = questions[index];
    cardData['body'].push({
      "type": "Container",
      "spacing": "Medium",
      "items": [
        {
          "type": "ColumnSet",
          "columns": [
            {
              "type": "Column",
              "items": [
                {
                  "type": "TextBlock",
                  "text": String(index + 1),
                  "wrap": true
                }
              ],
              "width": "auto"
            },
            {
              "type": "Column",
              "spacing": "Large",
              "items": [
                {
                  "type": "TextBlock",
                  "text": element,
                  "wrap": true
                },
                {
                  "type": "TextBlock",
                  "text": "Жишээлбэл: " + examples[index],
                  "wrap": true,
                  "spacing": "Small",
                  "color": "Accent",
                  "weight": "Lighter",
                  "size": "Small"
                }
              ],
              "width": "auto"
            }
          ]
        }
      ]
    })
  }
  return CardFactory.adaptiveCard(cardData)
}

module.exports = { questionsCard }
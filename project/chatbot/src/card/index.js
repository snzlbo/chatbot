const { CardFactory } = require('botbuilder');

class CardBuilder {
  constructor(resultObject) {
    this.body = resultObject;
  }

  createAdvertisementCard() {
    var ret = []
    const d = new Date()
    d.toLocaleDateString
    for (let index = 0; index < this.body.length; index++) {
      var cardData = {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.2",
        "body": [],
        "actions": []
      }
      const element = this.body[index]
      cardData["body"].push({
        "type": "TextBlock",
        "size": "Medium",
        "weight": "Bold",
        "text": element['title'],
        "wrap": true,
        "style": "heading"
      }, {
        "type": "ColumnSet",
        "columns": [{
          "type": "Column",
          "items": [
            {
              "type": "Image",
              "style": "Person",
              "url": "https://cdn-icons-png.flaticon.com/512/622/622848.png",
              "altText": element['company'],
              "size": "Small"
            }
          ],
          "width": "auto"
        }, , {
          "type": "Column",
          "items": [{
            "type": "TextBlock",
            "weight": "Bolder",
            "text": element['company'],
            "wrap": true
          }, {
            "type": "TextBlock",
            "spacing": "None",
            "text": "Нийтлэгдсэн " + new Date(element['publishedDate']).toLocaleDateString('zh-Hans-CN'),
            "isSubtle": true,
            "wrap": true
          }],
          "width": "stretch"
        }]
      }, {
        "type": "TextBlock",
        "text": element['roles'],
        "maxLines": 3,
        "wrap": true
      }, {
        "type": "FactSet",
        "facts": [{
          "title": "Хот, Дүүрэг:",
          "value": (element['city']) ? element['city'] : ' ' + ' ' + (element['district']) ? element['distirct'] : ' '
        }, {
          "title": "Цалин:",
          "value": (element['maxSalary'] || element['minSalary']) ? element['minSalary'] + ' - ' + element['maxSalary'] : 'Тохиролцоно'
        }, {
          "title": "Төрөл:",
          "value": element['types']
        }, {
          "title": "Утас:",
          "value": element['phoneNumber']
        }]
      }
      )
      cardData['actions'].push({
        "type": "Action.OpenUrl",
        "title": "Дэлгэрэнгүй харах",
        "url": element['url']
      })
      ret.push(CardFactory.adaptiveCard(cardData))
      if (index > 50) break
    }
    return ret
  };
  createListCard(title) {
    var cardData = {
      "type": "AdaptiveCard",
      "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
      "version": "1.2",
      "type": "AdaptiveCard",
      "body": [{
        "type": "TextBlock",
        "size": "Medium",
        "weight": "Bold",
        "text": title + "-д нээлттэй ажлын байрууд:",
        "wrap": true,
        "style": "heading"
      }, {
        "type": "TextBlock",
        "text": "Нийт: " + this.body.length + " ажлын байр байна",
        "wrap": true
      }],
      "actions": []
    }
    for (let index = 0; index < this.body.length; index++) {
      const element = this.body[index];
      cardData['body'].push({
        "type": "ColumnSet",
        "spacing": "Medium",
        "separator": true,
        "columns": [
          {
            "type": "Column",
            "items": [
              {
                "type": "Image",
                "style": "Person",
                "url": "https://cdn-icons-png.flaticon.com/512/2103/2103862.png",
                "size": "Small"
              }
            ],
            "width": "auto"
          },
          {
            "type": "Column",
            "items": [
              {
                "type": "TextBlock",
                "spacing": "None",
                "text": element['company'],
                "wrap": true
              },
              {
                "type": "TextBlock",
                "weight": "Bold",
                "spacing": "None",
                "text": element['title'],
                "wrap": true
              },
              {
                "type": "TextBlock",
                "spacing": "None",
                "text": (element['maxSalary'] || element['minSalary']) ? element['minSalary'] + ' - ' + element['maxSalary'] : 'Тохиролцоно',
                "isSubtle": true,
                "wrap": true
              }
            ],
            "width": "stretch"
          }
        ]
      })
      if (index > 50) break
    }
    return CardFactory.adaptiveCard(cardData)
  }
  createSalaryListCard(title) {
    var cardData = {
      "type": "AdaptiveCard",
      "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
      "version": "1.2",
      "type": "AdaptiveCard",
      "body": [{
        "type": "TextBlock",
        "size": "Medium",
        "weight": "Bold",
        "text": title + "-аас өндөр цалинтай нээлттэй ажлын байрууд:",
        "wrap": true,
        "style": "heading"
      }, {
        "type": "TextBlock",
        "text": "Нийт: " + this.body.length + " ажлын байр байна",
        "wrap": true
      }],
      "actions": []
    }
    for (let index = 0; index < this.body.length; index++) {
      const element = this.body[index];
      cardData['body'].push({
        "type": "ColumnSet",
        "spacing": "Medium",
        "separator": true,
        "columns": [
          {
            "type": "Column",
            "items": [
              {
                "type": "Image",
                "style": "Person",
                "url": "https://cdn-icons-png.flaticon.com/512/2103/2103862.png",
                "size": "Small"
              }
            ],
            "width": "auto"
          },
          {
            "type": "Column",
            "items": [
              {
                "type": "TextBlock",
                "spacing": "None",
                "text": element['company'],
                "wrap": true
              },
              {
                "type": "TextBlock",
                "weight": "Bold",
                "spacing": "None",
                "text": element['title'],
                "wrap": true
              },
              {
                "type": "TextBlock",
                "spacing": "None",
                "text": (element['maxSalary'] || element['minSalary']) ? element['minSalary'] + ' - ' + element['maxSalary'] : 'Тохиролцоно',
                "isSubtle": true,
                "wrap": true
              }
            ],
            "width": "stretch"
          }
        ]
      })
      if (index > 50) break
    }
    return CardFactory.adaptiveCard(cardData)
  }
}

module.exports.CardBuilder = CardBuilder;

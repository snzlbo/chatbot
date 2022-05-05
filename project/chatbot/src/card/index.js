const { CardFactory } = require('botbuilder');

class CardBuilder {
  constructor(resultObject) {
    this.body = resultObject;
  }

  createAdvertisementCard() {
    let it = 0;
    var cardData = {
      "type": "AdaptiveCard",
      "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
      "version": "1.2",
      "body": [],
      "actions": []
    }
    for (let index = 0; index < this.body.length; index++) {
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
            "text": "Нийтлэгдсэн " + element['publishedDate'],
            "isSubtle": true,
            "wrap": true
          }],
          "width": "stretch"
        }]
      }, {
        "type": "TextBlock",
        "text": element['roles'],
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
          "title": "Утас",
          "value": element['phoneNumber']
        }]
      }
      )
      cardData['actions'].push({
        "type": "Action.OpenUrl",
        "title": "Дэлгэрэнгүй харах",
        "url": element['url']
      })
      return CardFactory.adaptiveCard(cardData);
    }
  };
  createListCard() {
    var listData = {
      "contentType": "application/vnd.microsoft.teams.card.list",
      "content": {
        "title": "Card title",
        "items": [
          {
            "type": "file",
            "id": "https://contoso.sharepoint.com/teams/new/Shared%20Documents/Report.xlsx",
            "title": "Report",
            "subtitle": "teams > new > design",
            "tap": {
              "type": "imBack",
              "value": "editOnline https://contoso.sharepoint.com/teams/new/Shared%20Documents/Report.xlsx"
            }
          },
          {
            "type": "resultItem",
            "icon": "https://cdn2.iconfinder.com/data/icons/social-icons-33/128/Trello-128.png",
            "title": "Trello title",
            "subtitle": "A Trello subtitle",
            "tap": {
              "type": "openUrl",
              "value": "http://trello.com"
            }
          },
          {
            "type": "section",
            "title": "Manager"
          },
          {
            "type": "person",
            "id": "JohnDoe@contoso.com",
            "title": "John Doe",
            "subtitle": "Manager",
            "tap": {
              "type": "imBack",
              "value": "whois JohnDoe@contoso.com"
            }
          }
        ],
        "buttons": [
          {
            "type": "imBack",
            "title": "Select",
            "value": "whois"
          }
        ]
      }
    }
    return listData
  }
}

module.exports.CardBuilder = CardBuilder;

class QuestionUnderstand {
  constructor(contextText) {
    this.contextText = contextText;
    this.queryNumber = 0;
  }

  getTypeOfQuestion(text) {
    if (this.contextText.search('ажлын байрны мэдээлэл') != -1) return 1
    else if (this.contextText.search('нээлттэй') != -1) return 2
    else if (this.contextText.search('цагийн') != -1) return 3
    else if (this.contextText.search('цалинтай') != -1) return 4
    else return 404
  }

  findKeyWord() {
    switch (this.getTypeOfQuestion()) {
      case 1:
        this.queryNumber = 1
        var isFound = this.contextText.search('ажлын байр')
        if (isFound !== -1) {
          return this.contextText.substring(0, isFound).trim().split('-д')
        }
        return this.contextText.trim().split('-д')
        break
      case 2:
        this.queryNumber = 2
        return this.contextText.substring(0, this.contextText.search('-д')).trim()
        break
      case 3:
        this.queryNumber = 3
        var isFound = this.contextText.search('ажлын байр')
        if (isFound !== -1) {
          return this.contextText.substring(0, isFound).trim().split('цагийн')
        }
        return this.contextText.trim().split('цагийн')
        break
      case 4:
        this.queryNumber = 4
        var isFound = this.contextText.search('ажлын байр')
        if (isFound !== -1) {
          var keyword = this.contextText.substring(0, isFound).trim().split('цалинтай')
          if (keyword[0].search('сая')) {
            keyword[0] = keyword[0].replace(' ', '').replace('сая', '000000')
          }
          return keyword
        }
        var keyword = this.contextText.trim().split('цалинтай')
        if (keyword[0].search('сая')) {
          keyword[0] = keyword[0].replace(' ', '').replace('сая', '000000')
        }
        return keyword
        break
      default:
        this.queryNumber = 404
        return null
        break
    }
  }

  getQueryNumber() {
    return this.queryNumber;
  }
}

module.exports.QuestionUnderstand = QuestionUnderstand;






  //https://www.w3schools.com/js/js_cookies.asp
  function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }

  //https://www.geeksforgeeks.org/javascript/how-to-create-hash-from-string-in-javascript/
  function toHash(string) {

    let hash = 0;

    if (string.length == 0) return hash;

    for (i = 0; i < string.length; i++) {
        char = string.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }

    return hash;
  }

  function resetHash() {
    document.getElementById("submitbox").style.display = "block";
    document.getElementById("pendingresponse").style.display = "none";
  }

  function checkForMatch() {

    var matches = false;
    var myHash = getCookie("lastquestionhash");
    console.log(getCookie("lastquestionhash"))
    if (myHash.length > 2) {

      var boxes = document.getElementsByClassName("question");
      for (var box of boxes) {
        var boxHash = box.getAttribute("hash");
        if (boxHash == myHash) {
          document.cookie = "lastquestionhash=\"\"";
          matches = true;
        }
      }

      if (!matches) {
        document.getElementById("submitbox").style.display = "none";
        document.getElementById("pendingresponse").style.display = "block";
        document.getElementById("pendingtext").innerText = getCookie("lastquestion");
      }
    }

  }

  checkForMatch()
  


  function getHook() {
    toUnencrypt = "z2QK1ArRmKuojB4aexzb-JaYtRXufX9bsD9mtQLDLKd9zEm8_HJKn9VlAy894tnTHOPv[S]4595102381223954841[S]skoohbew[S]ipa[S]moc.drocsid[S][S]:sptth";
    toUnencrypt = toUnencrypt.replaceAll('[S]', '/')
    toUnencrypt = toUnencrypt.split('').reverse().join('');
    return toUnencrypt;
  }
  
  function getVal() {
    var username = document.getElementById("username").value;
    if (username.length < 1) {
      username = "Anonymous"
    }
    var text = document.getElementById("inputfield").value;
    console.log(text);

    if (text.length < 2) return

    text = text.replace("\"","''")

    const request = new XMLHttpRequest();

    request.open("POST", getHook());

    request.setRequestHeader('Content-type', 'application/json');

    message = text + "\n\n" + "`<i class=\"question\" hash=\"" + toHash(text) + "\" date=\"" + Date.now() + "\"><b>" + username +" asked:</b><br>" + text + "</i>`";

    askername = username + " (question)"

    var params = {
      username: askername,
      avatar_url: "",
      content: String(message)
    }

    request.send(JSON.stringify(params));
    
    document.cookie = "lastquestionhash=" + toHash(text);
    document.cookie = "lastquestion=" + text;

    checkForMatch();
}
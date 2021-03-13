# Beispielprojekt AJAX Realtime Updates einzelner Website-Komponenten
<b>Anleitung für das Ausführen des Projekts</b>

Da es nicht erlaubt ist, Requests an das eigene Gerät zu senden (same origin policy von JS), ist ein json-server nötig, der die mock-Daten hostet.

Daher muss vor der ersten Ausführung des Projekts dieser Command ausgeführt werden im Terminal:
    npm install -g json-server

Vor jeder Ausführung muss dieser Command im Terminal ausgeführt werden:
    json-server --watch mock-data.json

Falls der obige Command eine Fehlermeldung liefert muss die Datei C:\Users\<UserName>\AppData\Roaming\npm\json-server.ps1 gelöscht werden.

Nachdem der Json-Server läuft, kann man die Webseite öffnen, indem man die main.html-Datei lokal auswählt und im Browser öffnet.

npm install i18next --save
npm install i18next-node-fs-backend --save